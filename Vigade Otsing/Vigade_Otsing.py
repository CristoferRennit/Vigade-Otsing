import math  #import*from math asemel import math

print("Ruudu karakteristikud")

a = int(input("Sisesta ruudu külje pikkus =>")) #lisasin int()
S = a ** 2
print("Ruudu pindala", S)
P = 4 * a
print("Ruudu ümbermõõt", P)
di = a * math.sqrt(2)
print("Ruudu diagonaal", round(di,2))
print()

print("Ristküliku karakteristikud")
b=int(input("Sisesta ristküliku 1. külje pikkus => ")) #lisasin int()
c=int(input("Sisesta ristküliku 2. külje pikkus => ")) #lisasin int()
S=b*c
print("Ristküliku pindala", S)
P=2*(b+c) #2(b+c) => 2*(b+c)
print("Ristküliku ümbermõõt", P)
di=math.sqrt(b**2+c**2) #(b*2+c*2) => (b**2+c**2)
print("Ristküliku diagonaal", round(di))
print()

print("Ringi karakteristikud")
r=int(input("Sisesta ringi raadiusi pikkus => "))
d=2*r   #Korrutusmärk oli puudu (2r)
print("Ringi läbimõõt", d)
pi = 3.14
S=pi*r**2 #pi()*r*2 => pi*r**2
print("Ringi pindala", round(S))
C=2*pi*r  #Korrutusmärk oli puudu ja sulud oli valed(2pi()*r)
print("Ringjoone pikkus", round(C))
