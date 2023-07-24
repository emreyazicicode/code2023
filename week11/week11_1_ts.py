from math import ceil
import datetime
import pandas as pd
from datetime import date, timedelta
import calendar
from calendar import monthrange



import ephem
import datetime

def calculate_day_length(latitude, longitude, date):
    observer = ephem.Observer()
    observer.lat = str(latitude)  # Latitude in degrees
    observer.lon = str(longitude)  # Longitude in degrees
    observer.elevation = 0  # Sea level elevation (you can adjust this if needed)

    # Convert the input date to a PyEphem date
    date_format = "%Y-%m-%d"
    #!date_obj = datetime.datetime.strptime(date, date_format)
    date_obj = date
    observer.date = date_obj.strftime(date_format)

    # Calculate the sunrise and sunset times for the given date and location
    sunrise = observer.previous_rising(ephem.Sun())
    sunset = observer.next_setting(ephem.Sun())

    # Calculate the day length (time between sunrise and sunset)
    day_length = sunset - sunrise

    # Convert the day length to hours, minutes, and seconds
    hours = int(day_length * 24)
    minutes = int((day_length * 24 * 60) % 60)
    seconds = int((day_length * 24 * 60 * 60) % 60)

    return hours, minutes, seconds



VALUE_MAPS = {
	'season1': { 1: 1, 2: 1, 3: 1, 4: 2, 5: 2, 6: 2, 7: 3, 8: 3, 9: 3, 10: 4, 11: 4, 12: 4 },
	'season2': { 12: 1, 1: 1, 2: 1, 3: 2, 4: 2, 5: 2, 6: 3, 7: 3, 8: 3, 9: 4, 10: 4, 11: 4 },
	'summerwinter': { 
		10: 1, 11: 1, 12: 1, 1: 1, 2: 1, 3: 1, # COLD
		4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0     # HOT
	},
}


def weekOfYear( dto ):
	return int(dto.isocalendar()[1])


# method: weekOfMonth
# Returns the week of month
# @dt, datetime: The input
# @return, int: The output
# @completed
def weekOfMonth(dto: datetime) -> int:
	first_day = dto.replace(day=1)
	dom = dto.day
	adjusted_dom = dom + first_day.weekday()
	return int(ceil(adjusted_dom/7.0))

# data role ==> numeric, flag, categoric, .....
# Question 5: The values !!! of the season1 and season2 are ... variables

# Jan, Feb, Mar ==> 1 [3]  # winter
# Ap, May, Jun  ==> 2 [3]

# Season, climate ==> Dec, Jan, Feb ==> 1 # winter
#                     Mar, Apr, May ==> 2

def season1( dto ):
	return mapper( 'season1', dto.month )

def season2( dto ):
	return mapper( 'season2', dto.month )

def summerWinter( dto ):
	return mapper( 'summerwinter', dto.month )

# method: mapper
# Maps a label to corresponding value
# @mapName, str: The name of the map
# @mapValue, object: The label
# @return, object: The mapped value
# @completed
def mapper( mapName: str, mapValue: object ) -> object:
	#: Return
	return VALUE_MAPS[mapName][mapValue]


def dayOfYear( dto ):
	return float(dto.timetuple().tm_yday) / 366.0

def daysInMonth( dto ): # dto ==> date time object
	return int(monthrange( dto.year, dto.month )[1])

def lastDayFriday( dto ):
	return dto.weekday() == 4 and daysInMonth( dto ) == dto.day

# method: lastFriday
# Returns the day index of the last friday
# @year, int: The input year
# @month, int: The input month
# @return, int: The output
# @completed
def lastFriday(year: int, month: int) -> int:
	return max(week[calendar.FRIDAY] for week in calendar.monthcalendar(year, month))

# method: firstMonday
# Returns the day index of the first monday
# @year, int: The input year
# @month, int: The input month
# @return, int: The output
# @completed
def firstMonday(year: int, month: int) -> int:
	return min(week[calendar.MONDAY] for week in calendar.monthcalendar(year, month))



