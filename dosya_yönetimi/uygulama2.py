import os

def urunler(urun,fiyat):
    with open("urunler.txt","a",encoding="utf-8") as file:
    
        file.write(f"ad: {urun} fiyat:{fiyat}\n")
        
        
def güncelleme(dosya_adı,eski_isim,yeni_isim):

    with open(dosya_adı,"r+",encoding="utf-8") as file:
        
        yazı = file.read()
        yeni = yazı.replace(eski_isim,yeni_isim)
        file.seek(0)
        file.write(yeni)
        file.truncate() #imlecin geldiği son noktadan sonra kalan her şeyi siler 
        #değer vererek ondan sonra kaç karatker silinceğini seçebilirsin

        


güncelleme("urunler.txt","samsang galaxy s11","iphone 14 pro max")
