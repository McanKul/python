# import time

# def speed_test(fn):
#     def wrapper(*args,**kwargs):
#         start_time = time.perf_counter()
#         print(f"{fn.__name__} metodu çalışıyor")
#         result = fn(*args,**kwargs)
#         end_time = time.perf_counter()
#         run_time = end_time - start_time
#         print(f"geçirilen süre :{run_time}")
#         return result
#     return wrapper
                
                
# @speed_test               
# def sum_gen():
#     return sum((x for x in range(100000000)))

# @speed_test
# def sum_list():
#     return sum([x for x in range(100000000)])

# print(sum_gen())
# print(sum_list())

def dec_do_twice(count):
    def do_twice(func):
        def wrapper(*args,**kwargs):
            for _ in range(count):
                func(*args,**kwargs)
            
        return wrapper
    return do_twice

@dec_do_twice(count=3)
def hello():
    print("hello")

@dec_do_twice(count = 5)
def greet(name):
    print("hello "+name)

hello()
greet("ali")