
# Extra assignment
a, b = 3, 4
c, d = "x", "y"


# COMMON PROPERTIES


# advantage of classes:
# you can clearly see the structure and the properties of each classes



#? Person 'in icinde ne vardir?
class Person:
    # Declaration:
    firstname: str = None                         # properties, ozellikler, nitelikler
    lastname: str = None

    def __init__( self, fname: str, lname: str ): # ZORUNLU OLARAK 2 TANE ARGUMENT ALALIM
        self.firstname, self.lastname = fname, lname

# I recommend to use the properties in the declaration as well

# __xxxxx__: Magic, special function

"""

Madina Abdulsamadova
class Department:
    dep_id: int = 0
    name: str = None
    manager: Person = None
    team_members: list = []
    
    def __init__(self, dep_id: str, name: str, manager: Person, team_members: list):
        self.dep_id  = dep_id
        self.name = name
        self.manager = manager
        self.team_members = team_members
        pass

"""

#*a = 3
#* a: int = 3 # TYPE DEFINITION
#* a: Person = None # Type definition
#* a = Person() # Initialize a new "INSTANCE - Kopya" of Person class


class Lecturer:
    person: Person = None  # This line does NOT calls the __init__ function yet
    graduatedfrom: str = None
    yearsofexperience: int = 0

class Course:
    name: str = None
    code: str = None
    lecturer: Lecturer = None

    def __init__( self, name: str, code: str, lecturer: Lecturer ):
        self.name = name
        self.code = code
        self.lecturer = lecturer

class Student:
    person: Person = None
    studentyear: int = 1
    number: int = 0
    courses: list = [] # LIST OF COURSES!


p1 = Person("Ahmet", "Kerimov") # WITH ARGUMENTS

s = Student()
s.person = p1
s.number = 10121

p2 = Person("XZ", "asds")

l1 = Lecturer()
l1.person = p2
l1.graduatedfrom = "oxford"

c1 = Course("Data science", "CS101", l1)

p3 = Person("QTX", "asdfjdsfds")

l2 = Lecturer()
l2.person = p3
l2.graduatedfrom = "harvard"

c2 = Course("Databases", "CS102", l2)

s.courses.append( c1 )
s.courses.append( c2 )
"""

print(s.firstname, s.lastname, s.number)
for c in s.courses:
    print("  ", c.name, c.code)
    print("     ", c.lecturer.firstname, c.lecturer.lastname, c.lecturer.graduatedfrom)


print( s.courses[0].lecturer.firstname )
"""
# Student'in, SIFIRINCI kursunun, mualliminin, ilk adi

# My friend's dog's tail
# Arkadasminin, kopeginin kuyrugu
# 's == nin == "." python





# Ahmet => doktora yapiyor (Phd = student)
# Ahmet => undergraduate (muallim)

# ======================================================================
"""
class Person:
    firstname: str = None
    surname: str = None
    age: int = 0

class Department:
    id: int = 0
    name: str = None
    manager: Person = None
    team_members: list = []

class Company:
    name: str = None
    departments: list = []

p1 = Person()
p1.firstname = "r"
p1.age = 40

p2 = Person()
p2.firstname = "q"
p2.age = 30

p3 = Person()
p3.firstname = "p"
p3.age = 25

d = Department()
d.id = 1
d.name = "Accounting"
d.manager = p1
d.team_members.append( p2 )
d.team_members.append( p3 )

c = Company()
c.name = "Pepsi"
c.departments.append( d )

# Translate?
c.departments[0].team_members[1].lastname
# sirketin, 0. departmaninin, departmentin 1. ci uzvunun lastname -i

# In a company, we need to create a stucture (classes) which we can store employees, departments, managers

"""









