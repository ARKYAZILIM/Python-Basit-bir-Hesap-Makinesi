# Basit Hesap Makinesi

def toplama(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def carpma(a, b):
    return a * b

def bolme(a, b):
    if b != 0:
        return a / b
    else:
        return "Bölme hatası: Bölenin sıfır olmaması gerekiyor."

# Kullanıcıdan giriş al
a = float(input("Birinci sayıyı girin: "))
b = float(input("İkinci sayıyı girin: "))

print("toplama:", toplama(a, b))
print("cikarma:", cikarma(a, b))
print("carpma:", carpma(a, b))
print("bolme:", bolme(a, b))
