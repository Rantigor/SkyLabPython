# Kullanıcıdan üç sayı alın
sayi1 = int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))
sayi3 = int(input("Üçüncü sayıyı girin: "))

# Üçgen türünü belirleyin
if sayi1 == sayi2 and sayi2 == sayi3:
    print("Eşkenar üçgen")
elif sayi1 == sayi2 or sayi1 == sayi3 or sayi2 == sayi3:
    print("İkizkenar üçgen")
else:
    print("Çeşitkenar üçgen")
