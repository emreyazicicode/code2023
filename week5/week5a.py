
import pandas as pd

#: Read the csv file and assign to to a "df" dataframe (note, only read 10000 rows)
df = pd.read_csv("Telecom_customer churn.csv", nrows = 10000)

#* Dataframe is like a table

"""
df = {
    'rev_Mean': [23.9975, 57.4925, ....],
    'mou_Mean': [219.25, 482.75, ....]
}
"""

print(df)
print(df.shape[0]) # How many rows
print(df.shape[1]) # How many columns
df.info()

"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10000 entries, 0 to 9999
Data columns (total 100 columns):
 #   Column            Non-Null Count  Dtype  
---  ------            --------------  -----  
 0   rev_Mean          9979 non-null   float64
 1   mou_Mean          9979 non-null   float64
 2   totmrc_Mean       9979 non-null   float64
 3   da_Mean           9979 non-null   float64
 4   ovrmou_Mean       9979 non-null   float64
 47  callwait_Mean     10000 non-null  float64
 48  churn             10000 non-null  int64  
 49  months            10000 non-null  int64  
 50  uniqsubs          10000 non-null  int64  
 51  actvsubs          10000 non-null  int64  
 52  new_cell          10000 non-null  object 
 53  crclscod          10000 non-null  object 
 54  asl_flag          10000 non-null  object 
 55  totcalls          10000 non-null  int64  
 56  totmou            10000 non-null  float64
 57  totrev            10000 non-null  float64
 58  adjrev            10000 non-null  float64
 59  adjmou            10000 non-null  float64
 60  adjqty            10000 non-null  int64  
 61  avgrev            10000 non-null  float64
 63  avgqty            10000 non-null  float64
 64  avg3mou           10000 non-null  int64  
 65  avg3qty           10000 non-null  int64  
 66  avg3rev           10000 non-null  int64  
 67  avg6mou           9986 non-null   float64
 68  avg6qty           9986 non-null   float64
 69  avg6rev           9986 non-null   float64
 70  prizm_social_one  9395 non-null   object 
 71  area              9995 non-null   object 
 72  dualband          10000 non-null  object 
 73  refurb_new        10000 non-null  object 
 74  hnd_price         9905 non-null   float64
 75  phones            10000 non-null  int64  
 76  models            10000 non-null  int64  
 77  hnd_webcap        7662 non-null   object 
 78  truck             9845 non-null   float64
 79  rv                9845 non-null   float64
 80  ownrent           7752 non-null   object 
 81  lor               8081 non-null   float64
 82  dwlltype          7872 non-null   object 
 83  marital           9845 non-null   object 
 84  adults            8562 non-null   float64
 85  infobase          8632 non-null   object 
 86  income            8401 non-null   float64
 87  numbcars          6030 non-null   float64
 88  HHstatin          7280 non-null   object 
 89  dwllsize          7301 non-null   object 
 90  forgntvl          9845 non-null   float64
 91  ethnic            9845 non-null   object 
 92  kid0_2            9845 non-null   object 
 93  kid3_5            9845 non-null   object 
 94  kid6_10           9845 non-null   object 
 95  kid11_15          9845 non-null   object 
 96  kid16_17          9845 non-null   object 
 97  creditcd          9845 non-null   object 
 98  eqpdays           10000 non-null  int64  
 99  Customer_ID       10000 non-null  int64  
dtypes: float64(66), int64(13), object(21)
memory usage: 7.6+ MB
"""

# float64 (float32) ==> size of the float (3.45)
# int64   (int32)   ==> size of the int   (3)
# REST, object      ==> mostly used for "TEXT" and "CATEGORIC" (address, YES/NO...)

print("====================================================")
print(df.dtypes)
print(dict(df.dtypes))
print(df.dtypes['rev_Mean'], type(df.dtypes['rev_Mean']))
print("====================================================")
print(list(df.columns), type(list(df.columns)))
print("len", len(df), df.shape[0])
# There are many duplicates in pandas
# Pandas is a very powerful transformaiton, manipulation ENGINE

# Loop for each column
for c in df:  # df.columns
    print(c)

for c in df.columns:
    dtype = str(df.dtypes[c])
    if dtype in ['int64', 'float64']:
        print(c, dtype, df[c].mean(), df[c].kurt(), df[c].std())




df.describe().to_csv("week5_df_describe.csv")

"""
mode
median
kurtosis
skewness
Mean-3 x std
Mean+3 x std
upper count
lower bound (q1-IQR)
Upper bound (q3+IQR)
IQR = [range x 1,5] interquartile range
Range (q3-q1)
Q3 – similar to std
Q1 – similar to std
Nofzeros
Deviation ratio(her zaman dogru degil)
Mean-std
mean+std
standard deviation
fillness ratio
nofitems
count
avg
min
max
"""

# TASK: Find outlier values in ALL columns
for c in df.columns:
    dtype = str(df.dtypes[c])
    if dtype in ['int64', 'float64']:
        #: First approach        
        q3 = df[c].quantile(0.75)
        q1 = df[c].quantile(0.25)
        iqr = q3 - q1
        upper = q3 + 1.5 * iqr
        lower = q1 - 1.5 * iqr

        #: Second approach
        mean = df[c].mean()
        std = df[c].std()

        upper2 = mean + 3 * std
        lower2 = mean - 3 * std


        print(c, upper, lower, upper2, lower2)


# Mode may have problems. If there are many items with freq 1, it may return all table!!
# There may not be "MOST FREQUENT"
for c in df.columns:
    mode = df[c].mode()
    if len(mode) == 1:
        print(c)
        print(mode.iloc[0])
        print("==================")
    else:
        print(c)
        print(None)
        print("==================")




for c in df.columns:
    mode = df[c].mode()
    if len(mode) == 1:
        print("MODE", c, mode.iloc[0])
    else:
        print("MODE", c, None)


# cardinality
# number of uniuque items / number of items



for c in df.columns:
    nof_items = df[c].count() # counts the number of non-values
    nof_unique = df[c].nunique() # counts the DISTINCT number of items
    print("CARDINALITY", c, nof_unique / nof_items)

    if nof_unique == 1:
        print("!!!!!!!!!!!!!!!", c)

# if cardinality == 1.0, all unique, MEANINGLESS
# if cardinality is very low, this columns is a flag!! or a categoric column

# RULE: if there is only "ONE" value in a column, DELETE
# RULE: if cardinality is 1.0, DELETE



