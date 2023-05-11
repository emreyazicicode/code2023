students = {
    'Minəxanım Hacımuradova':[0, 7, 5, 6, 4, 4],
    'Lala Taghiyeva':[2, 5, 3, 7, 1, 3],
    'Yusif Ağasalamlı':[3, 4, 2, 3, 2, 2],
    'Həbibə Məmmədli':[3, 6, 2, 3, 2, 7],
    'Niyyət Rzayev':[3, 6, 4, 5, 6, 4],
    'Adil Rəhimov':[4, 5, 4, 3, 2, 5],
    'Riyad Əhmədov':[4, 5, 5, 4, 4, 6],
    'Ləman Rəhimli':[4, 6, 3, 5, 4, 4],
    'Riyad Əbdürəhimov':[4, 6, 4, 5, 7, 6],
    'İlyas Abbasov':[4, 6, 5, 6, 3, 3],
    'Lalə Məmmədli':[4, 8, 6, 6, 4, 2],
    'Anar Əhmədov':[5, 7, 5, 6, 6, 3],
    'Mahmizər Həsənova':[6, 4, 3, 7, 5, 4],
    'Mədinə Abdulsəmədova':[6, 7, 5, 4, 6, 3]
}


def ikitalebekiyasla( t1, t2 ):
    tv1 = students[t1]
    tv2 = students[t2]

    fark = 0
    for i in range(6):
        fark += abs(tv1[i] - tv2[i])

    return fark



en_benzer = 100000
en_benzer_nefer = None

for s in students:
    result = ikitalebekiyasla( s, 'Lalə Məmmədli' )
    if s != 'Lalə Məmmədli':
        if result < en_benzer:
            print("BULUNDU:", s, "result=", result, "en_benzer=", en_benzer, "en_benzer_nefer", en_benzer_nefer  )
            en_benzer = result
            en_benzer_nefer = s
        else:
            print("BENZER DEGIL:", s, "result=", result, "en_benzer=", en_benzer, "en_benzer_nefer", en_benzer_nefer  )





