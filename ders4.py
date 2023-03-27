
#!string eleman ayırma
text = "selam ben mehmet"
# print(text[:5]) #*saymaya 1 den başlıyor ilk 5 elemanı alır (selam) noktayı sağ tarafa atarsak sağdan sayar eğer 2 rakam ortasına koyarsak aralıkta ki değerleri alır
# print(text[:-2]) #*sondan 2 elemanı çıkarır (selam ben mehm)
# print(text[6:9]) #*aralıkda ki değerleri alır (ben)
# print(text[-3:]) #* (met)
# print(text[::4]) #* 4'er atlayarak değer alma (smnh)

#!String metodları
#?lovwer() (girilen metni kücük harflere dönüştürür)

# text = "MEHMET ÇOBAN"
# text = text.lower()
# print(text)

#?casefold() (girilen metini küçük harflere dönüştürür)
#*bant genişliği olarak lowerdan daha güçlüdür

# text = "MESUT SONGUR"
# text = text.casefold()
# print(text)

#?upper() (girilen metini büyük harflere dönüştürür)
# text = "mhmet coban"
# text = text.upper()
# print(text)

#?strip() (metin başındaki ve sonundaki boşlukları siler)
# text = "        selam ben mehmet coban          "
# text = text.strip()
# print(text)

# text = "!*?selam ben mehmet coban !*?"
# text = text.strip("*!?")
# print(text) #*özel karakterleri silmek için kullanılır , boş karakterleri temizlemez içinie girilen değerleri de temizleyebiir

#?istitle() (is title kelimelerin baş harflerine bakar

# text = "Mehmetcoban"
# textKontrol = text.istitle()
# print(textKontrol)

#*ÖRNEK
#*KULLANICIDAN BİR KULLANICI ADI ALINIZ!
#*eğer kullanıcı adınınn baş harfi büyükse hg değilse hatalı kullanım yazdırınız 

# kk = input("Kullanıcı adınızı giriniz : ")
# kkontrol = kk.istitle()
# if kkontrol == True: print("hg") 
# else: print("bb")

#*Count() (metin içerisinde belirttiğimiz kelimenin kaç adet olduğunu döndürürür)
# yazi = "selam ben yazılım çok severim. Çünkü benim işim yazılım"
# yaziKont =yazi.count("e")
# print(yaziKont)

#*countda belirtilen aralıklar cümle içerisinde nereden başlayıp nerede biteceğini belirtir
# text = "selam ben mehmet coban"
# textKont = text.count("e",10,len(text))
# print(textKont)

#?index () (girilen metin ya da karakterin index numarısını bize döndürür)
# text = "selam ben mehmet!"
# textindex = text.index("e")
# print(textindex)

#*İndex de aralık belirtmek
# text = "selam ben mehmet!"
# textKont = text.index("e",3,len(text))
# print(textKont)

#?Center() (metinde alınan değere göre bir ortalama işlemi yapar)
# metin = "neos yazilim"
# metin = metin.center(50)
# print(metin)
#*boşluklara değer atama
# text = "mehmet coban"
# text = text.center(50,"*")
# print(text)

#?split (verilen metini bize dizi olarak döndürür)
# girilenDegerler = input("Değerleri Giriniz : ")
# girilenDegerler = girilenDegerler.split(",")
# print(girilenDegerler)


