#: Find the list of holidays
# call center
tr_tatiller = ['2018-08-20','2018-08-21','2018-08-22','2018-08-23','2018-08-24','2018-08-30','2019-08-10','2019-08-11','2019-08-12','2019-08-13','2019-08-14','2019-08-30','2020-08-01','2020-08-02','2020-08-03','2020-08-30','2018-12-31','2019-12-31','2020-12-31','2018-10-28','2018-10-29','2019-10-28','2019-10-29','2020-10-28','2020-10-29','2018-06-14','2018-06-15','2018-06-16','2018-06-17','2019-06-03','2019-06-04','2019-06-05','2019-06-06','2018-05-01','2018-05-19','2019-05-01','2019-05-19','2020-05-01','2020-05-19','2020-05-23','2020-05-24','2020-05-25','2020-05-26','2018-04-23','2019-04-23','2020-04-23','2018-01-01','2019-01-01','2020-01-01','2018-07-15','2019-07-15','2020-07-15','2020-07-30','2020-07-31']
#: Make a unique list
tr_tatiller = list(set(tr_tatiller))
#: Load the dataset
df = pd.read_excel( "week10_tsdata_original.xlsx" )
#: A function to check a "TimeStamp object" in a list or not
def isholiday( dt ) -> bool:
    #: Split to get only date part, skip the time part
    dt = str(dt).split(' ')[0]
    #: Check the date part is in list of holidays
    return dt in tr_tatiller

#: Create a column of holidays
df['Holiday'] = df['Date'].apply( isholiday )
#: Convert to integer
df['Holiday'] = df['Holiday'].astype(int)

print("Holiday Count:Match", df['Holiday'].sum() )
print("Holiday Count:List", len(tr_tatiller) )

#: Question 1: Do the holidays effect the results? (Value):    
#: Question 2: In which direction it should effect, if so?:    NEGATIVE!!!

# How do we measure effect?
# Correlation
# Averages of mean

print("Corr Holiday", df['Holiday'].corr(df['Value']))

#: We create some more features
df['WeekDay'] = df['Date'].dt.day_of_week
# df['WeekEnd'] = df['WeekDay'].apply(lambda value: value in [5,6])
df['WeekEnd'] = df['WeekDay'].isin([5,6])
df['WeekEnd'] = df['WeekEnd'].astype(int)

print("Corr WeekEnd", df['WeekEnd'].corr( df['Value'] ) )

#: Question 3: Why weekend is more correlated than holiday
# 2/7           = 0.28
# holiday ratio = 0.06

df['Day'] = df['Date'].dt.day
df['Month'] = df['Date'].dt.month
# df['FirstDays'] = df['Day'] < 5 # they get their salary in first week
#print("Firstdays WeekEnd", df['FirstDays'].corr( df['Value'] ) )
# they make their montly operations in the first week
# Hypothesis

df['LastDays'] = df['Day'] > 26 # they get their salary in first week
print("LastDays WeekEnd", df['LastDays'].corr( df['Value'] ) )

# Devlet, 15
# df['MiddleDays'] = df['Day'].isin([13,14,15,16,17])
# print("MiddleDays WeekEnd", df['MiddleDays'].corr( df['Value'] ) )

df['summerBreak'] = df['Month'].isin([5,6,7])
print("summerBreak", df['summerBreak'].corr( df['Value'] ) )

#if variation == "summerBreak": return self.dataFrame[ column ].dt.month.isin( [5,6,7,8] )

"""
for r in range(0, 100, 5):
    i = r / 100.0
    df['dayOfYear'] = df['Date'].apply(lambda val: dayOfYear(val)) > i
    print(i, "dayOfYear", df['dayOfYear'].corr( df['Value'] ) )
"""

