# Import libraries for working with tables and graphs
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df_raw = pd.read_csv("https://code.s3.yandex.net/datasets/credit_scoring_eng.csv")

# Copy the dataset for working with it into the df variable or another
df = df_raw.copy()

# Examine the general information about the dataset

df.info()
df.sample(5)
df.describe()

# Count the volume of data:
print('Number of rows in the dataframe:', len(df))

# Count the number of missing values:
print('Number of missing values by columns:')
print(df.isna().sum())

# Ensure that all those with missing values in days employed also have missing values in monthly income:
df_isna = df.query('days_employed.isna() & total_income.isna()')
print('Information about rows without employment and income data:')
print(df_isna.info())

# Count the number of missing values in the dataset:
df_na_counts = df_raw.isna().sum()

# Count the number of rows in the dataset:
total_raws = len(df_raw)

# Calculate the percentage of missing values in the entire dataset:
df_na_share = df_na_counts / total_raws * 100

# Output the calculations:
print('Percentage of missing values in the column:')
print(df_na_share)

# Remove rows with missing values in the days_employed and total_income columns:
df.dropna(subset=['days_employed', 'total_income'], inplace=True)

# Check the result:
print('Number of missing values by columns:')
print(df.isna().sum())
print("Number of rows after removing missing values:")
print(len(df))

# Your code here

# Find all unique values in the education column:
unique_education = df['education'].unique()
# Find all unique values in the gender column:
unique_gender = df['gender'].unique()

# Output all unique values in the education column:
print('Unique values in the "education" column:')
print(unique_education)
# Output all unique values in the gender column:
print('Unique values in the "gender" column:')
print(unique_gender)

# Convert names to lowercase to eliminate implicit duplicates:
df['education'] = df['education'].str.lower()

# Check the result:
print('Unique values in the "education" column after processing:')
print(df['education'].unique())

# Analyze 'XNA' values in the gender column:
df_gender_xna = df.query('gender == "XNA"')
if not df_gender_xna.empty:
    print('Number of "XNA" values in the "gender" column:', len(df_gender_xna))
else:
    print('No "XNA" values found in the "gender" column.')

# Remove 'XNA' values in the gender column if they are less than 1%:
if len(df_gender_xna) / len(df) < 0.01:  # If less than 1% of data
    df = df[df['gender'] != 'XNA']
    print('Rows with "XNA" in "gender" have been removed.')

# Check the result:
print('Unique values in the "gender" column after processing:')
print(df['gender'].unique())

print("Number of rows after removing duplicates:")
print(len(df))

# Your code here

duplicate_rows = df.duplicated()
print("Number of duplicates in the dataframe:", duplicate_rows.sum())

# No duplicates in the dataframe.

# Find out how much data was removed during preprocessing:

# Find the initial number of rows in the dataset:
total_rows_count = len(df_raw)
# Find the number of rows in the dataset after preprocessing:
actual_rows_count = len(df)
# Calculate:
share = 100 - ((actual_rows_count / total_rows_count) * 100)
# Output:
print(f'Total lost in preprocessing: {share:.0f}% of data')

# Get basic statistical information for the total_income column:
df['total_income'].describe(percentiles=[0.5, 0.6, 0.7, 0.8, 0.95, 0.99])

# Define the outlier threshold as the 95th percentile of the total_income values:
outliers = df['total_income'].quantile(0.95)

# Filter the data, keeping only values above the identified outlier threshold:
new_df = df[df['total_income'] > outliers]

# Output describe() after filtering the data:
new_df['total_income'].describe()

# Your code here

# Set the size of the box:
plt.figure(figsize=(10, 6))

# Build a horizontal boxplot:
plt.boxplot(x=df['total_income'],  # monthly income data
            vert=False,     # horizontal boxplot
            showmeans=True, # show mean on the graph
            meanline=True,  # show mean as a line on the graph
            patch_artist=True,  # fill boxplot with color
            # set outliers color to red
            flierprops=dict(markerfacecolor='red'))
