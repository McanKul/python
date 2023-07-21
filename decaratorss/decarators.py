# def greating(name):
#     print("hello",name)

# print(greating)

# def outer(num1):
#     print("outher")
#     def inner_increment(num1):
#         print("inner")
#         return num1 + 1
#     num2 = inner_increment(num1)
#     print(num1)
#     print(num2)

# outer(10)

def factoriyel(number):
    if not isinstance(number,int):
        raise TypeError("number are required")
    if not number>= 0:
        raise ValueError("sayı 0 dan büyük olmalı")
    def inner_factoriyel(number):
        if number <= 1:
            return 1
        
        return number * inner_factoriyel(number-1)
    
    return inner_factoriyel(number)

try:
    print(factoriyel(10))

except ValueError as a:
    print(a)