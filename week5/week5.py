
import matplotlib.pyplot as plt
import numpy as np


randomdata = np.random.normal( 15, 10, 100 ) # will be explained later!!
randomdata2 =  np.random.normal( 45, 10, 100 ) # will be explained later!!

randomdata = np.concatenate( [randomdata, randomdata2] )

data = [18,18,18,20,22,23,23,24,24,25,26,27,27,27,27,27,28,29,29,29,29,29,29,30]
#! plt.hist( data ) # histogram

print(randomdata)

# 4.05261497e+01 
# e+01 = x 10 = power(10, 1) 
# 40.52

#! plt.hist(randomdata)
#! plt.show()


a = [9,10,11]  # ===> 10 (9+10+11) / 3 = 10  #!! DEGERLER ORTALAMAYA COK YAKIN
b = [5,10,15]  # ===> 10 (5+10+15) / 3 = 10  #!! DEGERLER ORTALAMAYA YAKIN SAYILIR 
c = [0,10,20]  # ===> 10 (0+10+20) / 3 = 10  #!! DEGERLER ORTALAMAYA UZAK!!!

# Ortalamalari AYNI olan farkli veriler olabilir!!!!


#! a == abs(9-10) + abs(10-10) + abs(11-10) = 2, very small value
#! c == abs(0-10) + abs(10-10) + abs(20-10) = 20, very large value


# mean = ortalama = normal = average = MERKEZ NOKTA, center point
# standard deviation = radius = how wide the data is spread



sample = [0,22.75,0,0,0,0,0,0,419.5,0,0,0,0,0,249.5,6,5.75,16,0,2.5,362.25,0,546.25,0.25,0.75,0,0.75,4.75,41.5,0,9.5,0,0,14,0,97.25,0,0.75,8.5,0.25,100.75,0,0,0,0,3,0,0,232.75,0,0,31.75,9.5,264.75,8.75,0,0,0,0,0,0,53.75]

#! plt.hist(sample)
#! plt.show()


