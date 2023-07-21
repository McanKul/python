import json

data =[
    {
    "uername":"McanKul",
    "firtname":"Mehmetcan",
    "Surname":"kul"
    },
    {
    
    "uername":"destroyer61",
    "firtname":"Muzaffer",
    "Surname":"Sarımehmet"

    }

]


# with open("user.json","w",encoding="utf-8")as file:
#     json.dump(data,file,ensure_ascii=False,indent=2)

user = {
    
    "uername":"destroy",
    "firtname":"ali",
    "Surname":"veli"

}
with open("user.json","r",encoding="utf-8")as file:
    bilgi = json.load(file)



with open("user.json","w",encoding="utf-8")as file:
    bilgi.append(user)
    json.dump(bilgi,file,ensure_ascii=False,indent=2)

