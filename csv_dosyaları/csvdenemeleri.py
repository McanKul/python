import csv

# with open("urunler.csv") as file:
#     ananas = csv.reader(file)
#     for i in ananas:
        
#         if i[2] == "True":

#             print(i[0],i[1])


# with open("urunler.csv") as file:
#     ananas = csv.DictReader(file)
#     for p in ananas:
#         print(p)





# with open("cars.csv","w") as file:
#     ananas = csv.writer(file)
#     ananas.writerow(["marka","model"])
#     ananas.writerow(["toyota","yaris"])
#     ananas.writerow(["toyota","corolla"]) #arada bosluk koydu anlamadım

# with open("cars.csv","a") as file:
#     ananas = csv.writer(file)
#     ananas.writerow(["toyota","rav4"])

# with open("urunler.csv") as file:
#     okuma = csv.reader(file)
#     with open("yeni-urunler.csv","w") as file:
#         yazici = csv.writer(file)
#         for i in okuma:
#             yazici.writerow([p.upper() for p in i])

# with open("urunler.csv","r+") as file:
#     okuma = csv.reader(file)
#     yazici = csv.writer(file)
#     next(okuma)
#     products = [[p[0],float(p[1])*2,p[2],p[3],p[4]] for p in okuma]
#     print(products)
#     file.seek(0)
#     yazici.writerow(["ProductName","Price","IsPublished","Categorry","Rewiews"])
#     yazici.writerows(products) ##bir hata var ama anlamadım 



with open("urunler.csv","w") as file:
    headers = ["ProductName","Price","IsPublished","Categorry","Rewiews"]
    csv_writter = csv.DictWriter(file, headers)
    csv_writter.writeheader()
    csv_writter.writerow(
        {
        "ProductName": "iphone 6",
        "Price": "6000",
        "IsPublished": True,
        "Categorry": "Telephone",
        "Rewiews": 4.6
    })