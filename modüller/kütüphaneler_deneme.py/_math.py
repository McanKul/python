import math

# # help dir ile kütüphanedeki fonksiyonlara bakabilriz
# print(math.sqrt(10))

# print(help(math.sqrt))

# print(math.factorial(19))

import random

# x = random.random()
# print(x)
# y = random.randint(1,100) 
# print(y)

# #.shuffle liste karıştırır 
# #.choice listeden rastgele seçim yapıyor
# #.sample listeden istenilen eleman kadar rastgele seçim yapıyor
from datetime import datetime

# # simdi = datetime.now()
# # year = simdi.year
# # month = simdi.month
# # print(month)

# # tamtarih = datetime.ctime(simdi)

# # bilgi = datetime.strftime(simdi,"%Y" " %X") #datetime diye googledan aratırsan detaylı olarak hangi harf ne işe yarıyor öğrenebilirsin
# # print(bilgi)
# t = "15 April 2023 23:45:30"
# ananas = datetime.strptime(t, "%Y %B %Y %H:%M:%S")
# print(ananas) # olmadı neden bilmiyom .:((
#     #timedelta gün eklemek için kullanlır

import os
print(dir(os))
# operating sistem konutları kullanmak için kullanılır baya iş yapar 
#os.path.abspath() bize dossyanın dizisini verir
#os.path.exsist() dossya var mmı yok mu onu sorgular

import re
 # str ifadeler içinde arama yapmak için kullanılabilir en basit tabiriyle
