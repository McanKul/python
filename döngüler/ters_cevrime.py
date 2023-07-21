# cumle = input("cümle giriniz ")
# kelimeler = []
# kelime_sayisi = 0;

# for harf in cumle:
#     if harf == " ":
#         kelime_sayisi+=1
#         print("bosluk var")
#     else:
#         kelimeler[kelime_sayisi]= kelimeler[kelime_sayisi] + cumle(harf)

# liste = ["abc"]
# yeniliste = ["a", "b", "c"]

# yeniliste = yeniliste[0] + "d"
# print(yeniliste)
cumle = input("cümle giriniz ") +" "
kelimeler = []

ananas = ""
for harf in cumle:
   
    if harf == " ":
        kelimeler.append(ananas)
        ananas = ""  
    else:
        ananas = ananas + harf
i=0
terscumle=""
while i < len(kelimeler):
    terscumle = terscumle + kelimeler[len(kelimeler)-1-i] + " "
    i += 1
print(terscumle)

for k in range(len(terscumle)-1):
    print(terscumle[k],end="")