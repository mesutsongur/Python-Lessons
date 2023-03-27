
#?count() (listedeki o elemandan kaç adet varsa sayısal olarak döndürür)
# mylist = ["html","css","js","python","html","react","html"]
# mylistCount = mylist.count("html")
# print(mylistCount)

#?reverse() (listeyi tersine çevirip yazdırır)
# mylist = ["html","css","js","python"]
# mylist.reverse()
# print(mylist)

#?extend (dizideki bütün elemanları diğer diziye atar)
# front = ["html","css","js"]
# back = ["django","c#","php"]
# front.extend(back)
# print(front)

#?sum() (dizi içerisinde rakamsal değerlerin toplamını döner)
# myList = [1,2,3,4,5,6,7,8,9]
# myListToplam = sum(myList)
# print(myListToplam)

# myList = ["1","2","3","4","5","6","7","8","9"]
# myListToplam = sum(myList)
# print(myListToplam) #!hata verir (sadece numeric ifadeler toplanır)

#?clear() (dizideki bütün elemanları siler)
# myList = ["1","2","3","4","5","6","7","8","9"]
# myList.clear()
# print(myList)

#?pop() (parametre alırsa index numarasına göre silme işlemi yapar)
#*pop değer almadığında son elemanı siler
# mylist = ["html","css","js","python"]
# mylist.pop(1)
# print(mylist)

#?sort() (listeyi küçükten büyüğe sıralar)
# myList = [20,15,24,78,10,67]
# myListNew = myList.sort()
# print(myList)

#*string olan diziyi alfabetik olarak A-Z'ye şeklinde
# mylist = ["html","css","js","python"]
# mylist.sort()
# print(mylist)

#*büyükten küçüğe sıralama için sorted methodu kullanılır
#*öncee liste küçükten büyüğe sıralanır,ardından
#*reverse true ile liste terse çevirilir ve büyükten küçüğe doğru sıralama yapılır
# myList = [11,99,22,42,12,67,32,78,23,1,4,77,99]
# test = sorted(myList,reverse=True) #*reverse cevirme
# print(test)

#!İF ELSE (KARŞILAŞTIRMA OPARETÖRLERİ (KAPI))
#*Reşit Uygulaması
# x = int(input("yaşınızı giriniz :"))
# if x >= 18:
#     print("reşitsiniz")
    
# else:
#     print("reşit değilsiniz")

#*kullanıcıdan alınan 2 sayının eşit olup olmadığı kontrol edilsin
# x = int(input("İlk rakamı giriniz : "))
# y = int(input("İlk rakamı giriniz : "))

# if x == y:
#     print("girdiğiniz sayılar eşit")

# else:
#     print("girdiğiniz sayılar eşit değil")
#*Ortalama geçtin kaldın
# x = int(input("1.rakamı giriniz : "))
# y = int(input("2.rakamı giriniz : "))

# if x+y >= 50:
#     print("geçtin cano")
# else:
#     print("kaldınız")
#*girilen iki sayının hangisinin büyük olduğunu bulunuz
# x = int(input("1. rakamı giriniz : "))
# y = int(input("2. rakamı giriniz : "))

# if x>y:
#     print("İlk girdiğiniz değer büyüktür")
# else:
#     print("ikinci giridiğiniz değer büyüktür")

#*girilen sayının tek mi çift mi olduğunu bulunuz
# x = int(input("Rakam giriniz : "))

# if x % 2 ==0:
#     print("çift")
# else:
#     print("tektir")

#*kullanııcdan yaptığı alışveriş fiyatını alınızı
# x = int(input("Alışveriş Tutarınızı Giriniz : "))
# kargo = 15
# if x >=100:
#     print(f"{x} kargo ücretsiz")
# else:
#     print(f"{x+kargo}")

#*üç sınav notunu giren öğrencinin
#*ort alındıktan sonra geçme durumu knotrol edilecektir
# x = int(input("İlk  Tutarınızı Giriniz : "))
# y = int(input("İkinci Tutarınızı Giriniz : "))
# z = int(input("Üçüncü Tutarınızı Giriniz : "))
# tot = (x+y+z)/3
# if x+y+z >= 50:
#     print("geçtiniz")
# else:
#     print("kaldınız")

#*kullanıcının girdiği vize ve final notlarının ort alınız
# x = int(input("Vize Tutarınızı Giriniz : "))
# y = int(input("Final Tutarınızı Giriniz : "))
# vf= (x+y)/2

# if vf >=50:
#     print("geçtiniz")
# else:
#     print("kaldınız")
#     z = int(input("Büt Tutarınızı Giriniz : "))
#     if (x+z)/2 >=50:
#         print("Geçtiniz")
#     else:
#         print("kaldınız")

#!Ödevler
#*girilen sayının kaç basamaklı olduğunu bulun

# girilenSayi = (input("Lütfen basamak değerini öğrenmek için rakam giriniz : "))

