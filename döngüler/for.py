# sayılar =[1,2,4,5,6,10]
# isimler = ["ali","ayşe","ahmet"]
# for i in sayılar:
#     print(i)
# for ad in isimler:
#     print(ad)

# liste = [(1,2),(3,4),(5,6)]
# for a in liste:
#   print(a[0])


# sayılar = [1,5,15,35,57,72]

# # for x in sayılar:
# #     if x % 5== 0:
# #         print(x)
# toplam=0
# for x in sayılar:
#     toplam = toplam + x
# print(toplam)

# for a in sayılar:
#     if a%2==0 :
#         print(a**2)


urunler = [
    {"name":"iphone 8","fiyat":"4000"},
    {"name":"iphone 8 plus","fiyat":"5000"},
    {"name":"iphone x","fiyat":"6000"},
    {"name":"iphone xr","fiyat":"7000"},
    {"name":"iphone 11","fiyat":"8000"},
    {"name":"samsung s10 8","fiyat":"6000"}]

# toplamfiyat=0
# for x in urunler :
#     toplamfiyat += int(x["fiyat"])
# print(toplamfiyat)

# for a in urunler:
#     if int(a["fiyat"])>=6000 :
#         print(a)

x = input("hangi marka telefon arıyorsunuz").lower()
for a in urunler:
    y = a["name"]
    z = a["fiyat"]
    if x is a["name"]:
        print(f"{y.capitalize()} fiyatı : {z}")
    elif x not in a["name"]:
         print(f"Maalesef {x.capitalize()} marka telefonumuz yok")
        