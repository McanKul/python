class User():

    active_user = 0
    @classmethod
    def display_active_user(cls):
        return f"{cls.active_user} tane aktif kullanıcı var"

    @classmethod
    def from_string(cls,data_str):
        name,surname,age = data_str.split(",")
        return cls(name,surname,age)

    
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age
        User.active_user +=1
    
    def logout(self):
        User.active_user -= 1 
        return f"{self.name , self.surname} uygulamadan çıkış yaptı"

print(User.display_active_user())
p1 = User("mehmetcan","kul",20)
p2 = User("sena","sarı",19)
print(User.display_active_user())

deneme = User.from_string("ali,çakmak,35")
print(deneme.name)
