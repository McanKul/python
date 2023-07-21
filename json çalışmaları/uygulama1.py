import json

def kayıt_gir(urunadi,fiyat,satistami,kategori):
    urun = {
        "Urun Adı":urunadi,
        "Fiyat":fiyat,
        "Satış Durumu":satistami,
        "Kategori":kategori
    }
    with open("urunler.json","a",encoding="utf-8") as file:
        json.dump(urun,file,ensure_ascii=False,indent=2)

# kayıt_gir("samsung s10",9000,True,"Telefon")

def urunleri_getir():
    with open("urunler.json","r",encoding="utf-8") as file:
        dosya = json.load(file)
        for i in dosya:
            print(dosya[i])

urunleri_getir()