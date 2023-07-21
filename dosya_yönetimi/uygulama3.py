def not_gir():
    ad = input("öğrenci ismi: ")
    soyad = input("öğrenci soyad: ")
    not1 = input("not 1: ")
    not2 = input("not 2: ")
    not3 = input("not 3: ")
    with open("notler.txt","a",encoding="utf-8")as file:
        file.write(ad + " " + soyad + ":" + not1 + "," + not2 + "," + not3 +"\n")

def not_hesapla(satir):
    satir = satir[:-1] # önemli olabilir boşlukları atmak için kullanılıyor
    liste = satir.split(":")
    isim = liste[0]
    notlar = liste[1].split(",")
    ortalama = (int(notlar[0])+int(notlar[1])+int(notlar[2]))/3
    if 90 <= ortalama <=100:
        harf = "AA"
    elif 70<ortalama <90:
        harf = "bb"
    elif 50<ortalama<70:
        harf = "cc"
    else:
        harf = "ff"
    return isim + ":" + harf + "\n"
    

def ortalamarı_oku():
    with open("notler.txt","r") as file:
        for satır in file: # buradaki kullanım dikkat et satırları veriyor, readlinea gerek yok demekki
            print(not_hesapla(satır))

def notları_kaydet():
    liste = []
    with open("notler.txt","r") as file:
        for i in file:
            liste.append(not_hesapla(i))
        with open("sonuclar.txt","w",encoding="utf8")as file2:
            for i in liste:
                file2.write(i)





while True:
    islem = input("1-notları oku\n2- not gir\n3-notları kayıt et\n4- çıkış\n")
    if islem == "1":
        ortalamarı_oku()
        
    elif islem == "2":
        not_gir()
    elif islem == "3":
        notları_kaydet()
    else:
        break