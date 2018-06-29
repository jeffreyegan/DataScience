'''

Candidate Surveys
In this project, you will use NumPy and binomial distributions to determine the probability of an expected outcome and use Matplotlib to chart the different possibilities.

---

Election Results
You're part of an impartial research group that conducts phone surveys prior to local elections. During this election season, the group conducted a survey to determine how many people would vote for Cynthia Ceballos vs. Justin Kerrigan in the mayoral election.

Now that the election has occurred, your group wants to compare the survey responses to the actual results. Was your survey a good indicator? Let's find out!


'''

import numpy as np
from matplotlib import pyplot as plt

survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

total_ceballos = sum([1 for vote in survey_responses if vote == 'Ceballos'])
print(total_ceballos)

print(len(survey_responses))
percentage_ceballos = float(total_ceballos) / len(survey_responses) *100
print(percentage_ceballos)

possible_surveys = np.random.binomial(10000*0.54, 0.47, size=10000 )/10000.
plt.hist(possible_surveys,bins=20,range=(0,1))
plt.show()

ceballos_loss_surveys = np.mean(possible_surveys < 0.5)
print(ceballos_loss_surveys)

large_survey = np.random.binomial(7000*0.54, 0.47, size=7000)/7000.
ceballos_loss_new = np.mean(large_survey < 0.5)
print(ceballos_loss_new)

# I understand the functions, I just don't understand exactly what the project is requesting.