# Add a title to the chart:
plt.title("Analysis of Monthly Income Outliers")
# Add a label to the X axis:
plt.xlabel("Monthly Income")
plt.show()

# Check people with income over 200000:
df_max = df.query('total_income > 200000')
df_max

# Get basic statistical information for the dob_years column:
df['dob_years'].describe()

# Find out how many rows in the dob_years column contain 0:
df_0_years = df.query('dob_years == 0')
df_0_years

# Since the number of rows with a value of 0 in the dob_years column is small, we decided to replace these values with the mean
# value in the dob_years column

# Create a variable that will store the mean value of the dob_years column:
value_age_replace = round(df['dob_years'].mean())
# Perform the replacement
df['dob_years'].replace(to_replace=0, value=value_age_replace, inplace=True)
# Check the basic statistical information for the dob_years column after replacement:
df['dob_years'].describe()

# Get basic statistical information for the children column:
df['children'].describe()

# Examine the rows where the value -1 appears:
df_outliers_negative = df.query('children == -1')
# Output the number of these rows:
print('Number of rows where "children" is -1:', len(df_outliers_negative))

# Most likely, this is a data entry error where -1 was intended to be 1 child. Therefore, in the next step
# we will make the replacement.

# Replace -1 in the children column with 1:
df['children'].replace(to_replace=-1, value=1, inplace=True)
print('Unique values in the "children" column:', df['children'].unique())

# Examine the rows where the value 20 appears in the children column:
df_outliers_max = df.query('children == 20')
# Output the number of these rows:
print('Number of rows where "children" is 20:', len(df_outliers_max))

# Most likely, this is a data entry error where the value 20 should have been entered as 2.
# Therefore, in the next step, we will make the replacement.

# Replace 20 in the children column with 2:
df['children'].replace(to_replace=20, value=2, inplace=True)
print('Unique values in the "children" column:', df['children'].unique())

# Define the names for 4 categories:
cat_names = ['Very Low Income', 'Low Income', 'Medium Income', 'High Income']

# Divide the data into 4 categories using percentiles:
df['category_qcat'] = pd.qcut(df['total_income'], q=[0, 0.14, 0.34, 0.78, 1],
                              labels=cat_names)
print(df['category_qcat'].value_counts()) 

# The division was made into 4 categories because during preprocessing
# the rows with a value of 0 in the total_income column (monthly income) were removed. Therefore, only clients with incomes remain.

# Your code here

def age(dob_years):
    
    # Define a conditional construct to check the value of dob_years:

    # If the client is up to 40 years old:
    if dob_years <= 40:
        return 'Up to 40 years'
    
    # If the client is older than 40 years:
    elif dob_years > 40:
        return 'Older than 40 years'
    
# Create a new column with age categorization:
df['age_category'] = df['dob_years'].apply(age)

# Display the first 10 rows on the screen:
print(df[['dob_years', 'age_category']].head(10)) 

# Your code here

def children_count(children):
    
    # Define a conditional construct to check the value of children:

    # If there are no children:
    if children < 1:
        return 'No children'
    
    # If there are 1 or 2 children:
    elif 1 <= children <= 2:
        return '1 to 2 children'
    
    # If there are more than 3 children:
    elif children >= 3:
        return '3 or more children'
    
# Create a new column with categorization by number of children:
df['childrens_category'] = df['children'].apply(children_count)

# Display the first 10 rows on the screen:
print(df[['children', 'childrens_category']].head(10))

# Create a pivot table to study the relationship between income level and whether the client was a debtor:
df_pivot = df.pivot_table(index='category_qcat', columns='debt', values='total_income', aggfunc='count')

# Calculate the total number of clients in each category:
df_pivot['total'] = df_pivot.sum(axis=1)

# Calculate the percentage of clients without debt:
df_pivot['no_debt_percentage'] = (df_pivot[1] / df_pivot['total']) * 100

