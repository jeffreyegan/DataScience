'''
Introduction

A huge part of data science involves acquiring raw data and getting it into a form ready for analysis. Some have estimated that data scientists spend 80% of their time cleaning and manipulating data, and only 20% of their time actually analyzing it or building models from it.

When we receive raw data, we have to do a number of things before we're ready to analyze it, possibly including:

    diagnosing the "tidiness" of the data — how much data cleaning we will have to do
    reshaping the data — getting right rows and columns for effective analysis
    combining multiple files
    changing the types of values — how we fix a column where numerical values are stored as strings, for example
    dropping or filling missing values - how we deal with data that is incomplete or missing
    manipulating strings to represent the data better

We will go through the techniques data scientists use to accomplish these goals by looking at some "unclean" datasets and trying to get them into a good, clean state.
Instructions

We have provided an example of data representing exam scores from 1000 students in an online math class.

These DataFrames are hard to work with. They're separated into multiple tables, and the values don't lend themselves well to analysis. Try to think about how you would plot the exam score average against the age of the students in the class. This would not be easy!

In the next exercises, we'll transform this data so that performing a task like that visualization would be simple.

'''
import codecademylib3_seaborn
import pandas as pd

students0 = pd.read_csv("file0.csv")
students1 = pd.read_csv("file1.csv")

print(students0)

'''
Diagnose the Data

We often describe data that is easy to analyze and visualize as "tidy data". What does it mean to have tidy data?

For data to be tidy, it must have:

    Each variable as a separate column
    Each row as a separate observation

For example, we would want to reshape a table like:
Account 	Checkings 	Savings
"12456543" 	8500 	8900
"12283942" 	6410 	8020
"12839485" 	78000 	92000

Into a table that looks more like:
Account 	Account Type 	Amount
"12456543" 	"Checking" 	8500
"12456543" 	"Savings" 	8900
"12283942" 	"Checking" 	6410
"12283942" 	"Savings" 	8020
"12839485" 	"Checking" 	78000
"12839485" 	"Savings" 	920000

The first step of diagnosing whether or not a dataset is tidy is using pandas functions to explore and probe the dataset.

You've seen most of the functions we often use to diagnose a dataset for cleaning. Some of the most useful ones are:

    .head() — display the first 5 rows of the table
    .info() — display a summary of the table
    .describe() — display the summary statistics of the table
    .columns — display the column names of the table
    .value_counts() — display the distinct values for a column

'''
import codecademylib3_seaborn
import pandas as pd

df1 = pd.read_csv("df1.csv")
df2 = pd.read_csv("df2.csv")

print(df1.head())
print(df2.head())

clean = 2

'''
Dealing with Multiple Files  - GLOB 

Often, you have the same data separated out into multiple files.

Let's say that we have a ton of files following the filename structure: 'file1.csv', 'file2.csv', 'file3.csv', and so on. The power of pandas is mainly in being able to manipulate large amounts of structured data, so we want to be able to get all of the relevant information into one table so that we can analyze the aggregate data.

We can combine the use of glob, a Python library for working with files, with pandas to organize this data better. glob can open multiple files by using regex matching to get the filenames:

import glob

files = glob.glob("file*.csv")

df_list = []
for filename in files:
  data = pd.read_csv(filename)
  df_list.append(data)

df = pd.concat(df_list)

print(files)

This code goes through any file that starts with 'file' and has an extension of .csv. It opens each file, reads the data into a DataFrame, and then concatenates all of those DataFrames together.
Instructions
1.

We have 10 different files containing 100 students each. These files follow the naming structure:

    exams0.csv
    exams1.csv
    ... up to exams9.csv

We are going to import each file using pandas, and combine all of the entries into one DataFrame.

First, create a variable called student_files and set it equal to the glob() of all of the csv files we want to import.
2.

Create an empty list called df_list that will store all of the DataFrames we make from the files exams0.csv through exams9.csv.
3.

Loop through the filenames in student_files, and create a DataFrame from each file. Append this DataFrame to df_list.
'''
import codecademylib3_seaborn
import pandas as pd
import glob

student_files = glob.glob("exams*.csv")
df_list = []
for filename in student_files:
    data = pd.read_csv(filename)
    df_list.append(data)

students = pd.concat(df_list)

print(students)
print(len(students))

