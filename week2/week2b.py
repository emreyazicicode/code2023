
# NUMERIC OPERATIONS LIBRARY


# while writing the code below, I am DEVELOPER!!!!!!
# USER FRIENDLY
def cleanupNumbers( text: str ) -> int: # LOCAL VARIABLE
    text = text.replace("$", "")
    text = text.replace("€", "") # "" ==> EMPTY STRING
    text = text.strip() # Removes the space around text
    text = text.replace(",", ".")
    text = int(text)
    return text # overwrite - change - update


def cleanupNumbers2( text: str )     : # LOCAL VARIABLE
    text = int(text.replace("$", "").replace("€", "").strip().replace(",", "."))
    # If I am going to use the "VALUE" 2 or more times, I need to assign to a variable 
    return text # overwrite - change - update
    # The variable "text" is deleted

def cleanupNumbers3( text: str )     : # LOCAL VARIABLE
    newtext = text.replace("$", "").replace("€", "").strip().replace(",", ".")
    if len(newtext) > 5: # million
        return 'TOO LARGE NUMBER'
    else:
        return newtext

def cleanupNumbers4( text: str )     : # LOCAL VARIABLE
    return int(text.replace("$", "").replace("€", "").strip().replace(",", "."))


# default value of small is False 
def cleanupNumbers5( text: str, small: bool = False ) -> int:
    text = text.replace("$", "").replace("€", "").strip().replace(",", ".")
    if small == True:
        text = smallRepresentaton( int(text) )
    return text

def cleanupDecimals( text: str ) -> float:

    return float(text)

def smallRepresentaton( number: int ) -> str:
    if number < 1000: 
        return str(number) 
    elif number < 100000:
        return str(round(number/1000, 1)) + "K" # Thousand = 10e3 = 10^3
    elif number < 100000000:
        return str(round(number/1000000,2)) + "M" # Million = 10e6 = 10^6
    elif number < 1000000000:
        return str(round(number/1000000000, 3)) + "B" # Billion = 10e9 = 10^9
    else:
        return str(round(number/1000000000000, 3)) + "T" # Trillion = 10e12 = 10^12


"""
3
35
350
3.5K
35.5K
0.36M
3.56M
35.55M
0.355B
0.004T
0.036T
0.355T
"""

def calculateWeight2( x, y, z, material: str = 'H2O', gravity: str = 'earth' ):
    if gravity == 'earth':
        gravity_value = 9.8
    elif gravity == 'moon':
        gravity_value = 1.72
# 3d object, mars, earth, moon
calculateWeight2( 10, 10, 10, 'AU', 'earth' ) # 9.8

# MUST = x: float, y: float, z: float,
# OPTIONAL = material: str = 'H2O', gravity: float = 9.8 
def calculateWeight( x: float, y: float, z: float, material: str = 'H2O', gravity: float = 9.8 ) -> float:
    materialweight = None
    if material == 'H2O':
        materialweight = 1.0
    if material == 'FE': # DEMIR, IRON, FERRIUM
        materialweight = 7.8
    elif material == 'AL': # ALIMINIUM
        materialweight = 13.6
    elif material == 'AU': # GOLD, ALTIN
        materialweight = 18.9
    return x * y * z * gravity * materialweight


def calculateWeight3( x: float, y: float, z: float ) -> float:
    return x * y * z * 9.8 * 1.0


# OPTIONAL ARGUMENTS
# If we use "=" in definition, it is a default value!
def cevreHesapla( radius: float, pi: float = 3.14 ) -> float:
    return 2 * pi * radius # 2πr

# OPTIONAL ARGUMENTS
# If we use "=" in definition, it is a default value!
def cevreHesapla2( radius: float) -> float:
    return 2 * 3.14 * radius # 2πr

# income levels are different in different cities
# istanbul === VERY HIGH 
# antalya  === MIDDLE

# ARGUMENTS ARE USED FOR CONDITION CHANGES!!!

def bankCustomerValue( salary: float, currency : str = 'Manat' ) -> str:
    # MANAT ?
    # TL
    # USD?

    if currency == 'Manat':
        salary = salary / 1.6
    elif currency == 'TL':
        salary = salary / 19

    if salary < 1000: return 'low'
    if salary < 2000 : return 'normal'
    return 'high'



#biz float yazanda o auto olaraq onu gravitye auto set etmeycek? 
#yeni parancesde tek float olsa (10, 20, 30,  5.0) boyle
