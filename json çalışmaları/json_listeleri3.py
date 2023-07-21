db = {
    "users":{
          "McanKul": 
          {
            "firstName": "Mehmetcan",
            "lastName": "Kul"
         },
        "Destroyer61": {
            "firstName": "Muzaffer",
            "lastName": "SarÄ±mehmet"
         }
    },
    "products":
    {
    "1":
    {
        "pruductName":"Iphone X",
        "price":8000

    },
    "2":
        {
            "pruductName":"Iphone 12",
            "price":10000
        }
    }
}

import json
# with open("db.json","w",encoding="utf-8") as file:
#     json.dump(db,file,ensure_ascii=False,indent=2)

with open("db.json",encoding="utf-8") as file:
    db = json.load(file)

# print(db["users"])

db["products"].update({
    "3":
        {
            "pruductName":"Iphone 13",
            "price":15001
        }
})





with open("db.json","w",encoding="utf-8") as file:
    json.dump(db,file,ensure_ascii=False,indent=2)