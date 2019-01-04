'''
Cleaning US Census Data

You just got hired as a Data Analyst at the Census Bureau, which collects census data and creates interesting visualizations and insights from it.

The person who had your job before you left you all the data they had for the most recent census. It is in multiple csv files. They didn't use pandas, they would just look through these csv files manually whenever they wanted to find something. Sometimes they would copy and paste certain numbers into Excel to make charts.

The thought of it makes you shiver. This is not scalable or repeatable.

Your boss wants you to make some scatterplots and histograms by the end of the day. Can you get this data into pandas and into reasonable shape so that you can make these histograms?
Mark the tasks as complete by checking them off
Inspect the Data!
1.

The first visualization your boss wants you to make is a scatterplot that shows average income in a state vs proportion of women in that state.

Open some of the census csv files in the navigator. How are they named? What kind of information do they hold? Will they help us make this graph?
2.

It will be easier to inspect this data once we have it in a DataFrame. You can't even call .head() on these csvs! How are you supposed to read them?

Using glob, loop through the census files available and load them into DataFrames. Then, concatenate all of those DataFrames together into one DataFrame, called something like us_census.
3.

Look at the .columns and the .dtypes of the us_census DataFrame. Are those datatypes going to hinder you as you try to make histograms?
4.

Look at the .head() of the DataFrame so that you can understand why some of these dtypes are objects instead of integers or floats.

Start to make a plan for how to convert these columns into the right types for manipulation.
Regex to the Rescue
5.

Use regex to turn the Income column into a format that is ready for conversion into a numerical type.
6.

Look at the PopulationGender column. We are going to want to separate this into two columns, the Men column, and the Women column.

Split the column into those two new columns using str.split and separating out those results.
7.

Convert both of the columns into numerical datatypes.

There is still an M or an F character in each entry! We should remove those before we convert.
8.

Now you should have the columns you need to make the graph and make sure your boss does not slam a ruler angrily on your desk because you've wasted your whole day cleaning your data with no results to show!

Use matplotlib to make a scatterplot!

plt.scatter(the_women_column, the_income_column)

Remember to call plt.show() to see the graph!
9.

Did you get an error? These monstrous csv files probably have nan values in them! Print out your column with the number of women per state to see.

We can fill in those nans by using pandas' .fillna() function.

You have the TotalPop per state, and you have the Men per state. As an estimate for the nan values in the Women column, you could use the TotalPop of that state minus the Men for that state.

Print out the Women column after filling the nan values to see if it worked!
10.

We forgot to check for duplicates! Use .duplicated() on your census DataFrame to see if we have duplicate rows in there.
11.

Drop those duplicates using the .drop_duplicates() function.
12.

Make the scatterplot again. Now, it should be perfect! Your job is secure, for now.
Histograms of Races
13.

Now, your boss wants you to make a bunch of histograms out of the race data that you have. Look at the .columns again to see what the race categories are.
14.

Try to make a histogram for each one!

You will have to get the columns into numerical format, and those percentage signs will have to go.

Don't forget to fill the nan values with something that makes sense! You probably dropped the duplicate rows when making your last graph, but it couldn't hurt to check for duplicates again.
Get Creative
15.

Phew. You've definitely impressed your boss on your first day of work.

But is there a way you really convey the power of pandas and Python over the drudgery of csv and Excel?

Try to make some more interesting graphs to show your boss, and the world! You may need to clean the data even more to do it, or the cleaning you have already done may give you the ease of manipulation you've been searching for.

'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplt
import codecademylib3_seaborn
import glob

states_files = glob.glob("states*.csv")
df_list = []
for filename in states_files:
  data = pd.read_csv(filename)
  df_list.append(data)
us_census = pd.concat(df_list)

#us_census = us_census.drop_duplicates()
#print(us_census)
#print(len(us_census))
print(us_census.columns)  # Index(['Unnamed: 0', 'State', 'TotalPop', 'Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific', 'Income', 'GenderPop'],

# Drop Useless Column that prevents identification of duplicates
us_census = us_census.drop(['Unnamed: 0'], axis=1)

# Drop Duplicated States Data
us_census = us_census.drop_duplicates()

# Clean Income Data
us_census.Income = us_census['Income'].replace('[\$,]', '', regex=True)
us_census['Income'] = us_census['Income'].astype(float)

# Clean Gender Data
us_census['gender_split'] = us_census['GenderPop'].str.split("_")
us_census['Men'] = us_census['gender_split'].str.get(0)
us_census['Men'] = us_census['Men'].str[:-1]
us_census['Women'] = us_census['gender_split'].str.get(1)
us_census['Women'] = us_census['Women'].str[:-1]
us_census = us_census.drop(['gender_split'], axis=1)
us_census = us_census.drop(['GenderPop'], axis=1)
us_census.Women = us_census['Men'].replace(r'', np.nan, regex=True)
us_census.Women = us_census['Women'].replace(r'', np.nan, regex=True)
us_census['Men'] = us_census['Men'].astype(float)
us_census['Women'] = us_census['Women'].astype(float)

us_census['Women'] = us_census['Women'].fillna(us_census['TotalPop']-us_census['Men'])

print(us_census.head())


f, ax1 =  pyplt.subplots()
pyplt.scatter(100.0*us_census['Women']/us_census['TotalPop'], us_census['Income'], alpha=0.8)
pyplt.xlabel('Percent Population of Women in Each State')
pyplt.ylabel('Income')
pyplt.show()

us_census['Hispanic'] = us_census['Hispanic'].fillna(0.0)
us_census['White'] = us_census['White'].fillna(0.0)
us_census['Black'] = us_census['Black'].fillna(0.0)
us_census['Native'] = us_census['Native'].fillna(0.0)
us_census['Asian'] = us_census['Asian'].fillna(0.0)
us_census['Pacific'] = us_census['Pacific'].fillna(0.0)


us_census.Hispanic = us_census['Hispanic'].replace('[\%,]', '', regex=True)
us_census.White = us_census['White'].replace('[\%,]', '', regex=True)
us_census.Black = us_census['Black'].replace('[\%,]', '', regex=True)
us_census.Native = us_census['Native'].replace('[\%,]', '', regex=True)
us_census.Asian = us_census['Asian'].replace('[\%,]', '', regex=True)
us_census.Pacific = us_census['Pacific'].replace('[\%,]', '', regex=True)

us_census['Hispanic'] = us_census['Hispanic'].astype(float)
us_census['White'] = us_census['White'].astype(float)
us_census['Black'] = us_census['Black'].astype(float)
us_census['Native'] = us_census['Native'].astype(float)
us_census['Asian'] = us_census['Asian'].astype(float)
us_census['Pacific'] = us_census['Pacific'].astype(float)

f, ax2 =  pyplt.subplots()
pyplt.hist(us_census['Hispanic'], bins=100)
pyplt.title('Hispanic Population')
pyplt.show()
f, ax3 =  pyplt.subplots()
pyplt.hist(us_census['White'], bins=100)
pyplt.title('White Population')
pyplt.show()
f, ax4 =  pyplt.subplots()
pyplt.hist(us_census['Black'], bins=100)
pyplt.title('Black Population')
pyplt.show()
f, ax5 =  pyplt.subplots()
pyplt.hist(us_census['Native'], bins=100)
pyplt.title('Native Population')
pyplt.show()
f, ax6 =  pyplt.subplots()
pyplt.hist(us_census['Asian'], bins=100)
pyplt.title('Asian Population')
pyplt.show()
f, ax7 =  pyplt.subplots()
pyplt.hist(us_census['Pacific'], bins=100)
pyplt.title('Pacific Population')
pyplt.show()