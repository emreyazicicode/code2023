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
    

s1 = Student("Ahmet", "YILMAZ", 1506)
s1.gender = "Male"
s1.universityyear = 2

s2 = Student("Ahmet", "YILMAZ", 1506)
s2.gender = "Male"
s2.universityyear = 2

print(s1 > s2)
# YAHSI MI?
# a better student?
# previous / next student

