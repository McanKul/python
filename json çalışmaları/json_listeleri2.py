data = {
    "McanKul":{
    "firstName":"Mehmetcan",
    "lastName":"Kul"
    },
    "Destroyer61":{
    "firstName":"Muzaffer",
    "lastName":"Sarımehmet"
    }
}
import json
with open("users.json","w",encoding="utf-8") as file:
    json.dump(data,file,ensure_ascii=False,indent=2)

with open("users.json","r") as file:
    users = json.load(file)

# print(users["McanKul"])

users.update({ 
    "fena61":
     {
        "firstName": "sena",
        "lastName": "sarıt",
        "age":19
     } 
  })

with open("users.json","w",encoding="utf-8") as file:
    json.dump(users,file,ensure_ascii=False,indent=2)

users.pop("fena61")

with open("users.json","w",encoding="utf-8") as file:
    json.dump(users,file,ensure_ascii=False,indent=2)