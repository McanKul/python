class Product:
    def __init__(self,name,price) -> None:
        self.name = name
        if price>0:
            self._price = price
        else:
            raise ValueError("ürün fiyatı negatif olamaz")
    @property #parantez kullanmayarak dışardan değer atamayı engellemeye yönelik
    def price(self):
        return self._price
    @price.setter # = ile değer ataması yapmayı sağlar gibi füşünebilir
    def price(self,value):
         if value>0:
            self._price = value
         else:
             raise ValueError("ürün fiyatı negatif olamaz")
        
    # def set_price(self,value):
    #     if price>0:
    #         self._price = price
    #     else:
    #         raise ValueError("ürün fiyatı negatif olamaz")

    # def get_price(self):
    #     return self._price

p = Product("iphone 12",9000)
print(p.price)