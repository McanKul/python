
msg = "giden gitmiştir gittiği gün bitmiştir"
print(msg)
a=len(msg)             # karakter sayısı gösteren fonksiyon
print(msg[0:5])        # belirlenen string dizinin içinde aralık seçme
print(msg[::-1])       # 3. sayı keliimeleri atlayarak yazmayı sağlar negatif kullanılırsa tersten alır
print(msg[-20:-1])     # en sağa göre kordinat yazma


name = "mehmetcan"
surname = "kul"
age = 19
print("my name is {} {}. I'm {} years old".format(name,surname,age)) # .format string serinizin içine belirlediğiniz değişkenleri ekler
print("my name is {1} {0}. I'm {2} years old".format(name,surname,age))#parantezlerin içine hangi terim geleceğini seçebilirsin seçmezsen  sırayla yazar
# aynı terimi birden fazla paranteze yazabilirsin
 
a = 10/9
print("result:{0:0.5}".format(a))# round fonksiyonundaki gibi ondalık kısmı yuvarlatabiliriz
print(f"my name is {name} {surname}. I'm {age} years old")# formot fonksiyonu en kısa kullanımı

website = "http://www.sadıkturan.com"
kursadı = "python dersleri: sıfırdan ileri seviye python programlama"
print(len(kursadı))
print(website[7:10])
karaktersayısı=len(website)
print(website[karaktersayısı-3:karaktersayısı])
print(kursadı[:15],kursadı[-15:])
print(kursadı[::-1])
print("abc"*3)
"""
"""
msg="benim adım Mehmetcan KUL"
a= msg.upper() #tüm harfleri büyük harfle yazar
b= msg.lower() # tüm harfleri küçük harfle yazar
c= msg.title() #her kelimenin baş harfini büyük yazar
d= msg.capitalize() #cümlenin ilk harfini büyük yazar.

e= msg.islower() #eğer başına is gelirse o komutu soru olarak sormuş olur true false sorusu
f= msg.strip() #boşlukları kaldırır
h= msg.split() # kelimeleri seçilen referanstan böler 
g= "-".join(msg) # seçilen ifadeyle kelimeleri birleştirir veya arasına ekler
ı= "".join(h) # dizilerri seçilen ifadeyle birleştirir
k= msg.index("Mehmetcan") # seçilen ifadenin kaçıncı indekste başladığını gösterir
# msgtartwith("") cümlenin başladığı harfi sorar true false şeklinde cevap verir
l= msg.replace("Mehmetcan","Mcan")# seçilen birinci ifadenin yerine ikinci ifadeyi yazar
print(g)

# k=msg.casefold()	#Converts string into lower case(küçük harfe çevirir)
# kcenter("-")     #Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Converts the elements of an iterable into a string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning

print("  hello world".strip()) 
print("www.sadıkturan.com".strip("w.moc"))
# print("kurAdı".lower())
# print("website".count("a"))
print("website".startswith("www"), "website".endswith("com"))

print("hello world".replace("world", "there"))
print("MCAN".center(50,"!"))
print("MCAN".ljust(50,"!"))
print(len("merhaba dünya"))