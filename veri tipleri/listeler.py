# liste = ["samsungs5","samsungs6","samsungs7","samsungs8"]
# print(len(liste))
# print(liste[0],liste[3])
# liste[0] = "samsungs9"
# if "samsungs6" in liste:
#     print("içindedir")
# print(liste[-3])
# print(liste[0:2])
# liste[-2:] = "samsungs9","samsungs10"
""""
liste1 = ["1","2","3"]
liste2 = ["4","5","6"]
liste3 = ["7","8","9"]
toplamliste = [liste1,liste2,liste3]
# print(toplamliste)
for a in toplamliste:
   kalan1 =  a[0]
   kalan2 = a[1]
   kalan0 = a[2]
  # print(f"3 e böşündüğünde 1 kalanı veren {kalan1},\n 3 e bölündüğünde 2 kalanı veren {kalan2}, \n3 e tam bölünen {kalan0}")
   k1 = kalan1
   k2 = kalan2
   k0 = kalan0

  # print("3e tam bölünenler {},\n3e bölününce 1 kalanı verenler {}\n3ebölününce 2 kalanı vereneler{}".format(k0,k1,k2))

sayılar = [1,2,3,4,5]
harfler = ["a","b","c","d","e"]
print(min(sayılar))
print(max(harfler))
sayılar.append(19) #dizinin sonuna terim ekler
sayılar.insert(2,19)#birinci sayı terim eklenecek yerin kordinatını gösterir.
sayılar.pop() #diziden terim siler isteğe bağlı indeks no eklenebilir
sayılar.remove(2)#belirli bir ifadeyi siler
sayılar.sort#küçükten büyüğe sıralar
sayılar.reverse#sıralamayı ters çevirir
print(sayılar.index(5))
"""
""""
isimler= ["ada","yiğit","beril","hasan"]
yıllar = [1998,2000,1998,1997]
isimler.append("mert")
isimler.insert(0,"ayşe")
isimler.remove("yiğit")
#print(isimler.index("yiğit"))
if "beril" in isimler:
    print("beril listede var")
isimler.reverse
isimler.sort
yıllar.sort()
yıllar.reverse
print(yıllar)
telefonlar = list("iphonexs, iphone10")
enbuyuk= yıllar[len(yıllar)-1]
enkucuk  =  yıllar[0]
print(enbuyuk,enkucuk)
print(yıllar.count(1998))
yıllar.clear
"""
"""
# a,b,c = input("favori 3 markanız nedir? Lütfen tek tek giriniz"),input(),input()
# markalar = [a,b,c]

markalar= []
markalar.append(input("bir marka giriniz"))
print(markalar)

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

# list = (1,2,4)
# print(type(list))# tuple veri tipi liste gibi ama değiştirilemez



plakalar = {"trabzon":61,"istanbul":34}
plakalar["izmir"]= 35 #ilk ifade bizim atadığımız index olarak düşünülebilir

ogrenciler= {
  150:{
   "adı":"mehmetcan",
   "soyadı":"kul",
   "yaş":18,},
  210:{
    "adı":"safa",
    "soyadı":"değil",
    "yaş":19
  }}
# x=int(input("öğrenci numarısını giriniz"))
# print(ogrenciler[x]["adı"])
print(ogrenciler)
"""
# x=input("id")
# y= input("ürün adı")
# z=input("ürün fiyatı")
# ürünler = {x:{y:z}}
# ürünler={}


# id=input("id")
# isim=input('isim')
# fiyat=input("fiyat")
# ürünler[id]={isim:fiyat}

# id=input("id")
# isim=input('isim')
# fiyat=input("fiyat")
# ürünler[id]={isim:fiyat}

# id=input("id")
# isim=input('isim')
# fiyat=input("fiyat")
# ürünler[id]={isim:fiyat}
# print(ürünler)

# karakterler={'1': {"adı":'dila', "fiyatı":'10lira'}, '2': {"adı":'yaren',"fiyatı": '200lira'}, '3': {"adı":'kevser', "fiyatı":'100lira'}}
# print(karakterler[input("ürün idsini 
# opelobj={
#   "marka":"opel",
#   "model":"corsa",
#   "yıl":2020

# }
# for x in opelobj.values():
#   print(x)

# for x,y in opelobj.items():
#   print(x,y)
# oyuncular={
#   1:{
    
#     "name":"Cristiano Ronaldo",
#     "yearofbirt":1985,
#     "nationality":"portugal",
#     "history":"juventus"
#   },
#   2:{
   
#    "name":"lionel messi",
#    "yearofbirth":1987,
#    "nationality":"Argantine",
#    "history":"Barceleno"}
#   }

# # oyuncular.pop(2)
# # print(oyuncular[2])
# id= int(input("oyuncu id sini giriniz"))
# print(oyuncular.get(id))


meyveler = {"kiraz","kavun","elma"}# sets liste tipinde sıra yoktur indexlenemezler 
# .union iki farklı sets birleştirir
# x=10
# y=19
# x=y
# print(x,y)

print(meyveler.pop())