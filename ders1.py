
#!cls() veya clear() ile terminal temizlenir
#! mesaj

# print("hello world")
# print("hello","world")
# print("hello"+"world")
# print("mesut                  son")
# print("senn"+"seven")
# print("selam ben Python öğreniyorum! 
#         sdasdsadasasd") #! hata

# print("""selam
# ben
# python
# öğreniyorum""")

# print("selam benim yaşım"+23) #!HATA

# mesaj = "selam ben python öğreniyorum"
# print(mesaj) #?değişkeni print içerisinde yazdırmak

# yas =23
# print(yas)

#?sep() değişken aralarına koyulacak karakterleri belirler
# print("frontend","backend","designer",sep="//")

#*adınızı soyadınızı ve yaşınızı bir değişkende tanımlayınız
# Tanımlama = "mesut songur 23"

#*bu 3 değişken arasına "**" atınız
# print("mesut","songur",23,sep="**")


#?end() mesaj sonuna eklenecekler anlamına gelmektedir
# print("selam ben ",end="mehmet")

"""selam ben mehmet yaşım 23"""
#*2 farklı değişken oluşturunz isim ve yas
# isim = "mesut"
# yas = " 23"

#*end kullanarak yukardaki çıktıyı alınız
#?end bir birleştirme işlemidir int() str() yorum satırına toplanamaz
# print(isim,end=yas)

#! f ile değer çekmek
#?backtick (js)

# isim = "ahmet"
# soyisim = "coban"
# yas = 23
# print(f"Selam Benim adım {isim},soyadım {soyisim},yaşım {yas}")

#!yorumm satırları
#? yorum satırları # ile kullanılır

"""
ÇOKLU 
YORUM
SATIRI

"""

#! FORMAT METODU
#?formaat metodu yer tutucu aanlamına gelir ve değişkenlerin yerlerini tutar
# print("selam benim  {ad}".format(ad="mehmet"))

# renk = "mavi"
# test = "kırmızı"
# print("benim en sevdiğim renk {1} {0}".format(renk,test)) #!{} 0 1 mantığı duruma göre değiştirme

# print("{0} {2} {3} {1}".format("ben","python","öğrenmek","istiom"))

#! Değişken oluşturma
#?Değişken oluşturma kuralları

#? değişkenler sayı ile başlamaz
# 1sayi = 20 

#?değişkenler arasında boşluk bırakılmaz ve özel karkater bulunmaz
# benim adım = "mehmet"
# benim&%!^^="mehmet"

#!doğru değisken oluşturma yönetmleri
giriIsim = "mehmet"
girilenisim = "mehmet"
girilen_isim = "mehmet"

#!değişken atama işlemler
isim = "mehmet" #?string()
yas = 23 #?int()

#!Çoklu değişken oluşturm
# say1,say2,say3 = 5,10,15
# print(say3)

#?küsürat sıfırlama düzeltme
# sinav1,sinav2,sinav3 = 50,60,50
# ortalama = int((sinav1+sinav2+sinav3)/3)
# print(ortalama)

# a=b=c=d="kırmızı" #? \n satır başı anlamına gelmektedir
# print(f"{a} \n{b} \n{c} \n{d}")












