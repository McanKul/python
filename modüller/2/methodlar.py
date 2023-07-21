def urunekle(a,b,c):
   dicti = {

   }
   dicti[b]=c
   a.append(dicti)

def urunguncelle(a,b,c):
    for i in range(0,len(a)):
        if c is not a[i][b]:
            a.pop(i)
            dicti = {

            }
            dicti[b]=c
            a.append(dicti)

def urunlerigeitr(a):
    print(a)
            
