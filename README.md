You have data on the clients of the bank "Scrooge" who are planning to take out a loan. You need to find out which of the available data affects the timely repayment of the loan and in what way.

The research will help create a credit scoring model—a system for assessing a potential borrower's ability to repay their loan.

For each client, there is information about their marital status, education, income, and other data. You will need to prepare the data for analysis and investigate it, answering questions along the way.

1.1 Data Description

    children — number of children in the family;
    days_employed — how many days the client has been employed;
    dob_years — age of the client;
    education — level of education of the client;
    education_id — education level identifier of the client;
    family_status — marital status of the client;
    family_status_id — marital status identifier of the client;
    gender — gender of the client;
    income_type — type of income of the client;
    debt — whether the client has ever been overdue on a loan payment;
    total_income — monthly income;
    purpose — reason for taking out the loan.

 
Step 1: Open the data file and examine the general information

    Load the data from the csv file into a DataFrame using the pandas library.
    Examine the general information about the resulting DataFrame.
    Make preliminary conclusions about the data.
    Consider the data types in each column.

Step 2: Perform data preprocessing

    Identify and examine missing values in the columns:

        Determine which columns have missing values.

        Fill in missing values where possible. For example, if the number of days worked is not specified, then the person likely has no work experience. Such gaps can be replaced with the number 0. If a logical replacement is not possible, leave the gaps. Missing values are also an important signal to consider. Remember that it is not necessary to handle all the gaps. Make a decision based on three options:
            delete rows with gaps;
            replace missing values;
            leave gaps as they are.

        In a markdown cell, indicate the reasons that could have led to missing data.

    Study the unique values in the columns with the client's education level and gender. Eliminate implicit duplicates and incorrect values. For example, for the "education" column, the values "secondary education," "Secondary Education," and "SECONDARY EDUCATION" are the same.

    Check for duplicates. Examine duplicate data if present and decide whether to delete or keep them.

Step 3: Examine the total_income, dob_years, and children columns for outliers and anomalous values:

    Use histograms and/or box plots for these columns.
    Describe outliers (if any) in any way you deem appropriate.
    Handle rows with outlier values: delete them, replace them, or simply do not use them in the analysis. Explain your choice.
    Draw conclusions and answer the question: what percentage of rows did you lose during preprocessing?

Step 4: Add new columns to the table:

    Divide clients into 5 categories by income level:

    No income: people without jobs and with zero income.
    Very low income: people earning below the 14th percentile of the overall income distribution.
    Low income: people earning between the 14th and 34th percentiles of the overall income distribution.
    Middle income: people earning between the 34th and 78th percentiles of the overall income distribution.
    High income: people earning more than the 78th percentile of the overall income distribution.
    Save the client's category in a separate column "income_category".

    Divide clients into two categories by age: under 40 years old and over 40. Save the result in the "age_category" column.
    Divide clients into several categories by the number of children: no children, from one to two, from three or more. Save the result in the "childrens_category" column.

Step 5: Conduct exploratory data analysis:

Study factors that may affect timely loan repayment:

    Income level,
    Education,
    Age,
    Number of children.

Show the distribution of these factors. Does the distribution differ between debtors? Using the columns created in the previous step, create a pivot table for each factor, showing how often debtors occur in each client group. Choose appropriate visualization and compare the groups of those who returned the loan and those who did not.
Step 6: Write a general conclusion

Describe the results obtained and summarize the final conclusion of the study.
Step 7: Conduct additional research:

Study the reasons for taking out a loan. Is it true that people who took out a loan for education were the least likely to be debtors?