sample = [2000,2500,2250,3000,3000,2500,3500,2750,2750,2750,3000,2500,2500,2500,1500,1500,1500,1750,1900,2000,2200,2400,2500,6700,7500,7500,10000]
sample = [0,22.75,0,0,0,0,0,0,419.5,0,0,0,0,0,249.5,6,5.75,16,0,2.5,362.25,0,546.25,0.25,0.75,0,0.75,4.75,41.5,0,9.5,0,0,14,0,97.25,0,0.75,8.5,0.25,100.75,0,0,0,0,3,0,0,232.75,0,0,31.75,9.5,264.75,8.75,0,0,0,0,0,0,53.75,0,1444.75,0,1.75,0,0,0,0,0,0,1.25,126,0,52.75,74,9,0,163.25,65.25,0,872.25,13,4.75,85,0,10.25,0,0,0,0.75,0,0,1.5,30.5,0,0,38,0,483.5,51.5,161,162.5,0,0,21.5,71.25,370,25.5,0,3.75,0,102.75,102,39,0.25,92.75,0,4.25,0,5.25,227.25,666.5,4,0,0,759,0,7,0,8.25,29.75,0,43.25,12,72,0,0,21.75,1,343.25,0,0,0,0,0,107,0,146.25,0,15,0,182.75,0,0,110.6666667,60.25,0,0,0,0,78.5,0,0,0,8.5,58.25,30,44.75,7,109.75,128.5,120.5,0,231.75,63.5,156.5,1948.75,0,215.75,0,140.5,32.25,0,0,3,0,49.75,54,99,5.5,0,0.75,0,62.5,284,0,0,186,0,0,1094.25,0,7.5,0,144,18.5,97,536.75,31.5,4.75,289.5,0,154,49,0,0,4.5,0,90.75,50,0,0,0,2.75,0,459.25,0,114.5,0,16,0,0,0,0,1055.5,0,0,20.75,323.75,0,0,0,443.25,0,64,0,648.25,0.25,0,0,0,0,0,0,21.5,59.75,36,6.5,237.75,23.75,5.75,248,0,608.75,0,52.75,88,0,13.5,229.25,250.25,0,6.25,71,1306.25,0,0,45.25,1.75,0,0,0,80,0,0,0,0,0,30.25,0,0,0.75,4.75,0,0,532,458.25,0,0,198.25,0,0,0,0,33,47.25,510,0,0,94.75,0,214,0,1565.25,0,0]
sample = [0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,0,1,1,0,1,1,1,0,1,1,1,0,1,0,0,1,0,1,0,1,1,1,1,0,0,0,0,1,0,0,1,0,0,1,1,1,1,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,1,1,0,1,1,1,0,1,1,0,1,1,1,1,0,1,0,0,0,1,0,0,1,1,0,0,1,0,1,1,1,1,0,0,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1,0,0,1,0,1,0,1,1,0,1,1,1,0,0,1,1,1,0,0,0,0,0,1,0,1,0,1,0,1,0,0,1,1,0,0,0,0,1,0,0,0,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,0,1,1,0,0,1,0,1,1,1,1,0,1,0,1,1,0,0,1,0,0,1,0,1,0,1,1,1,1,1,1,1,0,1,1,0,0,1,0,1,1,0,0,0,0,1,0,1,0,1,0,0,1,0,0,0,0,1,0,0,1,1,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,1,0,1,1,0,1,1,1,0,1,1,1,0,0,1,1,0,0,0,1,0,0,0,0,0,1,0,0,1,1,0,0,1,1,0,0,1,0,0,0,0,1,1,1,0,0,1,0,1,0,1,0,0,0,0,0,1,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,1,1,1,1,1,0,1,1,1,0,1,0,1,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,1,0,1,0,1,1,1,0,0,0,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,0,0,1,1,1,1,1,0,1,1,0,0,1,1,0,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,0,0,1,0,1,0,0,0,1,1,1,0,0,0,1,1,1,1,1,0,1,1,1,0,1,0,0,0,0,1,1,0,1,1,1,1,1,0,1,0,1,0,0,1,0,1,0,0,0,0,0,1,1,1,1,0,1,0,1,0,1,1,0,0,0,1,1,1,1,0,0,0,0,0,0,1,0,1,1,0,1,0,1,0,1,0,0,0,0,1,0,0,1,1,0,1,0,1,0,1,0,1,1,0,0,1,1,1,0,0,1,0,1,0,1,0,0,0,1,1,0,0,1,0,1,0,0,1,0,0,1,1,1,1,1,1,0,1,0,1,1,0,1,1,1,1,0,1,0,1,1,0,1,1,0,1,1,0,1,0,1,1,1,1,0,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,1,1,0,1,1,1,0,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,0,0,1,0,0,1,0,0,0,0,1,0,1,1,0,1,1,1,0,1,1,1,1,0,0,0,0,1,0,0,1,1,1,1,1,1,0,0,1,0,1,0,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,0,1,0,0,1,1,0,1,1,1,1,0,1,0,0,1,0,0,0,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,1,1,0,0,0,0,1,0,0,1,1,0,1,1,0,1,0,1,1,1,0,1,1,1,1,1,1,0,0,1,1,1,1,1,0,1,0,1,1,1,0,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,1,0,1,1,0,1,1,0,0,1,0,1,1,1,1,1,1,1,0,1,1,1,0,0,1,0,0,0,1,1,0,1,1,0,0,1,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,0,1,0,1,1,1,0,1,0,0,1,0,0,0,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,0,1,1,1,0,1,1,1,1,0,1,1,0,0,0,0,1,0,1,0,1,0,1,0,1,0,0,1,1,0,0,0,1,1,1,1,0,1,1,0,0,1,0,0,1,1,0]

sample = [10,11,11,10,10,10,9,9,10,11,12,8,8,8,12,12,10,10,10,10]
# plt.hist(sample)
# plt.show()


import time
import random
sample = np.random.normal(20, 5, 200)
sample = list(sample)
firstmean = np.mean(sample)
firstmedian = np.median(sample)

for i in range(200):
    plt.clf()
    plt.cla()    
    sample.append( random.randint(1500,2000) )
    plt.hist(sample)
    plt.pause(0.2)
    print("MEAN:", np.mean(sample), "MEDIAN:", np.median(sample), "FMEAN", firstmean, "FMEDIAN", firstmedian)

plt.show()
    







