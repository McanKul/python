def sayısay(max):
    sayi = 1
    
    while sayi <= max:
        yield sayi
        sayi += 1
    
genarator = sayısay(100)
# print(help(genarator))# iter ne next zaten mevcut buradan görebilirsin


# iterator = iter(genarator)
print(next(genarator))
print(next(genarator))
print(next(genarator))
print(next(genarator)) 
# next itaroturun olduğu yerden ilerii gitmeyi sağlar başa dönmez

for i in sayısay(29):
     print(i)


print(list(genarator))


genarator = (i for i in range(11)) #tuple veri tipi zaten genratordur