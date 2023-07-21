# def usalma(number):

#     def inner(power):
#         return number**power
#     return inner
    
# two = usalma(2)
# print(two(6))

# tree = usalma(3)
# print(tree(4))
    

# # def yerki_sorgula(page):
# #     def inner(role):
# #         if role == "Admin":
# #             print("{0} rolü {1} sayfasına ulaşabilir".format(role,page))
# #         else:
# #             print("{0} rolü {1} sayfasına ulaşamaz".format(role,page))
# #     return inner
# # user1 = yerki_sorgula("Product edit")
# # user1("Admin")

# # user2 = yerki_sorgula("Product edit")
# # user2("user")

def islem(islem_adı):
    def toplam(*args):
        toplam= 0
        for i in args:
            toplam +=1
        return toplam
    
    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim
    
    if islem_adı == "toplam":
        return toplam
    elif islem_adı=="carpma":
        return carpma
    
toplama = islem("toplam")
carpma = islem("carpma")

print(toplama(1,2,3,4,43))
print(carpma(3,5,6,7))
