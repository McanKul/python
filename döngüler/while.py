import random
# sayılar = [2,5,7,8,9,10,43,56,68,95,117,120,150]

# i= 0 
# while (i<len(sayılar)):
#     print(sayılar[i])
#     i += 1

# while sayılar :
#     print(sayılar.pop())

# c = int(input("başlangıç sayısını giriniz"))
# b = int(input("bitiş sayısını giriniz"))
# i=c+1
# while c<i<b:
#     if i % 2==1 :
#         print(i)
#     i += 1

# i=100
# while i>0 :
#     print(i)
#     i-=1

# sayılar = []

# while len(sayılar)<5 :
#     x = int(input("bir sayı giriniz"))
#     sayılar.append(x)

# sayılar.sort()
# print (f"sayıların sıralanışı {sayılar}")


urunler=[]
kufurler =["it","eşek","kaka","çiş","bok böceği"]
agir_kufurler =["bakkalda ananası saldırttığım","am böreği","gitine pushladığım","ızdırabını siktiğim","göt lalesi"]
kufur_sayaci = 0

x = int(input("kaç tane ürün gireceksiniz"))
i = 0
while i<x :
    
    name=input("ürün adını giriniz ").lower()
    fiyat=(input("ürün fiyatını giriniz "))
    while not fiyat.isdigit():
        kufur_sayaci+=1
        if kufur_sayaci < 4:
            fiyat = input(f"lütfeen sayı girirniz {kufurler[random.randint(0,len(kufurler)-1)]}")
        else:
            fiyat = input(f"lütfeen sayı girirniz {agir_kufurler[random.randint(0,len(agir_kufurler)-1)]}")
        print(f"Kufür sayıınz = {kufur_sayaci}")
    int(fiyat)
    
    k = {"Ürün adı":name,"Ürün fiyatı":fiyat}
    urunler.append(k)
    i +=1
while len(urunler)>0:
    print(urunler.pop())




# isim ="mehmetcan"
# for harf in isim:
#     if harf=="m":
#         continue
#     print(harf)


# isim ="mehmetcan"
# for harf in isim:
#     if harf==isim[6]:
#         break
#     print(harf)