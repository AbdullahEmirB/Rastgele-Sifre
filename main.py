import random

karakterler = "+-/*&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
parola_uzun = int(input("Şifre Kaç Karakter Olsun = "))
parola_adet = int(input("Kaç Adet Şifre Olsun = "))

for i in range(parola_adet):
    parola = ""
    for i in range(parola_uzun):
        parola_karakter = random.choice(karakterler)
        parola += parola_karakter
    print("Rastgele Oluşturulan Şifreniz =", parola)
