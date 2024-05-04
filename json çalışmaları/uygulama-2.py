import json
import os

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}

        # load users from .json file
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists('kullanıcalar.json'):
            with open('kullanıcalar.json','r',encoding='utf-8') as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser = User(user['username'],user['password'],user['email'])
                    self.users.append(newUser)
            print(self.users)

    
    def register(self, user:User):
        
        self.users.append(user)
        self.savetoFile()
        print("kullanıcı oluşturuldu")

    def login(self,usernma,password):
        for user in self.users:
            if user.username == usernma and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user.username
                print("giriş yapıldı")
                break
    
    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print("çıkış yapıldı")

    def identity(self):
        if self.isLoggedIn:
            print(self.currentUser)
        else:
            print("herhangi bir giriş yapılmadı")




    def savetoFile(self):
        liste = []
        for user in self.users:
            liste.append(json.dumps(user.__dict__))
        
        with open("kullanıcalar.json","w") as file:
            json.dump(liste,file,indent=2)


repository = UserRepository()

while True:
    print("Menü".center(50,"*"))
    secim = input("1-Register \n2-login\n3-logout\n4-Identity\n5-exit")
    
    if secim == "5":
        break
    elif secim=="1":
        username = input("username: ")
        password = input("Pasword: ")
        email = input("email: ")

        user = User(username,password,email)
        repository.register(user)
    elif secim=="2":
        username = input("kullanıcı adı giriniz")
        password = input("şifre giriniz")
        repository.login(username,password)
    elif secim == "3":
        repository.logout()
    elif secim == "4":
        repository.identity()
    else:
        print("geçerli bir kout giriniz")
