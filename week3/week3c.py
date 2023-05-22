class Person:
    def __init__( self, fname: str, lname: str ): # CONSTRUCTOR
        self.firstname = fname
        self.lastname = lname
        self.gender = None

    def __str__( self ):
        return self.firstname.lower() + " " + self.lastname.lower()

class Student( Person ):
    def __init__( self, fname: str, lname: str, number: int = 0, universityyear: int = 1 ):
        #                                                        ^ optional argument
        super().__init__(fname, lname)
        self.number = number
        self.universityyear = universityyear

    def __str__(self):
        return super().__str__() + " No:" + str(self.number) + " as " + self.gender
    
    def __add__(self, argument): # (+) 
        self.universityyear += argument
        return self

s = Student("Ahmet", "YILMAZ", 1506)
s.gender = "Male"
s.universityyear = 2

print( s )
# <__main__.Student object at 0x7fe2bcd06f40>
# Ahmet YILMAZ No:1506 as Male


#s = s + 1 #? bu ne demek
          # Talebe, sinifi gecince, bir artsin
          # universityyear bir artsin
          # WE DO DEFINE THIS



a = 3 + 1          # SUM                   a = 4
b = "x" + "y"      # CONCAT                b = "xy"

print(s.universityyear)
s += 1          # next year student     s = ??? s.universityyear = s.universityyear + 1
print(s.universityyear)
s += 1          # next year student     s = ??? s.universityyear = s.universityyear + 1
print(s.universityyear)




s1 = Student("Ahmet", "YILMAZ", 1506)
s1.gender = "Male"
s1.universityyear = 2

s2 = Student("Ahmet", "YILMAZ", 1506)
s2.gender = "Male"
s2.universityyear = 2


print(s1 == s2)