# try:
#     x = int(input("bir sayı giriniz"))
#     y = int(input("bir sayı daha giriniz"))
#     print(x+y)
# except:
#     print("bir hata oluştu")


# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x/y)
# except (ValueError,ZeroDivisionError)as i:
#     print("Y 0 olamaz")
#     print(i)
# except:
#     print("bilinmeyen bir hata oluştu")

# liste = ["1","2","5a","20b","abc","10","50"]
# i=0
# sayilar = []
# for i in liste:
#     try:
#        sayilar.append(int(i))
#     except ValueError:
#         continue
   
# print(sayilar)

# # while True:
    
# #     try:
# #         sayı = (input("bir sayı giriniz"))
# #         if sayı == "q":
# #             break
# #         else:
# #             int(sayı)
# #     except:
        
        
# #             print("lütfen bir sayı giriniz")
# #     else:
# #         break
# # # urun = {
# # #     "urunadi":"samsung galaxy s10"
# # # }
# # # def get(a,key):
# # #     try:
# # #         return a[key]
# # #     except:
# # #         return "none"
# # # print(get(urun,"urunadi"))

# # def colorize(text, color):
# #     colors = ("blue","red","white","black","orange")
# #     if type(color) is not str:
# #         raise TypeError("renk str olmalıdır")
# #     if type(text) is not str:
# #         raise TypeError("text str olmalıdır")
# #     if color not in colors:
# #         raise ValueError("geçersiz bir renk")
# #     print(f"{text} {color} renginde yazıldı")

# # try:
# #     colorize("5",)
# # except(TypeError,ValueError) as tp:
# #     print(tp)

# # # # def faktoriyel(a):
# # # #     a = int(a)
# # # #     if a<0:
# # # #         raise ValueError("negatid sayı giremezsiniz")
# # # #     carpim = 1
# # # #     for i in range(1,a+1):
# # # #         carpim *= i
# # # #     print(carpim)

# # # # for i in ["5",4,"10b","6"]:
# # # #     try:
# # # #         faktoriyel(i)
# # # #     except ValueError as e:
# # # #         print(e)

# def parolakontrol(parola):
#     turkce_karakterler = "ıİğüşöç"
#     for i in parola:
#         if i in turkce_karakterler:
#             raise TypeError("şifreniz türkçe karakter içeremez")

# a=1
# while a>0 :
#     parola = input("deneemk için şifre giriniz")
#     try:
#         parolakontrol(parola)
#     except TypeError as e:
#         print(e)
#     else: 
#         print("şifreniz uygundur")
#         break
        

 ##pdb isimlil kütüphaneyi cağırıp pdb.set_trace komutunu kullanarak kodun
 ##istediiğimiz yere kadar çalışması sağlayabiliriz
 ## l tüm komutları listeler n sonraki komutu çalıştırır p istenilen bir değişkenin içeriğini yazar c de kodu sonuna kadar çalıştırrı.

    



    

        
        
    

    
