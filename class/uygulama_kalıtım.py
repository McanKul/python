class User:
    active_user = 0
    def display_active_user():
        return f"şu anda {User.active_user} tane kullanıcı aktif"
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        User.active_user += 1

    def fullname(self):
        return f"{self.name} {self.surname}"

class Moderator(User):
    def __init__(self,name,surname,comunity):
        super().__init__(name,surname)
        self.comunity = comunity

u1= User("yağmur","Korkmaz")
m1= Moderator("mehmetcan","kul","computer since")

print(isinstance(m1,Moderator))