'''
Reshaping your Data

Since we want

    Each variable as a separate column
    Each row as a separate observation

We would want to reshape a table like:
Account 	Checking 	Savings
"12456543" 	8500 	8900
"12283942" 	6410 	8020
"12839485" 	78000 	92000

Into a table that looks more like:
Account 	Account Type 	Amount
"12456543" 	"Checking" 	8500
"12456543" 	"Savings" 	8900
"12283942" 	"Checking" 	6410
"12283942" 	"Savings" 	8020
"12839485" 	"Checking" 	78000
"12839485" 	"Savings" 	920000

We can use pd.melt() to do this transformation. .melt() takes in a DataFrame, and the columns to unpack:

pd.melt(frame=df, id_vars='name', value_vars=['Checking','Savings'], value_name="Amount", var_name="Account Type")

The parameters you provide are:

    frame: the DataFrame you want to melt
    id_vars: the column(s) of the old DataFrame to preserve
    value_vars: the column(s) of the old DataFrame that you want to turn into variables
    value_name: what to call the column of the new DataFrame that stores the values
    var_name: what to call the column of the new DataFrame that stores the variables

The default names may work in certain situations, but it's best to always have data that is self-explanatory. Thus, we often use .columns() to rename the columns after melting:

df.columns(["Account", "Account Type", "Amount"])


1.

Print out the columns of students.
2.

There is a column for the scores on the fractions exam, and a column for the scores on the probabilities exam.

We want to make each row an observation, so we want to transform this table to look like:
full_name 	exam 	score 	gender_age 	grade
"First Student" 	"Fractions" 	score% 	... 	...
"First Student" 	"Probabilities" 	score% 	... 	...
"Second Student" 	"Fractions" 	score% 	... 	...
"Second Student" 	"Probabilities" 	score% 	... 	...
... 	... 	...

Use pd.melt() to create a new table (still called students) that follows this structure.
3.

Print the .head() and the .columns of students.

Also, print out the .value_counts() of the column exam.
'''

import codecademylib3_seaborn
import pandas as pd
from students import students

print(students.columns)  # Index(['full_name', 'gender_age', 'fractions', 'probability', 'grade'], dtype='object')

students = pd.melt(frame=students, id_vars=['full_name', 'gender_age', 'grade'], value_vars=['fractions', 'probability'], value_name='score', var_name='exam')

print(students.head())
print(students.columns)
print(students.exam.value_counts())

'''
Index(['full_name', 'gender_age', 'fractions', 'probability', 'grade'], dtype='object')
           full_name gender_age       grade       exam score
0     Moses Kirckman        M14  11th grade  fractions   69%
1    Timofei Strowan        M18  11th grade  fractions   63%
2       Silvain Poll        M18   9th grade  fractions   69%
3     Lezley Pinxton        M18  11th grade  fractions   NaN
4  Bernadene Saunper        F17  11th grade  fractions   72%
Index(['full_name', 'gender_age', 'grade', 'exam', 'score'], dtype='object')
fractions      1000
probability    1000'''






'''
Dealing with Duplicates

Often we see duplicated rows of data in the DataFrames we are working with. This could happen due to errors in data collection or in saving and loading the data.

To check for duplicates, we can use the pandas function .duplicated(), which will return a Series telling us which rows are duplicate rows.

Let's say we have a DataFrame fruits that represents this table:
item 	price 	calories
"banana" 	"$1" 	105
"apple" 	"$0.75" 	95
"apple" 	"$0.75" 	95
"peach" 	"$3" 	55
"peach" 	"$4" 	55
"clementine" 	"$2.5" 	35

If we call fruits.duplicated(), we would get the following table:
id 	value
0 	False
1 	False
2 	True
3 	False
4 	False
5 	False

We can see that row 2, which represents an "apple" with price "$0.75" and 95 calories, is a duplicate row. Every value in this row is the same as in another row.

We can use the pandas .drop_duplicates() function to remove all rows that are duplicates of another row.

If we call fruits.drop_duplicates(), we would get the table:
item 	price 	calories
"banana" 	"$1" 	105
"apple" 	"$0.75" 	95
"peach" 	"$3" 	55
"peach" 	"$4" 	55
"clementine" 	"$2.5" 	35

The "apple" row was deleted because it was exactly the same as another row. But the two "peach" rows remain because there is a difference in the price column.

If we wanted to remove every row with a duplicate value in the item column, we could specify a subset:

fruits = fruits.drop_duplicates(subset=['item'])

By default, this keeps the first occurrence of the duplicate:
item 	price 	calories
"banana" 	"$1" 	105
"apple" 	"$0.75" 	95
"peach" 	"$3" 	55
"clementine" 	"$2.5" 	35


Make sure that the columns you drop duplicates from are specifically the ones where duplicates don't belong. You wouldn't want to drop duplicates with the price column as a subset, for example, because it's okay if multiple items cost the same amount!
1.

It seems like in the data collection process, some rows may have been recorded twice. Use the .duplicated() function on the students DataFrame to make a Series object called duplicates.
2.

Print out the .value_counts() of the duplicates Series to see how many rows are exact duplicates.
3.

Update the value of students to be the students table with the duplicates dropped.
4.

Use the .duplicated() function again to make a Series object called duplicates after dropping the duplicates. Print out the value counts again. Are there any Trues left?
'''
import codecademylib3_seaborn
import pandas as pd
from students import students

