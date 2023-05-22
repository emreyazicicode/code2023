import datetime

# Create your own rules
#  ---> If you are going to define a student, you MUST have his/her number or name


# UST SINIFTA OLAN HERSEY, ALT SINIFTA VARDIR!!

# MAIN, SUPER, UPPER, TOP, 
class Person:
    def __init__( self, fname: str, lname: str ): # CONSTRUCTOR
        self.firstname = fname
        self.lastname = lname
        self.gender = None

class Student( Person ):
    def __init__( self, fname: str, lname: str, number: int = 0, universityyear: int = 1 ):
        #                                                        ^ optional argument
        super().__init__(fname, lname)
        self.number = number
        self.universityyear = universityyear

class Lecturer( Person ):
    def __init__( self, fname: str, lname: str, graduatedFrom: str ):
        super().__init__(fname, lname)
        self.graduatedFrom = graduatedFrom
        self.numberOfPublishedBooks = 0
    
    # Lecturer has "numberOfPublishedBooks" attribute / property
    # But student does not have "numberOfPublishedBooks" attribute / property

# Dean is a Lecturer already!!!
class Dean( Lecturer ):
    def __init__( self, fname: str, lname: str, graduatedFrom: str, deanForHowManyYears: int ):
        super().__init__(fname, lname, graduatedFrom)
        self.deanForHowManyYears = deanForHowManyYears

class Manager( Person ):
    def __init__( self, fname: str, lname: str, workingHowManyYears: int ):
        super().__init__(fname, lname)
        self.workingHowManyYears = workingHowManyYears

sa = Student("x", "y", 11234242 )
print(sa.universityyear)
sb = Student("x", "y", 11234242, 3 )
print(sb.universityyear)


sc = Student("x", "y", 11234242, None )


s = Student("x", "y", 1)
#! print(s.Courses)
#! AttributeError: 'Student' object has no attribute 'Courses'

s = Student("x", "y", 1)
s.gender = "Female"
# s.dob = datetime.date(1999,5, 5)
s.universityyear = 2
print(s.firstname, s.lastname, s.number)

l = Lecturer("a", "b", "oxford")
l.gender = "Male"
l.numberOfPublishedBooks = 4
# l.dob = datetime.date(1984, 5, 5)
print(l.firstname, l.lastname, l.graduatedFrom)

d = Dean("q", "p", "cambrigde", 3)
d.numberOfPublishedBooks = 2


# ================================================
import json
mystudent = {
    'firstname': 'Emre',
    'lastname': 'Yazici',
    'number': 330432
}

# WRITE TO A JSON FILE
json.dump( mystudent, open('week3b.json', 'w') )
# ================================================
import pickle

s = Student("Mustafa", "YILDIRIM", 1)
s.gender = "Male"
s.universityyear = 2

pickle.dump(s, open('examplePickle.pickle', 'wb')) # W = write B = Binary, complex format

s2 = pickle.load(open('examplePickle.pickle', 'rb'))  # R = read

print(s.firstname)
print(s2.firstname)


"""
class Person:
    def __init__( self ):
        self.firstname = None
        self.lastname = None
        self.gender = None
        self.dob = None

class Student( Person ):
    def __init__( self, number: int ):
        super().__init__()
        self.number = number
        self.universityyear = 1

class Lecturer( Person ):
    def __init__( self, graduatedFrom: str ):
        super().__init__()
        self.graduatedFrom = graduatedFrom



s = Student(123)
s.firstname = "X"
"""



