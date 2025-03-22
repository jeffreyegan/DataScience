
import pandas as pd
import datetime
#import seaborn as sns
from matplotlib import pyplot as plt


data_url = "https://catalog.data.gov/dataset/lottery-mega-millions-winning-numbers-beginning-2002"
wiki_url = "https://en.wikipedia.org/wiki/Mega_Millions"

csv_file = "Lottery_Mega_Millions_Winning_Numbers__Beginning_2002.csv"

df = pd.read_csv(csv_file)
df["Draw Date"] = pd.to_datetime(df["Draw Date"] )
df = df[df['Draw Date'] > "2017-10-30"]  # October 2017 format and price change - first draw on 10/31/2017
print(df)

print(len(df['Winning Numbers']))

w_1 = []
w_2 = []
w_3 = []
w_4 = []
w_5 = []
m_b = []


for winning_numbers in df['Winning Numbers']:
    w_1.append(int(winning_numbers[0:2]))
    w_2.append(int(winning_numbers[3:5]))
    w_3.append(int(winning_numbers[6:8]))
    w_4.append(int(winning_numbers[9:11]))
    w_5.append(int(winning_numbers[12:14]))

for mega_ball in df['Mega Ball']:
    m_b.append(int(mega_ball))

print(m_b)
'''
sns.set_style("white")
sns.set_palette("pastel")

sns.kdeplot(w_1, shade=True)
sns.kdeplot(w_2, shade=True)
sns.kdeplot(w_3, shade=True)
sns.kdeplot(w_4, shade=True)
sns.kdeplot(w_5, shade=True)
sns.kdeplot(m_b, shade=True)
plt.legend()
plt.show()


sns.violinplot(data=w_1, x="label", y="value")
sns.violinplot(data=w_2, x="label", y="value")
sns.violinplot(data=w_3, x="label", y="value")
sns.violinplot(data=w_4, x="label", y="value")
sns.violinplot(data=w_5, x="label", y="value")
sns.violinplot(data=m_b, x="label", y="value")
'''