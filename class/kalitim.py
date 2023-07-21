

class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("person nesnesi türetildi")

class Student(Person):
    def __init__(self, name, surname, age, number):
        Person.__init__(self, name, surname, age)#alternatig kullanım teacher kısmında mevcuttur
        self.number = number
        print("student nesnesi üretildi")
    
    def study(self):
        print(f"{self.number} numaralı öğrenci ders çalışıyor")
   

class Teacher(Person):
    def __init__(self, name, surname, age,brans):
        super.__init__(name, surname, age)
        self.brans = brans
        print("Teacher nesnesi üretildi")
    
    def teach(self):
        print(f"{self.brasn} dersi anlatılıyor")
   

P1 = Person("ali","çakmak",35)
s1 = Student("mehmetcan","kul",20,1209)

print(P1.age,s1.age)