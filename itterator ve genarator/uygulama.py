

# def kareal():
#     sayi = 1
#     while True:
#         yield sayi ** 2
#         sayi += 1

# kare = kareal()
# print(next(kare))

# def fibonacci(k):
#     liste = []
#     n = 1 
#     while n<=k:
#         if n <= 2:
#             liste.append(1)
#         else:  
#             ekleme = liste[n-2] + liste[n-3]
#             liste.append(ekleme)
#         n +=1
#     return liste

# fibona = fibonacci(100000)
# for i in fibona:
#     print(i)
        


def fibonacci():
    n = 1
    temp = 1
    yeni = 1
    temp1=1
    while True:
        
        if(n <= 2):
           yield 1 
        else:
            yield yeni + temp1
            temp1 = yeni
            
            yeni += temp
            temp = temp1

        n += 1    
         
            
    
fibo = fibonacci()


for i in fibo:
    print(i)



# import sys 
# liste = [i*2 for i in range(1000000)]

# gen = (i*2 for i in range(1000000))

# print(sys.getsizeof(gen))
# print(sys.getsizeof(liste))