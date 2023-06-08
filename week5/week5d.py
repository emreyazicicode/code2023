import sys
import pandas as pd

#: Read the csv file and assign to to a "df" dataframe (note, only read 10000 rows)
#: Read the file at the beginning, it will be loaded into memory
df = pd.read_csv("week5_categoriconly.csv", nrows = 100000)

#! For, unknown and empty, non values
#* 1: Fill with ZERO
# Map, replaces the values with a "dictionary"
# Dictionary's key is the previous value, dictionary's value is the replacement
df['new_cell'] = df['new_cell'].map( {'Y': 1, 'N': 0, 'U': 0} )

#* 2: Analyze or model [Seperately]
dfA = df[ df['infobase'].notnull() ]  # Null olmayanlar
dfB = df[ df['infobase'].isnull() ]   # Null olanlar

#* 3: Fill with "most!"
# Fillna: Fill the Na/Null/None with ... =>
# df['ownrent'] = df['ownrent'].fillna( df['ownrent'].mode()[0] )

#* 4: For numerical ones
# Fill with MEAN, Fill with MEDIAN

#* 5: Find the relations - co-occoureance between multiple columns
#! 

#* 6: Logically find or estimate
# For example, a lawyer, doctor, engineer must be graduated from a university (at least, or phd)

#* 7: Find from a model
# We can create a machine learning model to find empty values FIRST, 
# then we can continue our analysis

#* 8: Fill by ratio or (if numeric) by distribution
# Faize gore doldurma

# Filled
dfO = df[ df['ownrent'] == 'O' ]        # 64K   %97
dfR = df[ df['ownrent'] == 'R' ]        # 2K    %3

# Non filled
dfN = df[ df['ownrent'].isnull() ]      # 33K


for c in dfO:
    most_in_owner = dfO[c].mode()[0]
    most_in_rent = dfR[c].mode()[0]

    if most_in_owner != most_in_rent:
        print(c, most_in_owner, most_in_rent)

#prizm_social_one S U
#dwlltype S M    # medium, small
#marital M S     # married, single

nn = df[ df['ownrent'].notnull() ]
ownerside = nn[ (nn['prizm_social_one'] == 'S') & (nn['dwlltype'] == 'S') & (nn['marital'] == 'M') ]
rentside = nn[ (nn['prizm_social_one'] == 'U') & (nn['dwlltype'] == 'M') & (nn['marital'] == 'S') ]

# Conclusion: owner side olanlar, can be replaced with "O"
#             but we do not the other ones yet
# NOTE: see below

# New function: value_counts()
print(ownerside['ownrent'].value_counts())
print(rentside['ownrent'].value_counts())


#! LATER: Customer_ID 1000001 1000005

# Chunk = parca
chunk = 100
length = len(df) # 100000
chunk_size = int(length / chunk)  # 33333


# 0. record ........................................... 99999. record
# 

#* 5th usage of [] brackets in dataframe
# If there is a "range", it returns the rows in the range
# 300:500

for i in range(chunk): 
    subset = df[ i*chunk_size:(i+1)*chunk_size ]
    counts = subset['ownrent'].value_counts().to_dict()

    print(i, i*chunk_size,(i+1)*chunk_size, counts['O'] / (counts['O'] + counts['R']))


"""
    # 0 ile 33333
    # 33333 ile 66666
    # 66666 ile 99999

    i = 0
    start = i * 33333            # 0
    end =   (i+1) * 33333        # 33333

    i = 1
    start = 1 * 33333            # 33333
    end =   (i+1) * 33333        # 66666


    i = 2
    start = 2 * 33333            # 66666
    end =   (i+1) * 33333        # 99999
    df[ start:end ]

"""



# TODO, we will see how we can replace!!
nn = df[ df['ownrent'].notnull() ]
ownerside = nn[ (nn['prizm_social_one'] == 'S') & (nn['dwlltype'] == 'S') & (nn['marital'] == 'M') ]
# Conclusion: owner side olanlar, can be replaced with "O"
#             but we do not the other ones yet

#     if value == None or pd.isna(value):
#        print(value)

def replace(row):
    #: If in this row, the value of "ownrent" is "empty/null/non"
    if row['ownrent'] == None or pd.isna(row['ownrent']):
        #: If it matches with the query below 
        if row['prizm_social_one'] == 'S' and row['dwlltype'] == 'S' and row['marital'] == 'M': 
            #: Return "OWNER" (we estimated this)
            return 'O'
        else:
            return 'UNKNOWN'
    
    # IF NOT EMPTY
    # DEFAULT VALUE, WHATEVER IS IN CELL
    return row['ownrent']

df['ownrent']= df.apply(replace, axis = 1)

print(df['ownrent'])

# prizm_social_one --> distribution'a gore dolduralim

"""
S %20
T %10
U %50
C %30
"""

# FREQUENCIES
df[].value_counts().to_dict()

