'''
Fetchmaker
In this project, we will help the fictional business FetchMaker determine the key numerical and categorical differences between different dog breeds.
You will get practice choosing and using various types of hypothesis tests.
'''

'''
Congratulations! You’ve just started working at the hottest new tech startup, FetchMaker. FetchMaker’s mission is to match up prospective dog owners with their perfect pet. Data on thousands of adoptable dogs are in FetchMaker’s system, and it’s your job to analyze some of that data.

'''
import numpy as np
import fetchmaker
from scipy.stats import binom_test
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import chi2_contingency

rottweiler_tl = fetchmaker.get_tail_length('rottweiler')
print(np.mean(rottweiler_tl))  # = 4.2361
print(np.std(rottweiler_tl))  # = 2.06475368749

whippet_rescue = fetchmaker.get_is_rescue('whippet')
num_whippet_rescues = np.count_nonzero(whippet_rescue)
num_whippets = np.size(whippet_rescue)

pval = binom_test(num_whippet_rescues, n=num_whippets, p=0.08)
print(pval)  # = 0.581178010624 (not significant)

whippet_w = fetchmaker.get_weight('whippet')
terrier_w = fetchmaker.get_weight('terrier')
pitbull_w = fetchmaker.get_weight('pitbull')
fstat, pval_w = f_oneway(whippet_w, terrier_w, pitbull_w)  # use ANOVA
print(pval_w)  # = 3.27641558827e-17 (significant difference in the sets somewhere)

# Using our data from ANOVA, we create v and l
v = np.concatenate([whippet_w, terrier_w, pitbull_w])
labels = ['whippet'] * len(whippet_w) + ['terrier'] * len(terrier_w) + ['pitbull'] * len(pitbull_w)

tukey_results = pairwise_tukeyhsd(v, labels, 0.05)
print(tukey_results)

'''
Multiple Comparison of Means - Tukey HSD,FWER=0.05
==============================================
 group1  group2 meandiff  lower  upper  reject
----------------------------------------------
pitbull terrier  -13.24  -16.728 -9.752  True 
pitbull whippet  -3.34    -6.828 0.148  False 
terrier whippet   9.9     6.412  13.388  True 
----------------------------------------------
'''

poodle_colors = fetchmaker.get_color('poodle')
shihtzu_colors = fetchmaker.get_color('shihtzu')

color_table = [[np.count_nonzero(poodle_colors == "black"), np.count_nonzero(shihtzu_colors == "black")],
              [np.count_nonzero(poodle_colors == "brown"), np.count_nonzero(shihtzu_colors == "brown")],
              [np.count_nonzero(poodle_colors == "gold"), np.count_nonzero(shihtzu_colors == "gold")],
              [np.count_nonzero(poodle_colors == "grey"), np.count_nonzero(shihtzu_colors == "grey")],
              [np.count_nonzero(poodle_colors == "white"), np.count_nonzero(shihtzu_colors == "white")]]

print(color_table)  # [[17, 10], [13, 36], [8, 6], [52, 41], [10, 7]]

chi2, pval, dof, expected = chi2_contingency(color_table)
print(pval)  # 0.00530240829324  significant difference

# where are the bulldogs????


