# def selamla(fn):
#     def wrapper():
#         print("hoş geldiniz")
#         fn()
#         print("görüşmek üzere")
#     return wrapper

# @selamla
# def gunaydın():
#     print("günaydın benim adım mehmetcan")


# def iyigunler():
#     print("hoş geldiniz")
#     print("iyi günler benim adım mehmetcan")
#     print("görüşmek üzere")


# gunaydın()
# #farklı kullanımlara göre parantez gerekebilir veya gerekmeyebilir bunu lğrenirken deneyerek yaptın biraz ama 
# #uğraşırsan her türlü bulursun çok zor değil

def do_twice(func):
    def wrapper_do_twice(*args,**kargs):
        return func(*args,**kargs),func(*args,**kargs)
        
        
    return wrapper_do_twice

@do_twice
def hello():
    print("hello")
hello()

@do_twice
def greet(msg):
    print("hello"+msg)
greet("world")

@do_twice
def return_greeting(name):
    print("greeting function")
    return f"hello, {name}"

print(return_greeting("ali"))

# harbi kafa sikiyormuş zor yani