# if int (girilenSayi) > 0 :
#     print(f"girilenen sayinin basamak değeri" , len(girilenSayi) )
# elif int (girilenSayi) == 0 :
#     print("Girilen Sayının basamak değeri: 1")
# else :
#     print ("Girilen sayının basamak sayısı:",len(girilenSayi) - 1)
    #*eksili sayı çevirip ekrana vuruyor

#*100lük sistemde girilen notu 5lik sisteme çevirin (87 => 5)
#*1.yol
# girilenSayi = int((input("Lütfen 5'lik sistemde ki karşılığı için ortalamanızı giriniz : ")))

# if girilenSayi >=85:
#     print("Tebrikler geçtiniz ortalamanız :5")
# elif girilenSayi >=70:
#     print("Tebrikler geçtiniz ortalamanız :4")
# elif girilenSayi >=60:
#     print("Tebrikler geçtiniz ortalamanız :3")
# elif girilenSayi >= 50:
#     print("Tebrikler geçtiniz ortalamanız :2")
# else:
#     print("Büyük başarı göstererek kaldınız hayırlı olsun, ortalama : 1")



#*alınan iki sayının girilen harfe göre dört işlem yapan uygulamayı yazınız
#* örn =  toplama = t

# Sayi_1 = int(input("işlem yapılması için ilk sayıyı giriniz : "))
# Sayi_2 = int(input("işlem yapılması için ikinci sayıyıy giriniz :  "))
# Islem = input("Ne işlem yapmak istiyorsunuz giriniz (örn: toplama=t,çıkarma=c,bölme=b,çarpma=c)")

# if Islem == "t":
#     print(Sayi_1+Sayi_2)
# elif Islem == "c":
#     print(Sayi_1-Sayi_2)
# elif Islem =="b":
#     print(Sayi_1/Sayi_2)
# elif Islem =="c":
#     print(Sayi_2*Sayi_1)
# else:
#     print("Düzgün işlem giriniz")

#*Kullanıcıya sinema ya da tiyatro tercihi sorulsun.
#*Sinema izlemek için 50 TL,
#*tiyatro için 100 TL ödenmesi gerekmedir.
#*Öğrencilere % 50 indirim yapıldığı düşünülerek
#*öğrenci ise indirim yapılan
#*öğrenci değilse indirimsiz tutarı
#*hesaplayarak ekrana yazdıran kodu yazınız.

# while True:
#     Tercih = input("Sinema (s) Tiyatro (t) izlemek istersiniz lütfen parantez içinde ki kısayolları kullanınız : ")
#     İndirim =input("Öğrenci misiniz ? (e,h) : ")
#     print("Sinema 50 tl , Tiyatro 100 tl")
            
#     if Tercih == "s" :
#         if İndirim == "e":
#             print("Öğrenci olduğunuzdan dolayı ödemeniz gereken tutar : 25 tl'dir İYİ SEYİRLER")
#         else:
#             print("Ödemeniz gereken tutar : 50 tl'dir İYİ SEYİRLER")
#     elif Tercih == "t":
#             if İndirim == "e":
#                 print("Öğrenci olduğunuzdan dolayı ödemeniz gereken tutar : 50 tl'dir İYİ SEYİRLER")
#             else:
#                 print("Ödemeniz gereken tutar : 100 tl'dir İYİ SEYİRLER")
#     else:
#         print("Yapmak istediğinizi anlayamadık tekrar deneyiniz :( )")
        
#     cevap = input("Başka bir işlem yapmak istiyor musunuz? (e/h): ")
#     if cevap == "h":
#         break

while True:
    print("Which would you like to watch?")
    print("Cinema (c) Theatre (t)")
    
    choice = input("Make your selection: ")
    discount = input("Are you a student? (y/n): ")
    print("Cinema: $50, Theatre: $100")
            
    if choice == "c":
        if discount == "y":
            print("Your discounted price is: $25. Enjoy the show!")
        else:
            print("Your price is: $50. Enjoy the show!")
    elif choice == "t":
        if discount == "y":
            print("Your discounted price is: $50. Enjoy the show!")
        else:
            print("Your price is: $100. Enjoy the show!")
    else:
        print("We didn't understand your request, please try again.")
        
    answer = input("Would you like to perform another operation? (y/n): ")
    if answer == "n":
        break




#*bir sisteme girişte or kullanarak kullanıcı adı veya şifre yanlışsa
#*ekrana "kullanıcı adı veya şifre yanlış" yazdırınız

# kullanici= "mesut"
# sifre="1234"

# Girilenk= input("Kullanıcı adınızı giriniz : ")
# Girilens= input("Şifenizi adınızı giriniz : ")

# if kullanici != Girilenk or sifre != Girilens:
#     print("De get la (kullanıcı adı veya şifre yanlış)")

# else :
#     print("Hoşgeldin Cano")

