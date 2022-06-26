def kelvin(x):
    return(x + 273.15)

def fahrenheit(x):
    return((x * 1.8) + 32)

while True:
    islem = int(input("Eğer kelvin dönüşü yapmak istersen 1 ,fahrenheit için 2, çıkmak için 3'e bas \n"))
    a = int(input("ilk deger:"))
    b = int(input("ikinci değeri gir:"))
    artis = int(input("artış değerini giriniz"))
    element = [a]
    while a + artis <= b:
        a += artis
        element.append(a)
    if islem == 1:
        for z in element:
            print(kelvin(z))
    if islem ==2:
        for v in element:
            print(fahrenheit(v))
    if islem == 3:
        print("programdan çıkıldı")
        break
    













