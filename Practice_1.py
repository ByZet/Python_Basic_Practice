from math import sin,exp,e,pi # matematik kütüphanesinden sinüs, exponansiyel,euler,pi

a1 = [300,1501,63,177,155,230,207,298,241,123,364,292,153,300,5,177,10000] # liste

a2 = [i for i in a1 if i % 10 == 0] #a1 listesi içinde 10'a tam bölünen elemanları a2 listesine at

print("a2 = ",a2)

a3 = {i: len(str(i)) for i in a2} #değerleri stringe çevirip uzunluğu alıyor

print("a3= ",a3)

print ("{2}:{1}:{0}".format(a3[10000],a3[300],a3[230])) # format ile yazdırma

print(a3.keys(),a3.values()) #sözlük

a4 = tuple(a3.values()) #tuple oluşturma
print( "a4= ",a4)

a5=set(a2) #a5 diye bir liste oluştur bu listeye a2 deki değerleri ekle

print( "a5= ",a5)
print("Toplam,max,min",sum(a1),max(a1),min(a1)) #toplam,max,min

a1.clear() #liste durur ama boş halde

print("a1 listesi",a1)

del(a3) # listesi tamamen siler

print("say",a4.count(3)) # 3 'e kadar değer sayar

print(round(2.4)) #yuvarlama
print("A5 listesi",a5)

print((a5) - {400,64,355,300,10000}) #aynı değer a5 listesinde varsa çıkart

print(a5 | {400,401,500,501}) #a5 listesinde yoksa ekle

