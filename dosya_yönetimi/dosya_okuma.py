#"r" (read) okuma. dosya konumda yoksa hata verir
#"w"(write)yazma modu , dosya konumda yoksa oluşturur., dosya içeriğini siler vve yeniden oluşturur.
#"a"(append) ekleme. dosya konnumda yoksa oluşturur.
#"r+" hem okuma hem yazma modunu açar ,dosya konumda yoksa hata verir

# with open("c:/Users/mehmetcan kul/OneDrive/Masaüstü/çalışmalarım/python/dosya_yönetimi/ananas.txt","r",encoding="utf-8") as dosya:
#     # print(dosya.read(10))
#     # print(dosya.tell())
#     # print(dosya.read())
#     for i in dosya:
#         print(i,end="")


# import os
# f = os.path.abspath("ananas.txt")
# print(f)

# with open("newfile.txt","w",encoding="utf-8") as dosya:

#     dosya.write("ananas ister misin o zama git al\n")
#     dosya.write("bakkaldan ananas aldırdım\n")


#     print(dosya)

# with open("newfile.txt","r",encoding="utf-8") as dosya:
#     print(dosya.read())

# with open("newfile.txt","a",encoding="utf-8") as file:
#     file.seek(0) #etkilemez sondan ekleme yapar
#     file.write("dördüncü satır\n")

# with open("newfile.txt","r+") as file:
#     file.read()
#     file.write("yeni satır\n") #seççilenn yerden ekleme yapar

# with open("ananas.txt","a") as file:
#     file.write("6-bmw")

# with open("ananas.txt","r+") as file:
#     markalar = file.read()
#     markalar = "1-toyata\n" + markalar
#     file.seek(0)
#     file.write(markalar)

with open("ananas.txt","r+") as file:
    markalar = file.readlines()
    markalar.insert(2,"3-renaılt\n")
    print(markalar)
    file.seek(0)
    for i in markalar:
        file.write(i)
    #file.writelines(markalar) for döngüsünde yaptığımız şeyle aynı işi yapar


with open("ananas.txt") as file:
    print(file.read())