duplicates = students.duplicated()
print(duplicates.value_counts())
students = students.drop_duplicates()
duplicates = students.duplicated()
print(duplicates.value_counts())


'''
Splitting by Index

In trying to get clean data, we want to make sure each column represents one type of measurement. Often, multiple measurements are recorded in the same column, and we want to separate these out so that we can do individual analysis on each variable.

Let's say we have a column "birthday" with data formatted in MMDDYYYY format. In other words, "11011993" represents a birthday of November 1, 1993. We want to split this data into day, month, and year so that we can use these columns as separate features.

In this case, we know the exact structure of these strings. The first two characters will always correspond to the month, the second two to the day, and the rest of the string will always correspond to year. We can easily break the data into three separate columns by splitting the strings using .str:

# Create the 'month' column
df['month'] = df.birthday.str[0:2]

# Create the 'day' column
df['day'] = df.birthday.str[2:4]

# Create the 'year' column
df['year'] = df.birthday.str[4:]

The first command takes the first two characters of each value in the birthday column and puts it into a month column. The second command takes the second two characters of each value in the birthday column and puts it into a day column. The third command takes the rest of each value in the birthday column and puts it into a year column.

This would transform a table like:
id 	birthday
1011 	"12241989"
1112 	"10311966"
1113 	"01052011"
into a table like:
id 	birthday 	month 	day 	year
1011 	"12241989" 	"12" 	"24" 	"1989"
1112 	"10311966" 	"10" 	"31" 	"1966"
1113 	"01052011" 	"01" 	"05" 	"2011"

We will practice changing string columns into numerical columns (like converting "10" to 10) in a future exercise.
1.

Print out the columns of the students DataFrame.
2.

The column gender_age sounds like it contains both gender and age!

Print out the .head() of the column to see what kind of data it contains.
3.

It looks like the first character of the values in gender_age contains the gender, while the rest of the string contains the age. Let's separate out the gender data into a new column called gender.
4.

Now, separate out the age data into a new column called age.
5.

Good job! Let's print the .head() of students to see how the DataFrame looks after our creation of new columns.
6.

Now, we don't need that gender_age column anymore.

Let's set the students DataFrame to be the students DataFrame with all columns except gender_age.
'''
import codecademylib3_seaborn
import pandas as pd
from students import students

print(students.columns)
print(students.head())
students['gender']=students['gender_age'].str[0]
students['age']=students['gender_age'].str[1:]
print(students.head())

students = students[['full_name','gender','age','grade','exam','score']]
print(students.head())

'''
Splitting by Character

Let's say we have a column called "type" with data entries in the format "admin_US" or "user_Kenya". Just like we saw before, this column actually contains two types of data. One seems to be the user type (with values like "admin" or "user") and one seems to be the country this user is in (with values like "US" or "Kenya").

We can no longer just split along the first 4 characters because admin and user are of different lengths. Instead, we know that we want to split along the "_". Using that, we can split this column into two separate, cleaner columns:

# Create the 'str_split' column
df['str_split'] = df.type.str.split('_')

# Create the 'usertype' column
df['usertype'] = df.str_split.str.get(0)

# Create the 'country' column
df['country'] = df.str_split.str.get(1)

This would transform a table like:
id 	type
1011 	"user_Kenya"
1112 	"admin_US"
1113 	"moderator_UK"
into a table like:
id 	type 	country 	usertype
1011 	"user_Kenya" 	"Kenya" 	"user"
1112 	"admin_US" 	"US" 	"admin"
1113 	"moderator_UK" 	"UK" 	"moderator"
1.

The students' names are stored in a column called full_name.

We want to separate this data out into two new columns, first_name and last_name.

First, let's create a Series object called name_split that splits the full_name by the " " character.
2.

Now, let's create a column called first_name that takes the first item in name_split.
3.

Finally, let's create a column called last_name that takes the second item in name_split.
4.

Print out the .head() of students to see how the DataFrame has changed.
'''
import codecademylib3_seaborn
import pandas as pd
from students import students

