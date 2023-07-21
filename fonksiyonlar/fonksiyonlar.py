
# a = 20
# b= 30

# # def toplam():
# #     print(a+b)

# # toplam()

# def toplam():
#     return a + b  -- verilen ifadeye işlemeden işlenebilir yapıp bırakır --

# print(toplam())

# def simdi():
#     import datetime
#     return datetime.datetime.now().year

# dogumyılı  = int(input("Doğum yılınızı giriniz"))

# def yashesapla():
#     return simdi() - dogumyılı
# print(yashesapla())

# # # def selamla(isim):
# # #     return f"merhaba {isim}"
# # # print(selamla("yaren"))

# # # def toplam(a,b):
# # #     return a+b
# # # print(toplam(10,30))

# # # def yas(dogumyılı):
# # #     return 2022 - dogumyılı
# # # print(yas(2003))

# # # def emeklilik(dogumyılı,isim):
# # #     k = yas(dogumyılı)
# # #     emekli = 65-k
# # #     if emekli>0:
# # #         return f"sayın {isim} emekliliğinize {emekli} yıl kaldı"
# # #     else:
# # #         return f"sayın {isim} emekli olabilirsiniz"
# # # sonuc= emeklilik(2003,"Mehmetcan")
# # # print(sonuc)


# def tekrarlama(tekrar,i):
#     for i in range(i):
#         print(tekrar)
# tekrarlama("wow",10)

# # # def alan(a,b):
# # #     return f"Dikdörtgenin alanı {a*b}\ndildörtgenin çevresi  {2*(a+b)}"
# # # print(alan(10,2))


# def kura():
#     import random
#     return random.choice(["yazı","tura"])
# print(kura())







# def asalsayı(a,b):
#     asalsayılar = []
    
#     for k in range(a+1,b):
#         asal = True
#         for c in range(2,k):
#            if (k%c)==0:
#                asal=False
#                break
#         if k==1:
#             asal=False
#         if asal==True:
#             asalsayılar.append(k)
#     return asalsayılar
# print(asalsayı(17,100))

# # def bolum(a):
# #     return [i for i in range(1,a+1) if a%i==0]

# # print(bolum(8))   

# # def usalma(a,b=2):
# #     return a**b
# # print(usalma(2))
# # # eğer fonksiyona gönderilen parametre bir değere eşitlenirse fonksiyon yazılırken yazılma şartı yoktur 
# # # ama yazılırsa yazılan değere dönüşür sadece birinci fonksiyona değer atılamaz aynı anda ikisine ya da en sondakine atılması gerekiyor
# # def toplam(a,b):
# #     return a+b
# # def cıkarma(a,b):
# #     return a-b
# # def islem(a,b,fonk=toplam):
# #     return fonk(a,b)
# # print(islem(8,4,cıkarma))
# # #burada islem fonksiyonunda fonk ile uygulanacak fonksiyonu seçiyoruz toplam ataması yapoldıpı için hiçbir şey yazılmazsa toplama yapılır


# liste = [10,20,30]
# def toplam(sayılar):
#     topla =  0
#     for i in sayılar:
#         topla += i
#     return topla
# print(toplam(liste))

# ##bunun yerine şunu yapabilirsin

# def toplama(*args): # buradaki yıldız kaç tane değer girileceği belli değil demek
#     sonuc=0
#     for k in args:
#         sonuc += k
#     return sonuc

# print(toplama(56,78,87,1))

# def kimlik(**dictinary): # ** dictinary veri tipini fonksiyonda kullanmamızı sağlar
#     print(dictinary)

# kimlik(adı="mehmetcan")

# # def kimlik(**kwarg):
# #     for k in kwarg.values():
# #         print(k)

# # kimlik(ad="mehmetcan",soyad="kul",yas=19)

# def karsılastırma(a,b):
#     if a>=b :
#         return a
#     else:
#         return b

# print(karsılastırma(14,67))


# # # def hesaplama(anan):
# # #     dicti= {

# # #     }
# # #     harfler = ("-".join(str(anan).strip("1234567890*,."))).split("-")
# # #     k=1
# # #     for i in harfler: 
# # #         if i in dicti:
# # #             dicti[i] +=1
# # #         else:
# # #             dicti[i]=k
# # #     dicti.pop(" ")
# # #     return dicti

# def hesaplama(string):
#     return {k: string.count(k) for k in string}

# print(hesaplama("dafhbuvnıWOPĞQ"))
# # # bananas= input("hesaplanmasını istediğiniz kelime sayısını giriniz")
# # # print(hesaplama(bananas))

# def kontrol(blue):
#     if "blue" in blue:
#         return True
#     else:
#         return False

# liste = ["red","black"]
# print(kontrol(liste))
anan = input("lütfen cümle giriniz").split( )
for i in anan:
    print(i)
