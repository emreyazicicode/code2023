people = {
    "Mahmizər Həsənova": ['t-shirt','coca-cola','lays','yogurt','spf cream','jean','bracelet'],
    "Mədinə Abdulsəmədova": ['nemlendirici','ayaqqabi','spor tayt','b12 vitamin','gunes kremi','dedektifsen oyunu','stefan zweig- amok','kemikli bulka','simit'],
    
    "İlyas Abbasov": [],
    "Adil Rəhimov": [],
    "Lala Taghiyeva": [],
    "Rafiq Rafiqzadə": [],
    "Anar Əhmədov": ["sunflower seeds", "peanut", "cheese balls", "carbonate", "coca-cola", "lays", "banana", "ice cream"],
    "Minəxanım Hacımuradova": ['sweets', 'trousers', 'tomatoes', 'beans', 'fabric', 'date fruit', 'soap', 'water', 'coffee'],
    "Riyad Əhmədov": [],
    "Riyad Əbdürəhimov": [],

    "Lalə Məmmədli": ['shoes','bag','short','swimming goggles','pie','ice cream','chocolate','shampoo'],
    "Yusif Ağasalamlı": ['short','shoes','bread','sandwich','beer','ice-cream','shirt'],
    "Ləman Rəhimli": ['tshirt','skincare products','jeans','macbook case and screen protector','antiperspirant','bag','sweatshirt'],
    "Həbibə Məmmədli": ['pantolon','t-shirt','terlik','spor ayakkabı','sac kremi','bebek shampuani','bebek kremi','manyetik egitici meyve hayvanlar seti'],
    "Niyyət Rzayev": ['energy drink','parfum','coffee ','maxito','burger','krampon'],
}


def jaccardSimilarity( a:list, b:list ) -> float:

    if len(a) + len(b) == 0: return 0

    anb = set(a).intersection(set(b))
    aub = set(a).union(set(b))

    anb = len(anb)
    aub = len(aub)

    return anb / aub

def cleanup( text: str ) -> str:
    text = text.replace("-", "")
    text = text.replace(" ", "")
    text = text.strip()
    text = text.lower()
    return text

# results = []
for a in people:
    for b in people:
        """
        a = "Anar"
        b = "Yusif"

        a = "Yusif"
        b = "Anar"
        l = ",".join(sorted([a,b]))
        l = "Anar,Yusif"
        """     

        if a > b:
            # ['sweets', 'trousers', 'tomatoes', 'beans', 'fabric', 'date fruit', 'soap', 'water', 'coffee']
        
            sim = jaccardSimilarity( [cleanup(i) for i in people[a]], [cleanup(i) for i in people[b]] )
            if sim > 0:
                print(a + "|" + b, sim)
        #    results.append( a + b )


"""
Mahmizər Həsənova Anar Əhmədov 0.15384615384615385
Mahmizər Həsənova Həbibə Məmmədli 0.07142857142857142
Lalə Məmmədli Anar Əhmədov 0.06666666666666667
Yusif Ağasalamlı Lalə Məmmədli 0.07142857142857142
Ləman Rəhimli Lalə Məmmədli 0.07142857142857142
"""