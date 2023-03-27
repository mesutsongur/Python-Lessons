
#!type
#?veri tipini verir
# sayi = 20
# print(type(sayi))

# text = "mdasd"
# print(type(text))

#!Değişkenlerde type çeşitleri
#?int(sayısal)
# sayi1 = 10

# sayi2 = 50
# sayi3 = 30
# print(sayi2+sayi3)

# sayi2 = 20
# sayi4 = "50"
# sonuc = sayi2+int(sayi4)
# print(sonuc)

#?Sayi++ gibi sayı arttırma komutu pythonda sööz konusu değildir !
# sayi= 20
# sayi++ #! hata
# print(sayi)

#*Doğru kullanımı
# sayi = 30
# sayi = sayi + 1 #?sayı arttırma
# sayi += 1 #?sayı arttırma alternatifi
# print(sayi)

#?string() (metinsel ifadeler)
# text = "selam cano"
# print(type(text))

#?Float() (virgüllü sayılar)
# sayi = 1,5
# print(type(sayi))

#?Tuple
# meyveler = "elma","armut","karpuz",12
# print(meyveler)

#*Tuple veri çekimi
# meyveler = "elma","armut","karpuz",12
# print(meyveler[0])

#?List (array)
#*index numaraları 0 dan döner
# harfler = ["a","b","c","d","e","f"]
# print(harfler[2])

#*list içerisinde eleman çağırmak
# harfler = ["a","b","c","d","e","f"]
# harflerIndex = harfler[3]
# print(harflerIndex)

#?Set() random index işe yaramıyor aynı veri printlenmez bunun için for döngüsü yapılabilir
# test = {"araba","ev",34,23,"masa",100,245,"telefon","ayakkabı"}
# print(test)

#?Dict (obje)
# kullanici = {
#     "kadi":"mehmet",
#     "sifre":123,
#     "yas":23
# }

# print(kullanici)

#*veri çekim
# kullanici = {
#     "kadi":"mehmet",
#     "sifre":123,
#     "yas":23
# }

# print(kullanici["kadi"])

#?dict ve list yapısının iç içe kullanımı
# kullanıcılar = [
#     {
#         "kadi":"mehmet",
#         "sifre":1234
#     },
#     {
#         "kadi":"mahmut",
#         "sifre":2345
#     },
#     {
#         "kadi":"selim",
#         "sifre":3456
#     }
# ]

# print(kullanıcılar[1]["sifre"])

#!operatör işlemleri
#? +++++ (toplama)
# say1 = "30"
# say2 = "40"
# sonuc = say1 + say2
# print(sonuc)

# text1 = "mehmet"
# text2 = "coban"
# print(text1+text2)

#? ----- (çıkarma)
# say1 = 15
# say2 = 20
# sonuc = say1 - say2
# print(sonuc)

# say = 30
# say1 = 10
# say3 = 40
# say = say1 - say3 - say #* "say" kullanılabilir 2 kere
# print(say1)

# say1 = 30
# say2 = "40"
# sonuc = say1 - say2
# print(sonuc)

#? ****** (çarpma)
# say1 = 10
# say2 = 10
# print(say1*say2)

#? ///// (bölme)
#? %%%%%% (mod alma) bölümden kalanı verir
# say = 10
# print(say%2)

#? ** (üs alma)
# say = 5
# sonuc = say**2
# print(sonuc)

#!değişkenlerde type tipini değiştirmek
#?int()
# say = int("23")
# say1 = int("25")
# sonuc = say + say1
# print(sonuc)

# isim = int("mehmet")
# soyisim = int("asda")
# toplam = isim+soyisim
# print(toplam)

# sayi = int(5.65)
# print(sayi)

#?string
# say = str(23)
# print(type(say))































