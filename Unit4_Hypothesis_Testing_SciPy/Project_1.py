'''
Familiar: A Study In Data Analysis
Welcome to Familiar, a startup in the new market of blood transfusion! You've joined the team because you appreciate the flexible hours and extremely intelligent team, but the overeager doorman welcoming you into the office is a nice way to start your workday (well, work-evening).

Familiar has fallen into some tough times lately, so you're hoping to help them make some insights about their product and help move the needle (so to speak).
'''

import familiar
from scipy.stats import ttest_1samp
from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency
import numpy as np

vein_pack_lifespans = familiar.lifespans(package='vein')
print(vein_pack_lifespans)

tstat, vein_pack_test = ttest_1samp(vein_pack_lifespans, 71)

print(vein_pack_test)  # 2.74631179866e-10  Significant!!

if vein_pack_test < 0.05:
    print("The Vein Pack Is Proven To Make You Live Longer!")
else:
    print("The Vein Pack Is Probably Good For You Somehow!")

artery_pack_lifespans = familiar.lifespans(package='artery')
print(artery_pack_lifespans)

tstat, package_comparison_results = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)
print(package_comparison_results)

if package_comparison_results < 0.05:
    print("the Artery Package guarantees even stronger results!")
else:
    print("the Artery Package is also a great product!")

    # Contingency table
#            Low    |   Normal  | High
# ----+------------------+------------
# Vein   | 140       |  40     |   20
# Artery | 29       |  87      |   29

## contingency table from familiar has it pivoted

iron_contingency_table = familiar.iron_counts_for_package()
print(iron_contingency_table)

chi2, iron_pvalue, dof, expected = chi2_contingency(iron_contingency_table)
print(iron_pvalue)

if iron_pvalue < 0.05:
    print("The Artery Package Is Proven To Make You Healthier!")
else:
    print("While We Can't Say The Artery Package Will Help You, I Bet It's Nice!")
