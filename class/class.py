# #class

# class Ogrenci:
#     #method
#     #attribute
#     pass

# ogrenci= Ogrenci()
# print(ogrenci)

#init

# # # # class Product:
# # # #     def __init__(self, name, price):
# # # #         self.name = name
# # # #         self.price = price
# # # # p1 = Product("samsung s10", 2000)
# # # # p2 = Product("ıphone 10", 3000)

# # # # print(p1.name, p2.name)

# class Comment():
#     def __init__(self, username, text, likes, dislikes):
#         self.username = username
#         self.text = text
#         self.likes = likes
#         self.dislikes = dislikes


# y1 = Comment("ananas","abi iyi video",3,5)
# y2 = Comment("destroyer_muzaffer","abi yok etceksin",10,3)
# y3 = Comment("s2imle100lesh","güzelmiiş",100,200)
# y4 = Comment("chan","anans gibi",50,2)
# y5 = Comment("muhharrrem ali","efsane olmuş",20,30)

# yorumlar = [y1,y2,y3,y4,y5]
# for i in yorumlar:
#     print(f"{i.username}: {i.text}")

# # class Person():

# #     #yapıcı metotlar
# #     def __init__(self,name,surname,year):

# #         #object atributes
# #         self.name = name
# #         self.surname=surname
# #         self.year = year
# #     # instance method
# #     def intro(self):
# #         return f"benim adım {self.name} ve soyadım {self.surname}"

# #     def calculate_age(self):
# #         return f"yaşınız: {2023 - self.year}"

# # p1 = Person("Mehmetcan","Kul",2003)

# # print(p1.calculate_age())

# class BankAccount():
#     def __init__(self,owner):
#         self.owner = owner
#         self.balance = 0.0
    
#     def deposit(self,deposito):
#         self.balance = self.balance + deposito
#         return f"yeni bakiyeniz {self.balance}"
    
#     def withdraw(self,nakit):
#         if nakit > self.balance:
#             return "yeterli bakiyeniz bulunmamakta"
#         else:
#             self.balance = self.balance - nakit
#             return f"yeni bakiyeniz: {self.balance}"

# p = BankAccount("mehmetcan kul")
# p.deposit(600)
# print(p.withdraw(500))
# print(p.owner)


# # class User():

# #     active_user = 0
    
# #     def __init__(self,name,surname,age):
# #         self.name = name
# #         self.surname = surname
# #         self.age = age
# #         User.active_user +=1
    
# #     def logout(self):
# #         User.active_user -= 1 
# #         return f"{self.name , self.surname} uygulamadan çıkış yaptı"

# # print(User.active_user)
# # p1 = User("mehmetcan","kul",20)
# # p2 = User("sena","sarı",19)
# # print(User.active_user)
# # p2.logout()
# # print(User.active_user)


class Pet():
    cinsler  = ["kedi","köpek","kuş"]
    def __init__(self,isim,cins):
        if cins not in Pet.cinsler:
            raise ValueError(f"{cins} bir pet değildir")
        self.isim = isim
        self.cins = cins

boncuk = Pet("boncuk","kedi")
pasa = Pet("pasa","köpek")
mavis = Pet("mavis","kuş")
Pet.cinsler.append("balık")
#classdaki mantık normaldeki global ve local valu sistemine benzemekte

print(mavis)






