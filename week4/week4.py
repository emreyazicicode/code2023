
from MySQLConnection import *
from week4queries import QUERIES
import datetime

def something(a):
    # some operation

    return 3, True
    # (3, True)


def askForWeather(location):
    # web service call

    return 28, 'very hot'


r = askForWeather( 'Baku' )

print(r)


degree, condition = askForWeather( 'Baku' )

print(degree)
print(condition)


a, b = "3", "4"
print(a)
print(b)


# LIMIT 0, 1 ==> LIMIT 1
# LIMIT 1, 1 ==> 2. kaydi getir

result, columnNames = dbSelect("SELECT * FROM cities LIMIT 0, 5;", ())


for r in result:
    p = rowToDict( r, columnNames )
    print("p", p)
    print("r", r)



r, c = dbSelect( QUERIES['customers'], () )

# .. later on ...
r, c = dbSelect( QUERIES['customers'], () )

# CENTRIC = MERKEZI 

r, c = dbSelect("SELECT COUNT(*) FROM products;", ())
# 1 row, 1 column ==> 1 CELL

record_zero = r[0]
value_zero = record_zero[0]
print(record_zero)
print(value_zero)

print( r[0][0], type(r[0][0]) )


r, c = dbSelect( QUERIES['customers'], () )
print(c)
print(r)
firstrow = r[0]
print(firstrow[1])


mydata = (103, 'Atelier graphique', 1)
print(mydata[1])




r,c = dbSelect(QUERIES['customersinfo'], [144])

print(r)

print(QUERIES['customersinfo'].replace("%s", "199"))

r,c = dbSelect(QUERIES['customersinfo'].replace("%s", "144"), ())


print("LATEST", r)

# FOR EACH INCOMING QUERY !! SQL SELECT, MYSQL STORES IT TO SOMEWHERE!!!


rows, c = dbSelect(QUERIES['mostbuyingcompanies'] )

for row in rows:
    print(rowToDict( row, c ) )
for row in rows:
    print(row )
for row in rows:
    print(list(row) )


rows, columns = dbSelect("SELECT * FROM orders;")

print(rows)

for row in rows:
    print(row[1], row[1].day, row[1].month, type(row[1]))

