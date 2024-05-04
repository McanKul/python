import csv

def add_user(name,surname):
    with open("user.csv","a",encoding="utf-8") as file:
        csv.writer(file).writerow([name.capitalize(),surname.capitalize()])
        

def get_users():
    with open("user.csv",encoding="utf-8") as file: 
        okunmus = csv.DictReader(file)
        for i in okunmus:
            print(i)
        

def get_user(name,surname):
    n=2
    isim = name.capitalize()
    soyisim = surname.capitalize()
    with open("user.csv") as file:
        okunus = csv.DictReader(file)
        for i in okunus:
            if i["Name"] == isim:
                    if i["Surname"] == soyisim:
                        print(f"kullanıcı {n}. satırda")
                        break
                    else:
                    
                        n +=1
            else:
                n += 1

        



##enumerate()#içine gönderilen bir şey indeksler

#yazdirmaişleminde nasıl boşluk bırakmaması gerektiğini öğrenmem gerekiyor çok önemli

def update_user(name,surname,yeni_name,*yeni_surname):
    n=2
    isim = name.capitalize()
    soyisim = surname.capitalize()
    liste = []
    with open("user.csv","r",encoding="utf-8") as file:
        okunus = csv.DictReader(file)
        for i in okunus:
            if i["Name"] == isim:
                    if i["Surname"] == soyisim.capitalize():
                        i["Name"] = yeni_name.capitalize()
                        i["Surname"] = yeni_surname
                        liste.append(i)
            else:
                liste.append(i)
    with open("user.csv","w",encoding="utf-8") as file:
        header= ["Name","Surname"]
        csv.DictWriter(file, header).writeheader()
        csv.DictWriter(file, header).writerows(liste)


def delete_user(name,surname):
    n=2
    isim = name.capitalize()
    soyisim = surname.capitalize()
    liste = []
    with open("user.csv","r",encoding="utf-8") as file:
        okunus = csv.DictReader(file)
        for i in okunus:
            if i["Name"] == isim:
                    if i["Surname"] == soyisim.capitalize():
                        continue
            else:
                liste.append(i)
    with open("user.csv","w",encoding="utf-8") as file:
        header= ["Name","Surname"]
        csv.DictWriter(file, header).writeheader()
        csv.DictWriter(file, header).writerows(liste)

        
update_user("safa","demirci","cafer")