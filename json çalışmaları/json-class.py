class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

p1 = Product("samsung S10",5000)
p2 = Product("samsung S11",6000)

products = [p1.__dict__,p2.__dict__]

import json

with open("urunler2.json","w",encoding="utf-8") as file:
    json.dump(p1.__dict__,file,indent=2)


with open("urunler2.json") as file:
    data = json.load(file)

