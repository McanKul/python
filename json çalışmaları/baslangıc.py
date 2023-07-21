import json
# # with open("person.json",encoding="utf-8") as file:
# #     data = json.load(file)

# # print(data)
# # print(data["hobies"])

# data = """
# {
#     "firtName":"Mehmetcan",
#     "lastName":"Kul",
#     "hobies":["Buz Pateni","Satranç","Film"],
#     "age":19,
#     "children": [
#         {
#             "firtName":"Reyna",
#             "age":4
#         }
#     ]   
# }

# """
# data = json.loads(data)
# print(data)

# # jsondan bilgi çekme




person = {
    "firtName":"Mehmetcan",
    "lastName":"Kul",
    "hobies":["Buz Pateni","Satranç","Film"],
    "age":19,
    "children": [
        {
            "firtName":"Reyna",
            "age":4
        }
    ]   
}

sonuc = json.dumps(person,ensure_ascii=False,indent=2)#ensure asci ile gelen bilgileri trkçe karakterleri korur
# print(sonuc)
# print(type(sonuc))
#dpsyaya bilgi yazarken dump uygulamadan alırken dumps
with open("person.json","w") as file:
    
    json.dump(person,file,ensure_ascii=False,indent=2)