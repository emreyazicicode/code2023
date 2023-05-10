
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

kucuk = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
buyuk = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def checkPassword( password ):
	if len(password) < 8:
		return False

	kucuk_var = False
	buyuk_var = False
	digit_var = False

	for p in password:
		if p in kucuk:
			#print(p, 'kucuk')
			kucuk_var = True
		elif p in buyuk:
			#print(p, 'buyuk')
			buyuk_var = True
		elif p in digit:
			#print(p, 'digit')
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

	if kucuk_var == True and buyuk_var == True and digit_var == True: 
		return True
	else:
		return False



password = input("Sifreyi giriniz: ")
print( checkPassword( password ) )









