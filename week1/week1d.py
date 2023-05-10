
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
	if len(password) < 8:
		return False
	if len(set(password)) < 5:
		return False

	kucuk_var = False
	buyuk_var = False
	digit_var = False

	for i, p in enumerate(password):

		if i > 0 and password[i] == password[ i-1 ]:
			return False

		if p in kucuk:
			kucuk_var = True
		elif p in buyuk:
			buyuk_var = True
		elif p in digit:
			digit_var = True
		

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

print(checkPassword4("123456Aa"))


# invalids
# axfdbcasdfs         ==> bc
# dsadjfljl67asdfkjs  ==> 67
# abc                 ==> ab, bc
# 