# Convert the pivot table to a long format for use with seaborn:
df_pivot_long = df_pivot.reset_index()
df_pivot_long = df_pivot_long[['category_qcat', 'no_debt_percentage']]

# Plotting the graph using seaborn:
plt.figure(figsize=(10, 6))
ax = sns.barplot(x='category_qcat', y='no_debt_percentage', data=df_pivot_long)
plt.title("Share of Debtors by Income Categories")
plt.xlabel("Income Category")
plt.ylabel("%")
plt.xticks(rotation=45)

# Add percentage values above each bar:
for p in ax.patches:
    ax.annotate(f'{p.get_height():.1f}%', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', fontsize=12, color='black', xytext=(0, 5),
                textcoords='offset points')
plt.show()

# Creating a pivot table to study the dependency on age and whether the client was a debtor:

df_pivot = df.pivot_table(index='age_category', columns='debt',
values='total_income', aggfunc='count')
# Calculating the total number of clients in each category:

df_pivot['total'] = df_pivot.sum(axis=1)
# Calculating the percentage of debtor clients:

df_pivot['no_debt_percentage'] = (df_pivot[1] / df_pivot['total']) * 100
# Converting the pivot table to long format for use with seaborn:

df_pivot_long = df_pivot.reset_index()
df_pivot_long = df_pivot_long[['age_category', 'no_debt_percentage']]
# Plotting the graph using seaborn:

plt.figure(figsize=(10, 6))
ax = sns.barplot(x='age_category', y='no_debt_percentage', data=df_pivot_long)
plt.title("Percentage of debtor clients (grouped by age)")
plt.xlabel("Age Category")
plt.ylabel("%")
plt.xticks(rotation=45)
# Adding percentage values above each column:

for p in ax.patches:
    ax.annotate(f'{p.get_height():.1f}%', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', fontsize=12, color='black', xytext=(0, 5),
                textcoords='offset points')
plt.show()

# Creating a pivot table to study the dependency on the number of children and whether the client was a debtor:

df_pivot = df.pivot_table(index='childrens_category', columns='debt',
values='total_income', aggfunc='count')
# Calculating the total number of clients in each category:

df_pivot['total'] = df_pivot.sum(axis=1)
# Calculating the percentage of debtor clients:

df_pivot['no_debt_percentage'] = (df_pivot[1] / df_pivot['total']) * 100
# Converting the pivot table to long format for use with seaborn:

df_pivot_long = df_pivot.reset_index()
df_pivot_long = df_pivot_long[['childrens_category', 'no_debt_percentage']]
# Plotting the graph using seaborn:

plt.figure(figsize=(10, 6))
ax = sns.barplot(x='childrens_category', y='no_debt_percentage', data=df_pivot_long)
plt.title("Percentage of debtor clients (grouped by number of children)")
plt.xlabel("Number of Children")
plt.ylabel("%")
plt.xticks(rotation=45)
# Adding percentage values above each column:

for p in ax.patches:
    ax.annotate(f'{p.get_height():.1f}%', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', fontsize=12, color='black', xytext=(0, 5),
                textcoords='offset points')
plt.show()

# Creating a pivot table:

df_pivot = df.pivot_table(index='childrens_category', columns='debt',
values='total_income', aggfunc='count')
# Calculating the total number of clients in each category:

df_pivot['total'] = df_pivot.sum(axis=1)
# Calculating the percentage of clients without debts:

df_pivot['no_debt_percentage'] = (df_pivot[0] / df_pivot['total']) * 100
# Converting the pivot table to long format for use with seaborn:

df_pivot_long = df_pivot.reset_index()
df_pivot_long = df_pivot_long[['childrens_category', 'no_debt_percentage']]
# Plotting the graph:

plt.figure(figsize=(10, 6))
ax = sns.barplot(x='childrens_category', y='no_debt_percentage', data=df_pivot_long)
plt.title("Percentage of clients without debts (grouped by number of children)")
plt.xlabel("Number of Children")
plt.ylabel('%')
plt.xticks(rotation=45)
# Adding percentage values above each column:

