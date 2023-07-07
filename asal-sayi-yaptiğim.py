import random
import time

print("Merhaba |Asal Sayı| oyununa hoşgeldin ama senin yaşını ve adını öğrenmem gerek.")
time.sleep(1)
name = input("İsminizi giriniz : ").title()

age = int(input("Yaşınızı giriniz : "))

if age >= 11:
    print(f"Oyunumuza hoşgeldin {name}")
else:
    print(f"Yaşın yetmiyor {name}")

print(f"Evettt {name} şimdi sana bir şey sormamız gerek bu oyunun nasıl oynanıldığını biliyor musun?\nEğer biliyorsan w, bilmiyorsan o tuşuna bas ve bekliyorum ")

soru = input("İstediğiniz işlem için söylenen tuşu tıklayın : ")

if soru == "w":
    print(f"Biliyorsan sıkıntı yok {name}")
else:
    print(f"Bilmiyorsan anlatalım ilk önce oyunumuzun adı Asal sayı öğrenme ama sen bunu Bir sayı asal mı değil mi diyede bakabilirsin\nOyuna giriş yaptık zaten şimdi önüne yazma ekranı çıkacak o ekrana Asal sayı mı değil mi diye yaz\nBuraya kadar geldiysen tamam sonra bekledikten sonra cevabın yanlış mı doğru mu öğrendin\nSeni çok sıkmadan oyuna geçelim {name}")

tahmin_hakki = 2

# 1.Soru

sayi = int(input("Asal sayı giriniz : "))
asalmi = True

if sayi == 1:
   asalmi = False

for i in range(2, sayi):
    if (sayi % i == 0):
        asalmi = False
        break

if asalmi:
    print("Sayınız Kontrol Ediliyor...")
    time.sleep(2)
    print(f"Afferim {name}.")
    tahmin_hakki -= 1
else:
    print(f"Yanlış cevap {name} ama Sorun yok 2 cevap hakkın daha var.")
    tahmin_hakki -= 1
    print("Yeni soru geliyorrr")
    time.sleep(2)

sayi2 = int(input("Asal sayı giriniz : "))
asalmi2 = True

if sayi2 == 1:
    asalmi2 = False

for i in range(2, sayi2):
    if (sayi2 % i == 0):
        asalmi2 = False
        break

# 2. Soru

if asalmi2:
    print(f"Sayınız Kontrol Ediliyor...")
    time.sleep(2)
    print(f"Afferim {name} Çok iyi.")
    tahmin_hakki -= 1
    print("Sonraki sorumuz gelsinnn")
else:
    print(f"Cevabın kontrol ediliyor {name} Lütfen bekle...")
    time.sleep(2)
    print(f"Yanlış cevap {name} ama Sorun yok son bir cevap hakkın daha var.")
    tahmin_hakki -= 1
    print("Sorular bitti...")
    time.sleep(2)

print(f"Evettt {name} şimdi söyle bakalım Oyunumuz nasıldı ve oyunu puanlama kısmına geldi.")
time.sleep(2)

soru2 = input("Kaç puan verirsin(5 üzerinden) : ")

if soru2 == 1:
    print("Çok kötü olmuş")
else:
    print("Gö")

if soru2 == 2:
    print("Kötü olmuş")
else:
    print("rü")

if soru2 == 3:
    print("İdare eder")
else:
    print("şü")

if soru2 == 4:
    print("İyi olmuş")
else:
    print("rüz")

if soru2 == 5:
    print("Çok iyi olmuş")
else:
    print("Bay bay")

print(f"Oyunumu oynadığın için Teşekkürler {name} daha sonra görüşmek üzere")