#*Kullanıcının girdiği 3 sayının en büyük sayısını bulun
# Girilen_1 = int(input("1.Büyük Sayıyı bulmak için rakam giriniz : "))
# Girilen_2 = int(input("2.Büyük Sayıyı bulmak için rakam giriniz : "))
# Girilen_3 = int(input("3.Büyük Sayıyı bulmak için rakam giriniz : "))

# if Girilen_1 > Girilen_2 and Girilen_3:
#     print(f"En büyük sayi {Girilen_1}")
# elif Girilen_2 > Girilen_3 and Girilen_1:
#     print(f"En büyük sayi {Girilen_2}")
# elif Girilen_3 > Girilen_2 and Girilen_1:
#     print(f"En büyük sayi{Girilen_3}")
# else:
#     print("Girilen Sayılar Geçersiz")


#!MAX(SAY1-SAY2-SAY3) EN BÜYÜĞÜNÜ BULUR

#*kullanıcıdan bir şifre ve kullanıcı adı oluşturmasını isteyiniz
#*eğer kullanıcı adı veya şifre en az 8 karakterden oluşuyorsa
#*parolayı ve kullanıcı adını yeniden oluşturmasını isteyiniz!

# Kayıtk= input("Kayıt için kullanıcı adınızı giriniz : ")
# Kayıts= input("Kayıt için şifrenizi giriniz : ")

# if len(Kayıtk) < 8 and len(Kayıts) < 8 :
#     print("Kayıt Olamadınız kullanıcı adınızı ve sifrenizi 8 karakterden fazla giriniz")
# else:
#    print("Tebrikler Kayıt Oldunuz")


#*Bir kişi mağazadan 100 TL ve üzeri alışveriş yaparsa %10 indirim, 200 TL ve üzeri alışveriş
#*yaparsa *%15 indirim, 300 TL ve üzeri alışveriş yaparsa %20
#*indirim kazandığını ve ödeyeceği miktarı ekrana yazınız

# urunler = {
#   "a":100,
#   "b":200,
#   "c":10,
#   "d":40,
#   "e":125,
# }
# toplam = 0
# while True:
#     urun = input("Ney almak istersiniz : ")
#     if urun in urunler:
#         toplam += urunler[urun]
#     devam = input("Alışverişe devam mı? e/h ")
#     if devam == "h":
#         break

# if toplam >=300:
#         toplam -=60
#         print(f"300 tl ve üzeri alışverişinize özel 60 tl indirim kazandınız : {toplam}")
# elif toplam >= 200:
#         toplam -=30
#         print(f"200 tl ve üzeri alışverişinize özel 30 tl indirim kazandınız ödemeniz gereken tutar : {toplam}")
# elif toplam >= 100:
#         toplam -=10
#         print(f"100 tl ve üzeri alışverişinize özel 10 tl indirim kazandınız : {toplam}")



#*basit bir bankamatik uygulaması oluşturunuz
#*kullanıcıdan bir şifre alınız şifre doğru olduğu taktirde işlemler alanlarına yöneltilsin
#*para çekme ve para yatırma işlemleri yapılsın



# kullanici= "mesut"
# sifre="1234"
# bakiye=1000
# Girilenk= input("Kullanıcı adınızı giriniz : ")
# Girilens= input("Şifenizi adınızı giriniz : ")

# if kullanici != Girilenk or sifre != Girilens:
#     print("De get la (kullanıcı adı veya şifre yanlış)")

# else :
#     print("Hoşgeldin", kullanici.upper(), "\nBakiyeniz:", bakiye)
#     while True:
#         istenilen=input(f"ne yapmak istersiniz para çekmek için (c) yatırmak için (p) işlemlerini yapabilirsiniz : ")
#         if istenilen =="c":
#             print(bakiye)
#             Cekilentutar=int(input("Ne kadar istiyorsun Cano : "))
#             if bakiye >= Cekilentutar : 
#                 bakiye=bakiye-Cekilentutar
#                 print(f"Çekilen Tutar : {Cekilentutar} Kalan Tutar : {bakiye}")
#                 devam = input("başka bir işlem yapmak istiyor musunuz ? e/h : ")
#             else:
#                 print("Girilen Tutar Bakiyenizden Yüksek İşlem Yapamıyoruz :( )")

#         if istenilen == "p":
#             Yatırılantutar =int(input("Ne kadar yatırmak istiyorsunuz : "))
#             bakiye=Yatırılantutar+bakiye
#             print(f"Güncel Bakiyeniz : {bakiye} Yatırlan Tutar : {Yatırılantutar}")
#             devam = input("başka bir işlem yapmak istiyor musunuz ? e/h : ")
#         if devam == "h":
#                 break

#!Hile Kodlaması


#!ödevler
#*boş list1 içerisine 4 meyve tanımla ve 3. indextekini patates ile değiştir
# list1=["elma","armut","muz","avakado"]
# list1[3]="patates"
# print(list1)

#*list2 3 yazılım dili girilsin sonuna "python" ekle ve 2.indexteki listeden çıkar
# list2=["css","java","c++","python"]
# list2.pop(2)
# print(list2)


















