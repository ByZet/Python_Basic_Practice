import matplotlib.pyplot as plt #kütüphane
baslangic = 0.0
bitis = 100.0
x = 0.0
x_liste = list()
y_liste =list()
while baslangic + x <= bitis:
    fonksiyon = 3 * x**2 + 2*x +1
    y_liste.append(fonksiyon)
    x_liste.append(x)
    x += 0.1
plt.plot(x_liste,y_liste)
plt.show()