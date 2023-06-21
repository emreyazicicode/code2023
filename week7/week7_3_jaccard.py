import sys
import numpy as np 
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

#: Imports
import pandas as pd
#: Set the path
path = "week7_Sales Transaction v.4a.csv"
#: Read the file
df = pd.read_csv(path, parse_dates=['Date'], nrows=50000)
#: For each customer pair [a,b] find the jaccard similarity
# ---> Create a dataframe of similarities
# ---> customer1, customer2, similarity [ if only greater than 0 ]
# ---> Create a different cleanup function to cleanup names


"""
lst = ['Emre YAZICI', 'Mahmizər Həsənova', 'Mədinə Abdulsəmədova', 'Adil Rəhimov', 'Rafiq Rafiqzadə', 'Anar Əhmədov', 'Minəxanım Hacımuradova', 'Riyad Əhmədov', 'Riyad Əbdürəhimov', 'Lalə Məmmədli', 'Ləman Rəhimli', 'Niyyət Rzayev']
import random
random.shuffle(lst)
team1 = lst[0:int(len(lst)/2)]
team2 = lst[int(len(lst)/2):]
print(team1)
print(team2)


team1 = ['Anar Əhmədov', 'Riyad Əbdürəhimov', 'Rafiq Rafiqzadə', 'Adil Rəhimov', 'Ləman Rəhimli', 'Niyyət Rzayev']
team2 = ['Lalə Məmmədli', 'Minəxanım Hacımuradova', 'Riyad Əhmədov', 'Emre YAZICI', 'Mahmizər Həsənova', 'Mədinə Abdulsəmədova']
"""



customer_products = {}
for customername, customerdata in df.groupby('CustomerNo'):
    #: Unique list of products for the customer customername
    pr = list(set(customerdata['ProductName'].tolist()))
    if len(pr) > 10:
        customer_products[ customername ] = pr


counts = []
for v in customer_products.values():
    counts.append(len(v))

print( np.mean(counts) )


similarities = pd.DataFrame(columns = ['a', 'b', 'sim', 'len-a', 'len-b'])
"""
for a in customer_products:
    for b in customer_products:
        if a > b:
            sim = jaccardSimilarity( [cleanup(i) for i in customer_products[a]], [cleanup(i) for i in customer_products[b]] )
            if sim > 0.50:
                similarities.loc[ len(similarities) ] = [
                    a, b, sim, len(customer_products[a]), len(customer_products[b])
                ]
                print(str(a) + "|" + str(b), sim, sim * (len(customer_products[a]) + len(customer_products[b])) / 83, len(similarities))

                if len(similarities) % 10 == 0:
                    similarities.to_csv("week7_similarities.csv")
"""

# 14877	14351
dfa = list(set(df[ df['CustomerNo'] == 14877 ]['ProductName'].tolist()))
dfb = list(set(df[ df['CustomerNo'] == 14351 ]['ProductName'].tolist()))

dfa.sort()
dfb.sort()

print('\033[92m', dfa[0:15], '\033[0m')
print('\033[94m', dfb[0:15], '\033[0m')


product_product_freq = {}

for g in df.groupby('TransactionNo'):
    
    print("=========================")
    products_in_this_transaction = list(set(g[1]['ProductName'].tolist()))
    
    if len(products_in_this_transaction) > 2 and len(products_in_this_transaction) < 50:
        print(products_in_this_transaction)
        for a in products_in_this_transaction:
            for b in products_in_this_transaction:
                if a > b:
                    key = a+"|"+b
                    if key not in product_product_freq:
                        product_product_freq[key] = 1
                    else:
                        product_product_freq[key] += 1



for p in product_product_freq:
    if product_product_freq[p] == 11 and p[0] == 'S':
        print(p, product_product_freq[p])