for p in ax.patches:
    ax.annotate(f'{p.get_height():.1f}%', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', fontsize=10, color='black', xytext=(0, 5),
                textcoords='offset points')
plt.show()

# Creating a function to categorize clients into two categories:
def men_group(row):
    
    family_status = row['family_status']
    category_qcat = row['category_qcat'] 
    gender = row['gender']
    
    
    if (family_status in ["married", "civil partnership"]) and (category_qcat == "Средний доход") and (gender == "M"):
        return 'Семейные мужчины со средним доходом'
    
    if (family_status in ["unmarried", "widow / widower", "divorced"]) and (category_qcat == "Низкий доход") and (gender == "M"):
        return 'Одинокие мужчины с маленьким доходом'
    
    return None  # Returning None if no condition is met

# Creating a new column with categorization by marital status and income:
df['men_category'] = df.apply(men_group, axis=1) 

# Creating a pivot table:
df_pivot = df.pivot_table(index='men_category', columns='debt',
                          values='total_income', aggfunc='count')

# Calculating the total number of clients in each category:
df_pivot['total'] = df_pivot.sum(axis=1)

# Calculating the percentage of debtor clients:
df_pivot['no_debt_percentage'] = (df_pivot[1] / df_pivot['total']) * 100

# Converting the pivot table to long format for use with seaborn:
df_pivot_long = df_pivot.reset_index()
df_pivot_long = df_pivot_long[['men_category', 'no_debt_percentage']]

# Plotting the graph using seaborn:
plt.figure(figsize=(10, 6))
ax = sns.barplot(x='men_category', y='no_debt_percentage', data=df_pivot_long)
plt.title("Percentage of debtor clients")
plt.xlabel("Category")
plt.ylabel("%")
plt.xticks(rotation=45)  

# Adding percentage values above each column:
for p in ax.patches:
    ax.annotate(f'{p.get_height():.1f}%', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', fontsize=10, color='black', xytext=(0, 5),
                textcoords='offset points')
plt.show()

# Explore unique values in the 'purpose' field
df['purpose'].unique()

# Split clients into 2 groups
def find_education_purpose(purpose): 
    # List of education-related purposes:
    education_keywords = [
        "supplementary education", "education", "to become educated", "getting an education",
        "to get a supplementary education", "getting higher education",
        "profile education", "university education", "going to university"
    ]
    
    # Check if the purpose is in the list of education-related purposes:
    if purpose in education_keywords:
        return "Education"
    else:
        return "Other"

# Create a new column with the purpose of the loan:
df['purpose_category'] = df['purpose'].apply(find_education_purpose)

# Investigate the obtained groups by the proportion of clients who defaulted
# Create a pivot table:
df_pivot = df.pivot_table(index='purpose_category', columns='debt',
                          values='total_income', aggfunc='count')

# Calculate the total number of clients in each category:
df_pivot['total'] = df_pivot.sum(axis=1)

# Calculate the percentage of debtor clients:
df_pivot['no_debt_percentage'] = (df_pivot[1] / df_pivot['total']) * 100

# Convert the pivot table to long format for use with seaborn:
df_pivot_long = df_pivot.reset_index()
df_pivot_long = df_pivot_long[['purpose_category', 'no_debt_percentage']]

# Plot the graph using seaborn:
plt.figure(figsize=(10, 6))
ax = sns.barplot(x='purpose_category', y='no_debt_percentage', data=df_pivot_long)
plt.title("Percentage of debtor clients")
plt.xlabel("Loan Purpose")
plt.ylabel("%")
plt.xticks(rotation=45)  

# Add percentage values above each column:
for p in ax.patches:
    ax.annotate(f'{p.get_height():.1f}%', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', fontsize=10, color='black', xytext=(0, 5),
                textcoords='offset points')
plt.show()