print(students.head())
students['name_split'] = students['full_name'].str.split(" ")
students['first_name'] = students['name_split'].str.get(0)
students['last_name'] = students['name_split'].str.get(1)
print(students.head())


'''
Looking at Types

Each column of a DataFrame can hold items of the same data type or dtype. The dtypes that pandas uses are: float, int, bool, datetime, timedelta, category and object. Often, we want to convert between types so that we can do better analysis. If a numerical category like "num_users" is stored as a Series of objects instead of ints, for example, it makes it more difficult to do something like make a line graph of users over time.

To see the types of each column of a DataFrame, we can use:

print(df.dtypes)

For a DataFrame like this:
item 	price 	calories
"banana" 	"$1" 	105
"apple" 	"$0.75" 	95
"peach" 	"$3" 	55
"clementine" 	"$2.5" 	35

the .dtypes attribute would be:

item        object
price       object
calories     int64
dtype: object

We can see that the dtype of the dtypes attribute itself is an object! It is a Series object, which you have already worked with. Series objects compose all DataFrames.

We can see that the price column is made up of objects, which will probably make our analysis of price more difficult. We'll look at how to convert columns into numeric values in the next few exercises.
Instructions
1.

Let's inspect the dtypes in the students table.

Print out the .dtypes attribute.
2.

If we wanted to make a scatterplot of age vs average exam score, would we be able to do it with this type of data?

Try to print out the mean of the score column of students.
'''
import codecademylib3_seaborn
import pandas as pd
from students import students

print(students.head())
print(students.dtypes)
print(students['score'].mean())  # broken


'''
String Parsing

Sometimes we need to modify strings in our DataFrames to help us transform them into more meaningful metrics. For example, in our fruits table from before:
item 	price 	calories
"banana" 	"$1" 	105
"apple" 	"$0.75" 	95
"peach" 	"$3" 	55
"peach" 	"$4" 	55
"clementine" 	"$2.5" 	35

We can see that the 'price' column is actually composed of strings representing dollar amounts. This column could be much better represented in floats, so that we could take the mean, calculate other aggregate statistics, or compare different fruits to one another in terms of price.

First, we can use what we know of regex to get rid of all of the dollar signs:

fruit.price = fruit['price'].replace('[\$,]', '', regex=True)

Then, we can use the pandas function .to_numeric() to convert strings containing numerical values to integers or floats:

fruit.price = pd.to_numeric(fruit.price)

Now, we have a DataFrame that looks like:
item 	price 	calories
"banana" 	1 	105
"apple" 	0.75 	95
"peach" 	3 	55
"peach" 	4 	55
"clementine" 	2.5 	35
1.

We saw in the last exercise that finding the mean of the score column is hard to do when the data is stored as Objects and not numbers.

Use regex to take out the % signs in the score column.
2.

Convert the score column to a numerical type using the pd.to_numeric() function.
'''
import codecademylib3_seaborn
import pandas as pd
from students import students

students.score = students['score'].replace('[\%,]', '', regex=True)
students.score = pd.to_numeric(students['score'])

print(students.score[0])

