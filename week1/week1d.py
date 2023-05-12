
import enum


STRINGS = {
	'en': {
		'hello': "Hello game user {0}"
	},
	'az': {
		'hello': "Salam game user {0}"
	},
	'tr': {
		'hello': "Merhaba game user {0}"
	}
}


username = "emre"
lang = "az"

print(STRINGS[lang]['hello'].format(username))

print("ok")

a = [ "emre", 'ahmet', (3,4), 3.14, 5, True, None ]

print("! Salam {name}, {surname}".format(name = "emre", surname = "yazici"))
print("! Salam {0}, {1}".format("emre", "yazici"))
print("Salam " + "emre")

for c in a:
	print("Type Detection", c, type(c))

q = "  emre okula giT    "
print(dir(q))

print("capitialize", q.capitalize())
print("endswith", q.endswith("a"))
print("endswith", q.strip().lower().endswith("t"))
print("title", q.title())
print("lower", q.lower())
print("upper", q.upper())
print("split", q.split())
print("strip", q.strip())


q1 = q.strip()
q2 = q1.lower()
q3 = q2.endswith("t")

s = "/home/emre/Downloads/file123.txt"
print("Check exists", "Downloads" in s)

sifre = "123456"
print("len", len(sifre))

s1 = "Ahmet" # 20
s2 = "Lale"  # 19

print(s1 > s2)

print(ord(s1[0]))

print(ord("A"))
print(ord("a"))


l = ['istanbul', 'baku', 'london']
p = ['new york']
print(p in l)



# 8 karakter
# 1 buyuk harf
# 1 kucuk harf
# 1 rakam
# 5 farkli karakter

kucuk = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
buyuk = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

buyuk = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def checkPassword( password ):
	#: Check null
	if password == None: 
		return False
	
	if not type(password) is str:
		return False
		
	#: Immediately return if the length is shorter than 8
	if len(password) < 8:
		return False
	#: Must have at least 5 different characters
	if len(set(password)) < 5:
		return False
	#: Declare variables
	kucuk_var = False
	buyuk_var = False
	digit_var = False
	#: Loop for each character in the password
	for i, p in enumerate(password):

		#: Check the previous item as the same of this item
		if i > 0 and password[i] == password[ i-1 ]:
			return False
		#: If one character is followed by another, return false
		if i > 0 and abs(ord(password[i]) - ord(password[i-1])) == 1:
			return False

		#: Check do they have capital, lower and digit
		if p in kucuk:
			print(p, "kucuk")
			kucuk_var = True
		elif p in buyuk:
			print(p, "buyuk")
			buyuk_var = True
		elif p in digit:
			print(p, "digit")
			digit_var = True
		
	#: Evaluate the statement
	if kucuk_var == True and buyuk_var == True and digit_var == True: 
		return True
	else:
		return False

def checkPassword2( password ):
	if len(password) < 8:
		return False

	kucuk_var = False
	buyuk_var = False
	digit_var = False

	for p in password:
		if p.islower():
			#print(p, 'kucuk')
			kucuk_var = True
		elif p.isupper():
			#print(p, 'buyuk')
			buyuk_var = True
		elif p.isdigit():
			#print(p, 'digit')
			digit_var = True

	return kucuk_var == True and buyuk_var == True and digit_var == True

	if kucuk_var == True and buyuk_var == True and digit_var == True: 
		return True
	else:
		return False



def checkPassword3( password ):
	if len(password) < 8:
		return False

	kucuk_var = 0
	buyuk_var = 0
	digit_var = 0

	for p in password:
		if p.islower():
			kucuk_var += 1
		elif p.isupper():
			buyuk_var += 1
		elif p.isdigit():
			digit_var += 1

	return kucuk_var > 0 and buyuk_var > 0 and digit_var > 0
	return kucuk_var * buyuk_var * digit_var > 0



#password = input("Sifreyi giriniz: ")
#print( checkPassword( password ) )

sifre = "A5bAA5155555c5c5c5"
print(sifre)
print(list(sifre))
print(set(sifre))
print(list(set(sifre)))
print(sorted(list(set(sifre))))







def checkPassword4( password ):
	if len(password) < 8: 
		return False
	if len(set(password)) < 5: 
		return False

	kucuk_var = 0
	buyuk_var = 0
	digit_var = 0

	for i, p in enumerate(password):
		if p.islower():
			kucuk_var += 1
		elif p.isupper():
			buyuk_var += 1
		elif p.isdigit():
			digit_var += 1

	return kucuk_var * buyuk_var * digit_var > 0


password = "Emre12345"

print(checkPassword("AA12345ab"))



# yaziciemre@gmail.com
# seslufohes@gmail.com

# invalids
# axfdbcasdfs         ==> bc
# dsadjfljl67asdfkjs  ==> 67
# abc                 ==> ab, bc

# valid
# Ab14375975042
# aBc7f9dsa87f90sa






print(checkPassword("ejslkaj873849874"))

# metin = "abcdef"
# print(abs(ord(metin[3]) - ord(metin[2])) == 1)






# ()
# []


# {} curly brace

a = {"key": "value"}
b = {1,2,3}
c = "salam"
d = f"merhaba / {c}"

# ()
a = (3, 4, 5) # tuple
b = checkPassword("341239479") # method cagirma
c = (3+4)/2 # onceliklendirme

# []
a = ['a', 'b', 'c', 'd']
b = a[2]
c = a[0:3]

# .
a = ""
a.lower() # sub element
a = 4
b = a ** 2

# +
a = "3"
b = "4"
print(a+b)

a = 3
b = 4
print(a+b)


a = [0] * 5
print(a)

print(10%3)
print(not True)
print(True != True)
print(100 // 9)

if 1 > 0 and 0 > -1:
	print("OK")

def celsius_to_fahrenheit(celsius):
	return celsius * 9/5 + 32

if a == 3:
	print("ok")
elif a == 4 or a in [5,6,7]:
	print("test")
else:
	print("ok2")

def sicaklikKontrol( sicaklik ):
	if sicaklik > 40:
		return False
	if sicaklik < 10:
		return False
	return True

def sicaklikKontrol2( sicaklik ):
	return sicaklik >= 10 and sicaklik <= 40

def sicaklikKontrol3( sicaklik ):
	a =  True if sicaklik >= 10 and sicaklik <= 40 else False
	return a

def sicaklikmetin( sicaklik ):
	return 'cok sicak' if sicaklik > 30 else 'normal'


def sicaklikmetin2( sicaklik ):
	if sicaklik > 30:
		return 'cok sicak'
	else:
		return 'sicak'

def sicaklikmetin3( sicaklik ):
	if sicaklik > 30:
		return 'cok sicak'
	return 'sicak'

def sicaklikmetin3( sicaklik ):
	if sicaklik > 30: return 'cok sicak'
	return 'sicak'

index = 0
while index < 10:
	print(index)	
	index += 1


for a in "testsasfdss":
	if a == "s":
		break
	else:
		pass


talebeler = [
	{'name': 'ahmet', 'no':12342},
	{'name': 'ali', 'no':1389},
	{'name': 'mehmet', 'no':389},
]


def lookupTalebe( no ):
	for t in talebeler:
		if t['no'] == no:
			return t
	return None

age1 = 3
age2 = 3.0
print(5 * age1)
print(5 * age2)


max_memory = 64.0


# var types



