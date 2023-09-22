# Toplama işlemi
def toplama(x, y):
    return x + y

# Çıkarma işlemi
def cikarma(x, y):
    return x - y

# Çarpma işlemi
def carpma(x, y):
    return x * y

# Bölme işlemi
def bolme(x, y):
    if y == 0:
        return "Sıfıra bölme hatası!"
    return x / y

while True:
    print("Yapmak istediğiniz işlemi seçin:")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Çıkış")
    
    secim = input("Seçiminizi yapın (1/2/3/4/5): ")
    
    if secim == "5":
        print("Hesap makinesi kapatılıyor.")
        break
    
    sayi1 = float(input("Birinci sayıyı girin: "))
    sayi2 = float(input("İkinci sayıyı girin: "))
    
    if secim == "1":
        print("Sonuç: ", toplama(sayi1, sayi2))
    elif secim == "2":
        print("Sonuç: ", cikarma(sayi1, sayi2))
    elif secim == "3":
        print("Sonuç: ", carpma(sayi1, sayi2))
    elif secim == "4":
        print("Sonuç: ", bolme(sayi1, sayi2))
    else:
        print("Geçersiz seçim! Lütfen tekrar deneyin.")
