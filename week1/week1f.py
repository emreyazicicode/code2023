import statistics
import random

def seller2(offers):
    if len(offers)==1:
        return 1000        
    elif statistics.median(offers) <= offers[-1]:
        return statistics.median(offers) * 1.5
    else:
        return statistics.median(offers)
    return 0


def seller(offers):
    if len(offers)==1: return 1000
    if len(offers)==3: return 750
    buyer_says = offers[-1]
    me_says = offers[-2]
    faiz_map = [
        0.95,
        0.75,
        0.60,
        0.55,
        0.50
    ]

    index = int((len(offers) - 1) / 2)
    if index < 4:
        print("!", buyer_says, me_says)
        return buyer_says + (me_says - buyer_says) * faiz_map[index]


    return 0

def buyer(offer: list):
    # define buyer 
    if offer == []:
        return 5
    if offer[-1] > 402.5:
        new_offer= offer[-2] + ((offer[-1] - offer[-2] )* 0.15)
        if new_offer > 402.5:
            return 10
        else:
            return new_offer
    elif offer[-1] > 100:
        if len(offer) <=  20:
            my_offer =  offer[-2] + offer[-2] * 0.2
            if my_offer < offer[-1]:
                return my_offer
            else:
                return offer[-1]
        elif len(offer) <= 30:
            last_offer =  offer[-2] + (offer[-1]-offer[-2]) *0.25
            if last_offer >=402.5:
                return 402.5
            else:
                return last_offer
        elif len(offer) == 38:
            return 402.5
    else: 
        return 0


# minimum = 5
# maximum = 1000

buyer_offer = 10
# first, buyer starts 10 manat
seller_offer = seller( [buyer_offer] )  # ODD
# seller_offer = 900
buyer_offer = buyer( [10, 900] )        # EVEN
# buyer_offer = 60
seller_offer = seller( [10, 900, 60] )

def router():
    first = buyer([]) # 0 ---> EVEN
    remaining = [first]
    
    cost = 0
    for i in range(20):
        returned = seller( remaining )
        if returned == 0: return "SELLER ACCEPTED", remaining, cost
        remaining.append( returned )
        returned = buyer( remaining )
        if returned == 0: return "BUYER ACCEPTED", remaining, cost
        remaining.append( returned )
        cost = cost + 5 # 5 manat!
    return "NO ONE ACCEPTED", remaining, cost


buyer_wins = 0
seller_wins = 0
for _ in range(100):
    net = random.randint(5, 1000)
    a, r, c = router()
    b = net - r[-1] - c
    s = r[-1] - net - c
    if b > s and b > 0:
        buyer_wins += 1
    elif b < s and s > 0:
        seller_wins += 1

print("buyer_wins", buyer_wins)
print("seller_wins", seller_wins)






message = """Türkün yolu Türk Dövlətləri Təşkilatından, Orta Dəhlizdən, Zəngəzurdan və Qarabağdan keçir. Bunu Türkiyənin xarici işlər naziri Mövlud Çavuşoğlu deyib. M.Çavuşoğlu Cümhuriyyət Xalq Partiyasının sədri Kamal Kılıçdaroğluna xitabən Türkiyənin Azərbaycandan yan keçə bilməyəcəyini deyib. Azərbaycandan nə istəyirsiniz? Azərbaycan Qarabağı geri alanda hər cür dəstəyi verdik. Siz, təəssüf ki, Türkiyə Azərbaycanı dəstəklədi dediniz. Azərbaycan niyə hərb meydanına endi? Öz torpaqlarını geri almaq üçün. Azərbaycan Ermənistanın torpaqlarına hücum etməyib ki?, - Türkiyənin xarici siyasət idarəsinin rəhbəri Kamal Kılıçdaroğluna xitabən deyib. Çavuşoğlu qeyd edib ki, bu gün türk dünyası güclüdür. Öz milli müdafiə sistemlərimiz var. Düşmənə möhtac deyilik. Azərbaycandan nə istəyirsiniz? Bu gün Türkiyə böyük türk dünyasını birləşdirir. Bu gün Türkiyə Türk Dövlətləri Təşkilatının arzusunu, yəni türk dünyasının birləşmək arzusunu həyata keçirən bir ölkədir."""

import random
def scramble( text ):
    chars = list(set(list(text)))
    remaining = chars[:]
    charmap = {}
    for c in chars:
        charmap[c] = random.choice( remaining )
        remaining.remove( charmap[c] )
    text = [charmap[t] for t in list(text)]
    text = "".join(text)
    return text, charmap


result, charmap = scramble( message )
print(result)