""""
sayılar= []
for i in range(10):
    sayılar.append(i)


liste = [1,34,54,13]
for k in liste:
    sayılar.append(k*2)
print(sayılar)
"""
# #bunun yerine aşşağıdaki gibi yapılabilir
# #(expression for item in liiste)
# liste = [1,34,54,13]

# sayılar= [i**2 for i in range(10)]
# sayılar=[i%10 for i in liste]
# print(sayılar)

# liste = [1,34,54,13]
# for k in liste:
#     if k<40:
#         print(k//3)
# # bunun yerine
# # expression for item in liste if koşul
# bolum = [k//3 for k in liste if k<40]
# bolum = [k//3 if k<40 else "40 den büyük" for k in liste]
# # eğer if else kullanılacaksa başta yoksa sonda kullanılır
# print(bolum)

# obj = [ (x,y) for x in range(3) for y in range(3)]
# print(obj)


# kalan0 =  [ k for k in range(100) if k%12==0]
# print(kalan0)

string = ("hello world 12345")
rakamlar = [rakam for rakam in string if rakam.isdigit()]#***********isdigit
print (rakamlar)