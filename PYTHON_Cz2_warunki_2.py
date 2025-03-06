'''
#Instr.warunkowa:

if pogoda_OK:
    idz_na_spacer()
    baw_sie_dobrze()
else:
    idz_do_kina()
    miłego_oglądania()
zjedz_sniadanie()


if pogoda_OK:
    idz_na_spacer()
    baw_sie_dobrze()
elif: są_dostępne _bilety:
    idz_do_kina()
    miłego_oglądania()
elif: jest_wolny_stolik:
    idz_do_restauracji()
    zjedz_sniadanie()
else:
    graj_w_szchy_w_domu()



zagnieżdżone if:
if pogoda_OK:
    if Jest_fajna_knajpka:
        zjedz_śniadanie()
    else:
        zjedz_kanapkę()
else:
    if są_bilety:
        idź_do_teatru()
    else:
        idź_na_zakupy()
 



if pogoda_OK:
    pass
elif: są_dostępne _bilety:
    pass
elif: jest_wolny_stolik:
    pass
else:
    pass


#1.    nie może być else bez uprzedniego if;
#2.    else jest zawsze ostatnią gałęzią kaskady, bez względu czy jest elif czy nie;
#3.    else jest opcjonalne i może być pominięte
#4.    jeśli jest else w kaskadzie, tylko 1 z gałęzi będzie wykonana;
#5.    jeśli nie ma else jest możliwe, że żadna gałąź sie nie wykona.


a single if statement, e.g.:

x = 10
if x == 10: # condition
    print("x jest równe 10")     # Executed if the condition is True.

#-------

a series of if statements, e.g.:

x = 10
if x > 5:                         # 1 warunek
    print("x jest większe od 5")  # jeśli 1 warunek  jest True.
if x < 10:                        # 2 warunek
    print("x jest mniejsze niż 10")    # jeśli 2 warunek jest True.
if x == 10:                       # 3 warunek
    print("x jest równe 10")      # jeśli 2 warunek jest True.

#-------

#Instrukcja if-else:

x = 10
if x < 10:  # warunek
    print("x jest mniejsze od 10")  # jeśli warunek jest True.
else:
    print("x jest większe lub równe 10")  # jeśli warunek jest False.

#-------
Seria warunków z else:

x = 10
if x > 5:  # True
    print("x > 5")
if x > 8:  # True
    print("x > 8")
if x > 10:  # False
    print("x > 10")
else:
    print("else będzie wykonane")
#---

#Zagnieżdżone warunki:

x = 10
if x > 5:  # True
    if x == 6:  # False
        print("zagnieżdżone: x == 6")
    elif x == 10:  # True
        print("zagnieżdżone: x == 10")
    else:
        print("zagnieżdżone: else")
else:
    print("else")

#======================================
Pytania:
x, y, z = 5, 10, 8

print(x > z)
print((y - 5) == x)
#------------

x, y, z = 5, 10, 8
x, y, z = z, y, x

print(x > z)
print((y - 5) == x)

#-----------

x = 10

if x == 10:
    print(x == 10)
if x > 5:
    print(x > 5)
if x < 10:
    print(x < 10)
else:
    print("else")

#-------------

x="1"
if x == 1:
    print("one")
elif x == "1":
    if int(x) > 1:
        print("two")
    elif int(x) < 1:
        print("three")
    else:
        print("four")
if int(x) == 1:
    print("five")
else:
    print("six")

#-----------

x = 1
y = 1.0
z = "1"

if x == y:
    print("one")
if y == int(z):
    print("two")
elif x == y:
    print("three")
else:
    print("four")

#-------------------------------------

INSTRUKCJA W WIELU LINIACH:
print ('To jest bardzo długa linia,'  \
  'ale nie chcemy jej dzielić na mniejsze linie.')
print ('To też działa?',
       'Nie wiedziałem!')
       
x = 10
if x == 10 or x > 0 or \
       x < 100:
       print ('True')

a=1+\
      2+\
3
print(a)

#-------------------------------------
ZADANIE 1: 
kalkulator podatkowy 
1.  kwota wolna od podatku wynosi 1650 PLN
2.  od dochodu należy odliczyć 350,08 PLN jako koszty
    uzyskania przychodu
3.  od powyższej kwoty należy odliczyć 12%
    na uzbezpieczenie społeczne (ZUS)
4.  jeśli przychód po odliczeniu kosztów ubezpieczenia
    społecznego jest nie większy niż 85528 PLN, 
    podatek wynosi 18% przychodu
5.  jeśli przychód jest większy niż 85528 PLN podatek
    wynosi 15345 PLN i 2 gr, 
    plus 32% nadwyżki ponad 85 528 PLN.
6.  od podatku należy odliczyć 15% na skłatkę zdrowotną
7.  jeśli podatek jest mniejszy niż 0, to przyjmujemy
    wartość 0


dochód = float(input("Wprowadź przychód: "))
dochód -= 1650
dochód -= 350.08
if dochód < 85528:
	podatek = dochód * 0.18 - 556.02
else:
	podatek = (dochód - 85528) * 0.32 + 14839.02

if podatek < 0.0:                
 	podatek = 0.0

podatek = round(podatek, 0)
print("Podatek:", podatek, "PLN")

#------------------

ZADANIE 2: Oblicz średnicę i obwód koła samochodu,
gdy podany jest rozmiar opony np, 205/55 R16 
(trzeba wczytać 3 parametry)

#-----------------

ZADANIE 3: Rok przestępny

1.    if the year number isn't divisible by four, it's a common year;
2.    otherwise, if the year number isn't divisible by 100, it's a leap year;
3.    otherwise, if the year number isn't divisible by 400, it's a common year;
4.    otherwise, it's a leap year.

year = int(input("Wprowadź rok: "))

if year < 1582:
	print("Tylko kalandarz Juliański")
else:
	if year % 4 != 0:
		print("Zwykły rok")
	elif year % 100 != 0:
		print("Przestępny") 
	elif year % 400 != 0:
		print("Zwykły rok")
	else:
		print("Przestępny")


#LUB:
if rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0):
    return True
else:
    return False
 
#------------------
ZADANIE 4. Oblicz obwód dowolnego równoleżnika Ziemi


#------------------
ZADANIE 5. Oblicz pierwiastki trójmianu kwadratowego  y=ax2+bx+c
           o zadanych współczynnikach a,b,c

CO Z DELTĄ < 0?

dlt=b**2-4ac
x1= (-b - dlt ** .5) / 2a
x2= (-b + dlt ** .5) / 2a

'''
