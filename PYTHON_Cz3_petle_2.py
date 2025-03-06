'''
PĘTLE:

While:

while warunek:
    instrukcja_1
    instrukcja_2
    instrukcja_3
    :
    :
    instrukcja_n

#------------

# znajdź największą liczbę
najw_liczba = -999999999

# wprowadź pierwszą liczbę.
liczba = int(input("Wprowadź liczbę lub -1 aby zakończyć: "))
licz = 0
# jeśli liczba różna od -1 idź dalej
while liczba != -1:
    licz += 1 
    if liczba > najw_liczba:
        najw_liczba = liczba
    liczba = int(input("Wprowadź liczbę lub -1 aby zakończyć: "))
if licz > 0:
    print("Największa to:", najw_liczba)
else:
    print('nic nie wprowadzono')

#------------

secret_number = 777
print(
"""
+================================+
| Witaj w grze!                  |
| Wprowadź liczbę i zgadnij,     |
| co miałem na myśli             |
+================================+
""")

user_number = int(input("Podaj liczbę: "))

while user_number != secret_number:
    print("Ha ha! Utknąłeś w pętli!")
    user_number = int(input("Wprowadź jeszcze raz: "))
print(secret_number, "OK! Jesteś wolny.")
#------------------------

i = 1
while i <= 10:
    print("Cóś robię", i)
    i += 1
print("Koniec")

#------------------
#! the range() function accepts only integers as its arguments

for i in range(10):
     print("Cóś robię", i)
     pass
print("Koniec")

#------------------

for i in range(3, 10):
     print("Cóś robię", i)
     pass
print("Koniec")

#-------------------
#Pytanie1: jaki będzie wynik?
for i in range(3, 3):
     print("Cóś robię", i)
     pass
print("Koniec")

#-------------------
#Pytanie1: jaki będzie wynik?

for i in range(10):
     pass
print("Koniec")

#-------------------

1.    pętla ma swoją zmienną sterującą, do której automatycznie przypisuje wartości za pomocą funkcji range
2.    funkcja range() generuje kolejne wartości z zestawu: 0, 1, 2 .. 97, 98, 99; 
      Zaczyna od 0 (lub wartości pierwszego parametru) i kończy na wartości o 1 mniejszej od drugiego 
      parametru (lub jedynego, jeśłi jest tylko jeden)
3.    instrukcja pass wewnątrz pętli nic nie robi - jest tam, bo musi być przynajmniej 1 intrukcja wewnątrz pętli
4.    funkcja range() function przyjmuje jako argumenty tylko liczby całkowite 
      i generuje sekwencje liczb całkowitych.

# 3 argumenty range:
for i in range(30, 20, -3):
     print("Cóś robię", i)
     pass
print("Koniec")

#------------
power = 1
for expo in range(16):
    print("2 do potęgi", expo, "to", power)
    power *= 2

#--------------------------------------
import time
for second in range(1, 6):
    print(second, "Mississippi")
    time.sleep(1)
print("Ready or not, here I come!")
#--------------------------------------

# break - example

print("Instrukcja break:")
for i in range(1, 6):
    if i == 3:
        break
    print("W pętli", i)
print("Poza pętlą")

#--------------------------------------
# continue - example

print("\nInstrukcja continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("W pętli", i)
print("Poza pętlą")
#--------------------------------------

for i in range(1, 6):
    print("W pętli i", i)
    for j in range(1,10):
        if j == 4:
            break
        print("    W pętli j", j)
	

print("Poza pętlą")

#-------------------------------------
# NAJWIĘKSZA LICZBA z pętlą DO WHILE

największa = -99999999
licznik = 0

while True:
    liczba = int(input("Wprowadź liczbę lub -1 aby zakończyć program: "))
    if liczba == -1:
        break
    licznik += 1
    if liczba > największa:
        największa = liczba

if licznik != 0:
    print("Największa liczba to", największa)
else:
    print("Nic nie wprowadzono")

#------------------------------------------------------------------------
#Usuń samogłoski:
user_word = input("Enter your word: ")
user_word = user_word.upper()

for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        print(letter, end = '')
        
#---------------------------------------------------------------------------
#ELSE w pętlach:

i = 1
while i < 15:
    print(i)
    i += 1
else:
    print("else:", i)
    
#-------------------

# dla FOR else zachowuje ostatnią wartość:
for i in range(5):
    print(i)
else:
    print("else:", i)

#----------------------------
#Ćwiczenie 1 (samodzielnie)
Jaki będzie wynik?
n = 3
while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)
#---------------------------
#Ćwiczenie 2 (samodzielnie)
Jaki będzie wynik?
n = range(4)
print(n)
for num in n:
    print(num - 1)
else:
    print(num)
#---------------------------
#Ćwiczenie 3 (samodzielnie)
#Jaki będzie wynik?
for i in range(0, 6, 3):
    print(i)

====================================================================



'''
