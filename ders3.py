
#!len
#?uzunluk kontrolü anlamına gelir (lenght) sadece yazısal ifade alabiliriz
# myList = ["a","b","c","d","e","f"]
# print(len(myList))

# myList = ["a","b","c","d","e","f"]
# myListen = len(myList)
# print(myListen)

# metin = "selam ben metin"
# metinLen =len(metin)
# print(metinLen)

# elemanlar = {
#     "isim":"mehmet",
#     "meslek":"caycı"
# }
# elemanlarLen = len(elemanlar)
# print(elemanlarLen)

#!eval
#?Açık inputa girilen değerleri kullanıcı python kodu ile alabilir
# x = "print(25)"
# eval(x)

# y = "print(len('mehmet coban'))" 
# eval(y)

# x = eval("2+5")
# print(x)

#?Max Min Değer Bulma
# degerler = max(-23,65,87,98,11,34,76) 
# print(degerler)

#!Input()
#*kullanıcı dan değer almak için kullanılır
#*alınan değerler stringdir
# input("adınız nedir :")

#?inputdan gelen kodu int cevirme
# girilenDeger =int(input("lütfen bir değer giriniz : "))
# print(f"girilen deger{girilenDeger}")
# print(type(girilenDeger))

#*Dışarıdan gelen bilgileri ekrana yazdır (ad soyisim doğum tarihi)
# isim = "mahmut"
# soyisim = "peksoz"
# dogum_tarihi = "20.01.2000"
# print(f"isim : {isim} soyisim : {soyisim} doğum tarihi : {dogum_tarihi}")

#*kullanıcınını girdiği sayının 3 katını yazdırın
# girilenDeger = int(input("lütfen değer giriniz : "))
# girilenicarp = girilenDeger*3
# print(girilenicarp)

#*kulanıcısının girdiği sayının karesini alan progaram
# girilenDeger = int(input("lütfen değer giriniz : "))
# girileniKare = girilenDeger*girilenDeger
# print(girileniKare)

#*girilen 3 sınavın ortalamasını alan uygulamayı yazzınız
# sınav1=int(input("lütfen ilk sınavınızı giriniz :"))
# sınav2=int(input("lütfen ikinci sınavınızı giriniz :"))
# sınav3=int(input("lütfen ücüncü sınavınızı giriniz :"))
# total = (sınav1+sınav2+sınav3)/3
# print(total)

#*kenar uzunluğu ve yüksekliği girilen üçgenin alanının hesaplayan programı yazınız (k*h)/2   
# kenar_uzunlugu = int(input("kenar uzunluğunu giriniz : "))
# yükseklik = int(input("yüksekliği giriniz : "))
# hesap = (kenar_uzunlugu * yükseklik)/2
# print(hesap)

#*kısakenarın ve uzun kenarın girildiği dikdörtgenin çevresini hesaplayan programı yazınız (kk+uk)*2
# kk = int(input("kısa kenar uzunluğunu giriniz : "))
# uk = int(input("uzun kenar uzunluğu giriniz : "))
# total = (kk+uk)*2
# print(total)

#*vizenin %40 finalin %60 alınarak ortalamayı ekrana yazdıran program
# vize = int(input("vizeyi giriniz : "))
# final = int(input("finali giriniz : "))
# sonuc = (vize*0.4)+(final*0.6)
# print(sonuc)

#*kullanıcıdan alınan kullanıcı adının karakter uzunluğunu bulunuz
# ka = input("kullanıcı adınızı giriniz : ")
# print(len(ka))

#*kullanıcı dan iki deger alınız 1. alt değer 2.üssü dğeri
# x = int(input("alt deger giriniz : "))
# y = int(input("üssü deger giriniz : "))
# total = x+(x*y)
# print(total)

#*kullanıcıdan alınan kilo ve boy ile vücut kitle indeksini hesaplayınız//  kilo/(boy*boy)
# kg = int(input("Kilonuzu Giriniz : "))
# boy = float(input("Boyunuzu Giriniz : "))
# kendeksi = int(kg*(boy*boy))
# print(kendeksi)

#*kullanıcıdan alınan bir python kodunu çalıştırınız
# yazi = input("Kod giriniz : ")
# print(yazi)

#* kullanıcıdan maaşını ve zam oranını alınız. hesaplama yaparak yeni zamlı maaşı verin
# maas = int(input("maaş giriniz : ")) 
# zam = int(input("zam oranını giriniz : "))
# yeni_zam = (maas*zam/100)
# print(yeni_zam)

#*kullanıcıdan 3 farklı değer alınız bu değerleri ekrana yazdırırken aralarına *** işareti koyunuz
 #*mesela ahmet***mehmet***rojin
# bir = (input("İlk değeri giriniz : "))
# iki = (input("İkinci değeri giriniz : "))
# üc = (input("ücüncü değeri giriniz : "))
# print(bir,iki,üc,sep="***")

#*klavyeden yarıçapı girilen dairenin alanını ve çevresini hesaplayınız.
#*kullanıcıya alanı ve çevreyi verini 
#* cevre = 2 * pi * yarıcap
#* alan = pi * yaricap * yaricap

# yc = int(input("girilen yarıçap : "))
# cevre = (2*3*yc)
# zone = (3*yc*yc)
# # tot = ("cevresi"{cevre}"alanı"{zone})
# print(f"alanı : {zone}",f"cevresi : {cevre}")

#*kullanıcın girdiği isimi 10 kere ekrana yazdırınız (for kullanmadan)
# girilenDeger = input("Girilen değer 10 kere yazılacaktır :")
# print((girilenDeger + "\n") * 10)


#!zor örnek
#* kullanıcın girdiği meyve isimlerini (virgülle ayrılmış) bir array içerisinde toplayın

# ki =input("giriniz : ")

# ki = ki.split(",")

# print(ki)

#!zor örnek çözümü
#* kullanıcın girdiği meyve isimlerini (virgülle ayrılmış) bir array içerisinde toplayın
# kullaniciIsimleri = input("Kullanıcı Adlarını Girinzi :")

# kullaniciIsimleri = kullaniciIsimleri.split(",")

# print(kullaniciIsimleri[0])
