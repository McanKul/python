liste = [1,2,3]


print(type(liste))

class Film:
    def __init__(self,baslik,yonetmen,sure):
        self.baslık = baslik
        self.yonetmen = yonetmen
        self.sure = sure
    def __str__(self):
        return f"{self.baslık} {self.yonetmen} tarafından yönetildi"
    
    def __repl__(self):
        return f"{self.yonetmen},{self.baslık}{self.sure},"

    def __len__(self):
        return self.sure
    def __del__(self):
        print("obje silindi")



f = Film("film adı","yonetmen",120)
print(str(liste))
print(str(f))
print(len(f))
