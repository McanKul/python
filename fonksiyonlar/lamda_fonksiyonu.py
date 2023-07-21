
carpma = lambda a: a*3 
print(carpma(34))


sayilar =[1,3,4,5,7]
sonuc = list(map(lambda sayi: sayi ** 2, sayilar))
print(sonuc)


yaslar = [5,12,19,23,56]
sonuc = list(filter(lambda x: x>=18, yaslar))
print(sonuc)

#all fonkisyonu kendisine gelen liste içerisinde 
# tüm elemanaların true değerine sahip se true değilse
#   false değeri verir 
# any fonkisiyonu için bir tane true olması yeterlidir

#sorted fonksiyonu listeleri sıralamak için kkullanılır
#.sort methodundan daha kapsamlıdır.

