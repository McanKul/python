# def dosya_kopyala(dosya_ismi,yeni_dosya_ismi):
#     with open(dosya_ismi,"r") as file:
#         kopya = file.read()
    
#     with open(yeni_dosya_ismi,"w",encoding="utf-8") as file:
#         file.write(kopya)

# dosya_kopyala("ananas.txt","ananascopied.txt")

# # def ters_cevir(dosya_ismi,yeni_dosya_ismi):
# #     with open(dosya_ismi,"r") as file:
# #         kopya = file.read()
        
# #     parca = "-".join(kopya).split("-")
# #     parca.reverse()

# #     with open(yeni_dosya_ismi,"w",encoding="utf-8") as file:
# #         for i in parca:
# #             file.write(i)
####alternatif olarak file.write(kopya[::-1])

# # ters_cevir("ananas.txt","sanana.txt")

# def bilgilendir(dosya_ismi):
#     with open(dosya_ismi,"r") as file:
#         satır_sayısı = len(file.readlines())
#         file.seek(0)
#         tumu = file.read()
#         kelime_sayısı = tumu.split(" ")
#         sayısı = len(kelime_sayısı)
#         karakter_sayısı = len("-".join(tumu).split("-"))
#     print(satır_sayısı)
#     print(sayısı)
#     print(karakter_sayısı)
# # boşluk ifadesini karakter saymak istemezsem .sprit metodu ile atılabilir
# bilgilendir("ananas.txt") 