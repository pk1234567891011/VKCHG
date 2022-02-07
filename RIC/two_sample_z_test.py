import pandas as pd
from statsmodels.stats import weightstats as stests
df = pd.read_csv("blood_pressure.csv")
df[['bp_before','bp_after']].describe()
print(df)
ztest ,pval = stests.ztest(df['bp_before'], x2=df['bp_after'], value=0,alternative='twosided')
print(float(pval))
if pval<0.05:
 print("reject null hypothesis")
else:
 print("accept null hypothesis")
