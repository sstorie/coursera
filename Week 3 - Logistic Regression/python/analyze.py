import pandas as pd
#import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("ex2data2.txt");

## Pull in original data set
#
df.columns = ["test1", "test2", "pass"]

#groups = df.groupby('pass')

## Now build up the plot
#fig, ax = plt.subplots()
#ax.margins(0.05)
#for name, group in groups:
#    ax.plot(group['test1'], group['test2'], marker='o', linestyle='', ms=12, label = name)

#ax.legend()

#plt.show()


## Map it into a new data set that incorporates the higher order polynomial
#   we want to use
#
df_map = pd.DataFrame(columns=range(1,29))

df_map.set_value(1, 1, 5)


#train_cols = df.columns[[0, 1]]

#print train_cols

#logit = sm.Logit(df["pass"], df[train_cols])

#result = logit.fit()

#print result.summary()

