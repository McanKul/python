from functools import wraps

def log_data(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        print(f"çağırsığınız metot ismi: {fn.__name__}")
        print(f"çağırsığınız metot bilgisi: {fn.__doc__}")
        return fn(*args,**kwargs)
    return wrapper

@log_data
def add(x,y):
    """fonksiyonunuz 2 sayıyı toplar"""
    return x+y

print(add(10,20))

print(add.__name__)
print(add.__doc__)