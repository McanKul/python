
r = float(input( "daireninYarıCapı:")) # float veri yipine dönüştürüyor
print("dairenin çevresi:", 2*r*3.14)
print("ddairenin alanı: ",3.14*r**2)



x = float(input( "gidilen kilometre:"))
mil = x/1.609344
mil = round(mil, 3)
print("mil: " + str(mil))

print("Dairenin yarı çapı:")
r=float(input())
print("dairenin çevresi: "+str(2*3.14*r) + "  daireninalanı: "+str(3.14*r**2))


a = float(input())
b = float(input())
r = a*b
k = round(r, 1) # ondalık sayıları kaç basamağının gösterileceğini seçen fonksiyon
print(k)
