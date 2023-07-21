import module

ananas = module.sayi

elma = module.ögrenci["isim"]

toplam = module.topla(30,40)

print(ananas,elma,toplam)

import module as an
#module an ismiyle çağırıyor yani modulden bilgi kullancağımız zaman an kullanabilir burada

from module import ogrenci

#moduleden özellikle tek bir eleman çağırmaya yaraıyor, özellikle bir eleman çağırdığımız için tekrardan modulun ismini kullanmaya gerek yok
#  * senbolu kullanılırsa tüm elemanlar tek tek çağırılır yinede modul ismini kullanmaya gerek yoktur