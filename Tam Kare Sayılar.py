# Kullanıcıdan iki farklı sayı alın
sayi1 = int(input("İlk sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))

# Sayıları küçükten büyüğe sıralayın
kucuk_sayi = min(sayi1, sayi2)
buyuk_sayi = max(sayi1, sayi2)

# Tam kare sayıları bulun ve yazdırın
print(f"{kucuk_sayi} ile {buyuk_sayi} arasındaki tam kare sayılar:")
for i in range(kucuk_sayi, buyuk_sayi + 1):
    kare_kok = int(i ** 0.5)
    if kare_kok ** 2 == i:
        print(i)
