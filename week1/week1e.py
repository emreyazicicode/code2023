
def sicaklikTest( sicaklik ):
    if sicaklik > 35:
        print("cok sicak")
    else:
        print("normal")



def sicaklikTest2( sicaklik ):
    if sicaklik > 35:
        return True
    else:
        return False


result = sicaklikTest2(40)
if result == True:
    print("cok sicak")
else:
    print("sicak")

talebeler = [
    {"Mahmizər Həsənova":{"degree": "IT", "courses":["analytics", "statistics"], "no": 1234}},
    {"Mədinə Abdulsəmədova":{"degree": "Business Informatics", "courses":["analytics", "statistics"], "no": 1234}},
    {"Adil Rəhimov":{"degree": "Automation", "courses":["analytics"], "no": 1234}},
    {"Rafiq Rafiqzadə":{"degree": "Automation", "courses":["analytics"], "no": 1234}},
    {"Anar Əhmədov":{"degree": "Data Science", "courses":["analytics"], "no": 1234}},
    {"Minəxanım Hacımuradova":{"degree": "Computer Engineering", "courses":["analytics"], "no": 1234}},
    {"Riyad Əhmədov":{"degree": "IT", "courses":["analytics"], "no": 1234}},
    {"Riyad Əbdürəhimov":{"degree": "IT", "courses":["analytics"], "no": 1234}},
    {"Lalə Məmmədli":{"degree": "Artificial Intelligence", "courses":["analytics"], "no": 1234}},
    {"İlyas Abbasov":{"degree": "Computer Science", "courses":["analytics"], "no": 1234}},
    {"Yusif Ağasalamlı ":{"degree": "Computer Science", "courses":["analytics"], "no": 1234}},
    {"Ləman Rəhimli":{"degree": "Maths", "courses":["analytics"], "no": 1234}},
    {"Həbibə Məmmədli":{"degree": "Maths", "courses":["analytics"], "no": 1234}},
    {"Lala Taghiyeva":{"degree": "Policy Analysis", "courses":["analytics"], "no": 1234}},
    {"Niyyət Rzayev":{"degree": "Automation", "courses":["analytics"], "no": 1234}}
]



talebeler = [
	{'name': 'ahmet', 'no':12342, 'courses': ['data science', 'analytics', 'statistics', 'maths']},
	{'name': 'ali', 'no':1389, 'courses': ['statistics']},
	{'name': 'mehmet', 'no':389, 'courses': ['maths', 'analytics']},
]


output = []
def filtrele( ders ):
    for t in talebeler:
        if ders in  t['courses']:
            output.append( t['name'] )
    return output


print(filtrele("maths"))
print(filtrele("maths"))
print(filtrele("analytics"))



