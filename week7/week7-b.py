
import numpy as np
import pandas as pd

df = pd.read_csv("Telecom_customer churn.csv")
df = df.select_dtypes(exclude = ['object'])
target = 'churn'


for c in df:
    #! df['TEMP'] = np.log(df[c] + 1)
    df['TEMP'] = np.power(df[c], 0.2)


    oz = df[c].corr(df[target])
    farkli = df['TEMP'].corr(df[target])

    if abs(farkli) > abs(oz) and \
        abs(farkli) > abs(oz) * 1.15 and \
        abs(farkli) - abs(oz) > 0.02:
        print(c, oz, farkli, farkli / oz, abs(farkli) - abs(oz))