'''
More String Parsing

Sometimes we want to do analysis on numbers that are hidden within string values. We can use regex to extract this numerical data from the strings they are trapped in. Suppose we had this DataFrame df representing a workout regimen:
date 	exerciseDescription
10/18/2018 	"lunges - 30 reps"
10/18/2018 	"squats - 20 reps"
10/18/2018 	"deadlifts - 25 reps"
10/18/2018 	"jumping jacks - 30 reps"
10/19/2018 	"lunges - 40 reps"
10/19/2018 	"chest flyes - 15 reps"
... 	...

It would be helpful to separate out data like "30 lunges" into 2 columns with the number of reps, "30", and the type of exercise, "lunges". Then, we could compare the increase in the number of lunges done over time, for example.

To extract the numbers from the string we can use pandas' .str.split() function:

split_df = df['exerciseDescription'].str.split('(\d+)', expand=True)

which would result in this DataFrame split_df:
	0 	1 	2
0 	"lunges - " 	"30" 	"reps"
1 	"squats - " 	"20" 	"reps"
2 	"deadlifts - " 	"25" 	"reps"
3 	"jumping jacks - " 	"30" 	"reps"
4 	"lunges - " 	"40" 	"reps"
5 	"chest flyes - " 	"15" 	"reps"
... 	... 	... 	...

Then, we can assign columns from this DataFrame to the original df:

df.reps = pd.to_numeric(split_df[1])
df.exercise = split_df[2].replace('[\- ]', '', regex=True)

Now, our df looks like this:
date 	exerciseDescription 	reps 	exercise
10/18/2018 	"lunges - 30 reps" 	30 	"lunges"
10/18/2018 	"squats - 20 reps" 	20 	"squats"
10/18/2018 	"deadlifts - 25 reps" 	25 	"deadlifts"
10/18/2018 	"jumping jacks - 30 reps" 	30 	"jumping jacks"
10/19/2018 	"lunges - 40 reps" 	40 	"lunges"
10/19/2018 	"chest flyes - 15 reps" 	15 	"chest flyes"
... 	... 	... 	...
1.

Print out the first five rows of the grade column.
2.

Each value in grade looks like "9th grade", "10th grade", "11th grade", or "12th grade".

We want to pare that down to just having the numerical grade. Maybe we want to do linear regression on this data, which would require numerical inputs.

Use regex to extract the number from each string in grade and store those values back into the grade column.
3.

Print the dtypes of the students table.
4.

Convert the grade column to be numerical values instead of objects.
5.

Calculate the mean of grade, store it in a variable called avg_grade, and then print it out!

We could not have done this with strings like "9th grade" or "10th grade".
'''
import codecademylib3_seaborn
import pandas as pd
from students import students

print(students.grade.head())

students.grade = students.grade.str.split('(\d+)', expand=True)[1]

print(students.dtypes)

students.grade = pd.to_numeric(students.grade)
avg_grade = students.grade.mean()

print(avg_grade)


'''
Missing Values

We often have data with missing elements, as a result of a problem with the data collection process or errors in the way the data was stored. The missing elements normally show up as NaN (or Not a Number) values:
day 	bill 	tip 	num_guests
"Mon" 	10.1 	1 	1
"Mon" 	20.75 	5.5 	2
"Tue" 	19.95 	5.5 	NaN
"Wed" 	44.10 	15 	3
"Wed" 	NaN 	1 	1

The num_guests value for the 3rd row is missing, and the bill value for the 5th row is missing. Some calculations we do will just skip the NaN values, but some calculations or visualizations we try to perform will break when a NaN is encountered.

Most of the time, we use one of two methods to deal with missing values.
Method 1: drop all of the rows with a missing value

We can use .dropna() to do this:

bill_df = bill_df.dropna()

This command will result in the DataFrame without the incomplete rows:
day 	bill 	tip 	num_guests
"Mon" 	10.1 	1 	1
"Mon" 	20.75 	5.5 	2
"Wed" 	44.10 	15 	3

If we wanted to remove every row with a NaN value in the num_guests column only, we could specify a subset:

bill_df = bill_df.dropna(subset=['num_guests'])

Method 2: fill the missing values with the mean of the column, or with some other aggregate value.

We can use .fillna() to do this:

bill_df = bill_df.fillna(value={"bill":bill_df.bill.mean(), "num_guests":bill_df.num_guests.mean()})

This command will result in the DataFrame with the respective mean of the column in the place of the original NaNs:
day 	bill 	tip 	num_guests
"Mon" 	10.1 	1 	1
"Mon" 	20.75 	5.5 	2
"Tue" 	19.95 	5.5 	1.75
"Wed" 	44.10 	15 	3
"Wed" 	23.725 	1 	1


1.

Get the mean of the score column. Store it in score_mean and print it out.
2.

We will assume that everyone who doesn't have a score for an exam missed the test. We want to replace all nans with a score of 0. Let's do this with the score column.

Fill all of the nans in students['score'] with 0.
3.

Get the mean of the score column again. Store it in score_mean_2 and print it out.
'''
import codecademylib3_seaborn
import pandas as pd
from students import students

print(students)

score_mean = students.score.mean()
print(score_mean)

students = students.fillna(value={"score":0})

score_mean_2 = students.score.mean()
print(score_mean_2)


'''
Review

Great! We have looked at a number of different methods we may use to get data into the format we want for analysis.

Specifically, we have covered:

    diagnosing the "tidiness" of the data
    reshaping the data
    combining multiple files
    changing the types of values
    dropping or filling missing values - how we deal with data that is incomplete or missing
    manipulating strings to represent the data better

You can use these methods to transform your datasets to be clean and easy to work with!
'''
