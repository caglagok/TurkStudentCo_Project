#Soru: Kullanıcıdan iki sayı alarak bu sayıları toplayan bir programın pseudo kodunu yazın

x = input("Birinci sayi giriniz: " )
y = input("İkinci sayi giriniz: " )
z = int(x)+int(y)
print(z)

"""
ÇIKTI
Birinci sayi giriniz: 2
İkinci sayi giriniz: 2
4
"""
# Soru: 1'den 100'e kadar olan sayıları toplayan bir programın pseudo kodunu yazın

sum = 1
for x in range(1 , 100):
    sum += x
print(sum)

"""
ÇIKTI
5050
"""

# Soru: Kulanıcıdan alınan bir sayının asal olup olmadığını bulan bir programın pseudo kodunu yazın.

x = int(input("Bir sayi giriniz:" ))
if x <= 1:
    print(f"{x} asal değildir.")
else:
    for i in range(2, x):
        if x % i == 0:
            print(f"{x} asal değildir.")
            break
    else:
        print(f"{x} asaldır.")
"""
ÇIKTI
Bir sayi giriniz:56
56 asal değildir.

Bir sayi giriniz:2
2 asaldır.

Bir sayi giriniz:23
23 asaldır.
"""

#Soru: Bir dizideki (array) elemanların tekrar edip etmediğini kontrol eden bir programın pseudo kodunu yazın.

dizi = [2, 4, 6, 8, 10, 3, 5, 10, 2, 4] 
#dizi = [1, 2, 3, 4]
tekrar_eden_elemanlar = []
for i in range(len(dizi)):
    for j in range(i + 1, len(dizi)):
        if dizi[i] == dizi[j]:
            if dizi[i] not in tekrar_eden_elemanlar:
                tekrar_eden_elemanlar.append(dizi[i])

if tekrar_eden_elemanlar:
    for k in tekrar_eden_elemanlar:
        print(f"Tekrar eden eleman: {k}")
else:
    print("Dizide tekrar eden eleman yok.")

"""
ÇIKTI
Tekrar eden eleman: 2
Tekrar eden eleman: 4
Tekrar eden eleman: 10

ÇIKTI
Dizide tekrar eden eleman yok.
"""
