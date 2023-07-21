# # sayılar = [1,2,3,4,5]
# # s = "ananas aldırdım."

# # # for i in sayılar:
# # #     print(i)   #bunu kendimiz yapalım #for döngüsü kendisi iteratore çevirerek işimizi hallediyor

# # iterator = iter(sayılar)
# # print(iterator)
# # # print(next(iterator))
# # # print(next(iterator))
# # # print(next(iterator))
# # # print(next(iterator))
# # # print(next(iterator))


# # def my_for(iterable, func):
# #     iterator = iter(iterable,)
# #     while True:
# #         try:
# #             sayi = next(iterator)
# #             func(sayi)
# #         except StopIteration:
# #             break


# # my_for(s,print)

class Counter:
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start<= self.stop:
            x=self.start
            self.start += 1
            return x
        else:
            raise StopIteration
            return False
    

# for i in Counter(10,20):
#     print(i) # kendinn yap altta

k = iter(Counter(2,20))

while True:
    try:
        print(next(k))
    except:
        break