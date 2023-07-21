# # r = list(range(10,100,11)) #başlangıç, bitiş, kaçar kaçar #negatif sayı kullanılıp ters çevrilmek istersen önce büyük sayı yazılmalı
# # print(r)
# for i in range(10):
#     print(i)

# markalar = ["bmw","meredes","opel"]
# obj1 = enumerate(markalar)
# print(list(obj1))
# print(type(obj1))

# for i,b in enumerate(markalar,1) : # yukarıda verilen markalar listesini indexiyle beraber yazmaya yarıyor virgülden sonra koyulan sayı ilk sayının numarasını sorar
#     print(i,b)

# liste1= [1,2,3,4,5]
# liste2=["a","b","c","d","e","f"]
# print(list(zip(liste1,liste2)))#iki listeyi birleştirir ikiden fazlada birleştirebilir

# for i in zip(liste1,liste2):
#     print(i)
"""
for a in range(1,11):
    print(f"{a}ın tablosu:")
    for b in range(1,11):
        print(f"{a} x {b} = {a*b})
çarpım tablosu
"""





# asalsayı = True
# sayı = int(input("asal olup olmadığını öğrenmek için sayı giriniz: "))
# if sayı==1:
#    asalsayı = False

# for k in range(2,sayı):
#     if (sayı % k) == 0 :
#         asalsayı = False
#         break# çok önemli işlemi kolaylaştırmak adına

# if asalsayı:
#     print(f"{sayı} sayısı asaldır")
# else:
#     print(f"{sayı} sayısı asal değildir")
        
import random


sayı = random.randint(1,101)
i=1
oyun = input("bir oyun oynamak ister misin").lower()
if oyun =='evet':
    k = int(input("kaç tane hak istiyorsunuz"))
    while not 5<=k<=10:
        k = int(input("üzgünüm en az 5 hak alabilirsin en fazla 10. \n lütfen tekrar kaç tane hak istediğinizi giriniz."))
    tahmin = int(input("aklımdan bir sayı tuttum tahmin edebilir misin"))
    while i<k :   
        if tahmin==sayı:
            break
        elif tahmin<sayı:
            print("daha yüksek bir sayı")
            tahmin = int(input("tekrar tahmin et"))
        else:
            print("daha küçük bir sayı")
            tahmin = int(input("tekrar tahmin et"))
        i += 1

    t = 100/k
    if tahmin!=sayı:
        print(f"üzgünüm {i} seferde sayıyı bulamadın hiç puan alamadın. Sayı {sayı} idi")
    else:
        print(f"Tebrikler {i} seferde sayıyı buldun. {100-(i-1)*t} puan aldın")
elif oyun=="hayır":
    print("sen kaybedersin")