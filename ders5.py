
#!GÖNÜLLÜ ÖRNEKLER

#*market uygulaması!
#* bir adet dict oluşturunuz 
#* dict içerisine ürünler ve karşısında fiyatlar olsun
# urunler = {
#   "a":10,
#   "b":20,
#   "c":30,
#   "d":40,
#   "e":50
# }
# toplam = 0

# while True:
#     urun = input("Ney almak istersiniz : ")
#     if urun in urunler:
#         toplam += urunler[urun]
#     devam = input("Alışverişe devam mı? e/h ")
#     if devam == "h":
#         break

# print(f"Toplam alışveriş tutarı : {toplam}")

#*kullanıcıya ne almak istediğini sorunuz 
#* => a
#*alışverşişe devammı ? e/h
#* => e 
#*kullanıcıya ne almak istediğini sorunuz 
#* => b
#*alışverşişe devammı ? e/h
#* => h
#* a ürünün ve b ürünün toplamını yazıdırnız
#* => toplam alışveriş tutarı 30 TL


#!çekiliş
#*kullanıcıdan kullanıcı isimlerini virgülle ayrık bir şekilde isteniz
#*kaç adet kazanan olsun 
#* => 1
#*kaç adet yedek olsun
#* => 3
#*kazananları ve yedekleri yazıdırnız
#! kurallar
#*kazanan yedek olamaz
#*yedek olan kazamaz
#*kazanan ve yedek sayısının toplamı toplam kullanıcı sayısını geçemezzz!
# import random
# kullaniciGiris = input("kullanıcı isimlerini virgül ile ayırarak giriniz : ")
# kullaniciGiris = kullaniciGiris.split(",")
# kazananSay = int(input("Kaç kazanan olsun : "))
# yedekSay =int(input("kaç yedek olsun : "))
# if kullaniciGiris 

# kazananSay = random.sample(kullaniciGiris, kazananSay)
# yedekler = random.sample(kullaniciGiris, yedekSay)

# print("Kazananlar: ", kazananSay)
# print("Yedekler: ", yedekSay)

# print(kullaniciGiris)

# import random

# isimler = input("Kullanıcı isimlerini virgülle ayrılmış şekilde girin: ")
# isimler = isimler.split(",")
# kazanan_sayisi = int(input("Kaç adet kazanan olacak: "))
# yedek_sayisi = int(input("Kaç adet yedek olacak: "))

# kazananlar = random.sample(isimler, kazanan_sayisi)
# yedekler = []
# for isim in isimler:
#     if isim not in kazananlar:
#         yedekler.append(isim)
#     if len(yedekler) == yedek_sayisi:
#         break

# print("Kazananlar: ", kazananlar)
# print("Yedekler: ", yedekler)




#*Split 
# girilenKullanicilar = input("karakter giriniz : ")
# kullanicilarList =girilenKullanicilar.split()
# print(kullanicilarList)

# girilenKullanicilar = input("Kullancıları Giriniz : ")
# kullanciList = girilenKullanicilar.split(",")
# print(kullanciList)


#?lstrip()
#*metin içerisinde ilk karakteri siler

# text = "1323123213"
# text = text.lstrip("3")
# print(text)

#?endwith() (metin içerisinde metin sonunun ne ile bittiğinde bakmak için)
#*true ya da false döndürür

# text = "mehmet coban"
# text = text.endswith("n") #!true son harf
# print(text)

#?startwtih()

# text = "mehmet coban"
# text = text.startswith("n") #!false baş harf
# print(text)

#?replace() (metin içerisindeki değiştirmek istediğmiiz karakterlerde uygulanır)

# text = "selam ben mehmet"
# text = text.replace("ben","sen")
# print(text)

#*telefon numarasının başında 0 girildiğini silinmesini sağlayan yapı hazırlayalım
#? Benim Yaptığım
# phone = input("Telefon Numarasını Giriniz : ")
# phone = phone.lstrip("0")
# if phone == True:
#     print(phone)
# else :
#     print(phone)

#?2.yol
# phone = input("Telefon Numarasını Giriniz : ")
# phone = phone.replace("0"," ")
# print(phone)

#?Hocanın yaptığı
# girilenNo = input("giriniz : ")
# girilenNoKontrol = girilenNo.startswith("0")

# if girilenNoKontrol == True:
# girilenNo = girilenNo.replace("0",","1") #!1 koyunca ilk değeri kapsıyor replace olayı
#     print(girilenNo)

# girilenNo = input("Giriniz : ")
# girilenoKont = girilenNo.startswith("0")

# if girilenoKont == True:
#  girilenNo = girilenNo.replace("0","",1) #!sadece ilk sıfırı sil
# print(girilenNo)

#?isnumeric() (girilen metinsel değerlerin rakam olup olmdığına bakar)
#*true ya da false dönddürür
# text ="746486547"
# textKont = text.isnumeric() #*true
# print(textKont)

#*örnek (girilen telefon numarasında harf bulunması gerekmekte)
# text = input("Giriniz : ")
# tex = text.isnumeric()
# if tex == True:print("Doğru Kullanım")
# else:print("Yanlış kullanım")
    
#?find() (metinsel değerin index numarısını verir)

#*değer bulunmazsa -1 döndürür
#*find ile index arasındaki fark index bulmazsa hata döndürür find ise -1
 
# text = "mehmet"
# text = text.find("t")
# text = text.find("e",2,6)
# print(text)

#!Listeleri toplama birleştirme

# list1 = [1,2,3,4,5]
# list2 = ["a","b","c","d","e"]

# toplamList = list1 + list2
# print(toplamList[5])

#!lİSTE METODLARI
#?append (dizi sonuna bir eleman ekler)
# meyveler = ["a","b","c","d","e"]
# meyveler.append("şeftali")
# print(meyveler)

#*kullanıcıdan alınan bir ürünü listeyi ekleyin

# girienKul = input("Eklemek istediğiniz ürünü giriniz : ")
# meyveler = ["a","b","c","d","e"]
# meyveler.append(girienKul)
# print(meyveler)
#*dict içerisinde append kullanımı
# Kullanici ={
#     "isim":"ahmet",
#     "soyad":"soy",
#     "yaş":23,
# }

# GirilenDeger =input("Mesleğinizi Giriniz : ")
# Kullanici["meslek"] = GirilenDeger
# print(Kullanici)

#*var olan diziye kullanıcıdan aldığınız farklı bir diziyi ekleyin
# meyveler = ["elma","armut","karpuz","kivi"]
# yeniMeyveler = input("diğer meyveleri giriniz : ")
# yeniMeyveler = yeniMeyveler.split(",")
# meyveler.append(yeniMeyveler)
# # meyveler = meyveler + yeniMeyveler #?Ek seçenek appendsız
# print(meyveler[4][0])

#?insert() (ilk değeri nereye ekleneceği,ikinci değeri ne ekleneceği)
# myList = ["elma","armut","karpuz","kivi"]
# myList.insert(0,"test")
# print(myList)

#?remove() (listedeki elemanı siler)
# myList = ["test1","test2","test3","test4"]
# myList.remove("test1")
# print(myList)
# del myList[0] #?index numarasına göre silinir


































