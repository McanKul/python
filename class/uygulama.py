class Newdict(dict):
    def __repr__(self):
        print("repr metodundan mesaj var")
        return super().__repr__()
    
    def __missing__(self,key):
        print("olmayan key bilgisi istiyorsunuz")

    def __getitem__(self,key):
        print("bir elemanı çağırıyoesunuz")
        return super().__getitem__(key)
    
    def __setitem__(self,key,value):
        print("listeye eleman ekliyorsunuz")
        return super().__setitem__(key,value)
    
    def __contains__(self,item):
        print("eleman arıyamazsınız")
        return super().__contains__(item)
    
data = Newdict({"first":"Mehmetcan","last":"kul"})
print(data)
print(data["age"])

print("first" in data)