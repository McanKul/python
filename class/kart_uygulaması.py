class Kart():
    kartsayı = 0
    def __init__(self,tip,deger):
        self.tip = tip
        self.deger = deger
        Kart.kartsayı += 1
    
    def kartıgetir(self):
        return self.tip +" "+ self.deger
        #burada __repr__ kullanırsak da olur özel bir metot


class Deste():
    tipi = ["karo","sinek","maça","kupa"]
    degeri = ["A","2","3","4","5","6","7","8","9","10","J","Q","k"]
    deste = []
    
    for i in tipi:
            for k in degeri:
                deneme = Kart(i,k)
                
                deste.append(deneme.kartıgetir())
    
    def kartsayı():
         return Kart.kartsayı
    
    @classmethod
    def kartlarıkarıstır(cls):
         import random
         random.shuffle(cls.deste)
    
    @classmethod
    def kartlarıdagıt(cls,k):
         from random import sample
         if k > Kart.kartsayı:
              raise ValueError("elinizde o kadar kart yok")
         elif k < Kart.kartsayı:
              dagıtma = sample(cls.deste,k)    
              for i in dagıtma:
                   cls.deste.remove(i)
              
              Kart.kartsayı -= k
              return dagıtma
    @classmethod
    def kartatma(cls,k):
         cls.deste.remove(k)
         Kart.kartsayı -= 1
         
         
          
         
        
# Deste.kartlarıkarıstır()

print(Deste.kartatma("kupa A"))
print(len(Deste.deste))
print(Kart.kartsayı)