df['FirstMonth'] = df['Month'] == 1
df['LastMonth'] = df['Month'] == 12

#			if variation == "season1": return self.dataFrame[ column ].apply( lambda row: season1( row ) )
#			if variation == "season2": return self.dataFrame[ column ].apply( lambda row: season2( row ) )
#			if variation == "summerWinter": return self.dataFrame[ column ].apply( lambda row: summerWinter( row ) )

df['Season1'] = df['Date'].apply(lambda val: season1(val))
df['Season2'] = df['Date'].apply(lambda val: season2(val))

df['SummerWinter'] = df['Date'].apply(lambda val: summerWinter(val))
print("SummerWinter", df['SummerWinter'].corr( df['Value'] ) )

df['FirstHalf'] = df['Month'] < 7
print("FirstHalf", df['FirstHalf'].corr( df['Value'] ) )

df = pd.get_dummies( df, columns = ['Season1', 'Season2'] )

cols = list(df.columns)

cols = [c for c in cols if c in ['Season1_2', 'Season2_1'] or 'Season' not in c ]

# ['Date', 'Value', 'Holiday', 'WeekDay', 'WeekEnd', 'Day', 'Month', 
# 'LastDays', 'summerBreak', 'FirstMonth', 'LastMonth', 'SummerWinter', 
# 'FirstHalf', 'Season1_1', 'Season1_2', 'Season1_3', 'Season1_4', 
# 'Season2_1', 'Season2_2', 'Season2_3', 'Season2_4']


# Season1_2	Season2_1

"""
# MANUAL WAY
del df['Season1_1']
del df['Season1_3']
del df['Season1_4']
del df['Season2_2']
del df['Season2_3']
del df['Season2_4']
"""

df = df[ cols ] # some columns will be eliminated



# 30
# 31
# 28 [very rare]
# 29 [very rare]


df['weekOfMonth'] = df['Date'].apply(lambda val: weekOfMonth(val))


df['DayLength'] = df['Date'].apply(lambda val: calculate_day_length(41.015137, 28.979530, val)[0])



#df["MidTerm"] = (df["Date"].dt.month == 2) & (df["Date"].dt.day <= 14)
#print(df["MidTerm"].sum())
"""
df['MidTerm'] = ................ true/false
df['MidTerm'] = df['MidTerm'].astype(int)

print( df[(df["Date"].dt.month == 2) & (df["Date"].dt.day <= 14)] )

# df.Date = df['Date']



According to the order, classes in general educational institutions start on September 15 and end on June 14. 
The academic year is divided into two semesters:
- first semester - September 15 - January 26;
- second semester - February 1 - June 14.
"""



# 1. hafta, 2. hafta

"""
if variation == "daylength": return self.dataFrame[ column ].apply( lambda row: daylength( row ) )
if variation == "dayLengthg10": return self.dataFrame[ column ].apply( lambda row: daylengthGT( row, 10 ) )
if variation == "dayLengthg11": return self.dataFrame[ column ].apply( lambda row: daylengthGT( row, 11 ) )
if variation == "dayLengthg12": return self.dataFrame[ column ].apply( lambda row: daylengthGT( row, 12 ) )
if variation == "dayLengthg13": return self.dataFrame[ column ].apply( lambda row: daylengthGT( row, 13 ) )
if variation == "dayLengthg14": return self.dataFrame[ column ].apply( lambda row: daylengthGT( row, 14 ) )
if variation == "weekPercentage": return self.dataFrame[ column ].apply( lambda row: weekPercentage( row ) )
if variation == "dayPercentage": return self.dataFrame[ column ].dt.day / 30.0
if variation == "weekPercentage": return self.dataFrame[ column ].apply( lambda row: lastDayFriday( row ) )
"""


#print(df.head(25))
df.to_csv("week11_1_ts.csv")
df.corr().abs().to_csv("week11_1_corr.csv")


print(df.corr())

