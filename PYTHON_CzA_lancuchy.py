'''
# Kodowanie ASCII
ASCII (American Standard Code for Information Interchange): 
 - 256 różnych znaków
 - 8 bitów na każdy znak.
 - punkt kodowy to liczba tworząca znak. Np. 32 to spacja, 65 to 'A' , 55 to'7'.

Strona kodowa to standard do do przechowywania znaków diakrytycznych danego języka.
# UNICODE: 
 - ponad milion code pointów dla kazdego znaku
 - nie mówi nic o tym jak przechowywac dane, kodować, zapisywac, dlatego rozrózniamy różne rodzaje kodowania
 - pierwsze 128 punktów kodowych Unicode jest identycznych jak w ASCII, 
 - pierwsze 256 punktów kodowych Unicode jest identycznych ze stroną kodową ISO/IEC 8859-1 (zaprojektowaną dla języków Europy Zachodniej).

# UCS4 - Universal Character Set używa 32 bitów (czterech bajtów),by przechować każdy znak.

UTF-8 Nazwa wywodzi się od Unicode Transformation Format.
Metoda ta jest bardzo inteligentna. UTF-8 wykorzystuje tyle bitów na każdy punt kodowy, 
ile w rzeczywistości jest wymagane, by je poprawnie zakodować, np. 
    • wszystkie znaki alfabetu łacińskiego (oraz wszystkie znaki standardu ASCII) zajmują 8 bitów; 
    • znaki inne niż pochodzące z alfabetu łacińskiego zajmują 16 bitów; 
    • ideogramy CJK (Chiny-Japonia-Korea) zajmują 24 bity. 

Język Python 3 w pełni obsługuje Unicode oraz UTF-8:
    • Można używać znaków zakodowanych w Unicode/UTF-8 w do dawania nazw zmiennym, itp, 
    • możesz korzystać z nich zarówno w przypadku danych wejściowych oraz wyjściowych. 

Cechy:
    - Łańcuchy znaków w języku Python są sekwencjami stałymi.
    - Funkcja len() zwraca liczbę znaków zawartych w argumentach.
    - Łańcuch znaków może być pusty. Jego długość to wówczas 0
    - Ukośnik wsteczny (backslash) (\) używany jako znak wyjścia nie jest uwzględniony w całkowitej długości stringu.
    - łańcuchy znaków w języku Python są sekwencjami
    - Łańcuchy znaków nie są listami, ale można traktować je jak listy w szczególnych przypadkach np., 
      aby uzyskać dostęp do dowolnych znaków łańcucha, można to zrobić za pomocą indeksowania, tak jak w przykładzie w edytorze. 
      
# STRINGS
# Typowy string musi być zawarty w " lub '
text = "Przykładowy string"
text = 'Przykładowy string'

# Stringi wieloliniowe - można zapisać ciąg znaków
#wraz z częsciowym formatowaniem za pomoca 3 znaków ' lub "
#np:
text = """Linia #1    
Linia #2
Linia #3
"""

# Jak wyznaczyć długość ciągu znaków?
a) sposób "na piechotę" - za pomocą pętli. Zwróc uwagę, że przykład wskazuje na iterowalność stringów!
text = "Ala ma kota"
counter = 0
for letter in text:
    counter+=1
print(counter)

b) funkcja len():
text = "Ala ma kota"
print("Długość stringu: {}".format(len(text)))
#lub:
print("Długość stringu: %s"%len(text2))

#łańcuchy znaków mogą być:
    • konkatenowane (połączone) (operatory +, +=)
    • replikowane, czyli powielane (*, *=)

Przykład:
str1 = 'a' 
str2 = 'b' 
print(str1 + str2) 
print(str2 + str1) 
print(5 * 'a') 
print('b' * 4)

#Funkcje ord i chr:
print(ord('A'))
print(chr(98))

print(chr(ord('x'))) 
print(ord(chr(65)))

# Wycinki:
# Stringi są typem sekwencyjnym, są idexowane, mogą byc iterowane

alpha = "To jest kurs języka Python."
print(alpha[2:5])
print(alpha[1:3]) 
print(alpha[3:]) 
print(alpha[:3]) 
print(alpha[3:-2]) 
print(alpha[-3:4]) 
print(alpha[::2]) 
print(alpha[1::2])

Sekwencje:
#1:

lancuch = 'Przykładowy łańcuch'
for ch in lancuch:
    print(ch, end=' ')
print()

#2:
lancuch = 'Przykładowy łańcuch'
for i in range(len(lancuch)): 
    print(lancuch[i], end='-') 

# Można wykorzystać operatory in/not in w celu sprawdzenia czy dany string jest częścią innego stringu/listy/krotki itp.

a = "Python"
b = "####Python course #####"
print("Czy słowo \"%s\" znajduje się w ciągu \"%s\"? Odpowiedź: "%(a, b), a in b)

#Ćwiczenie 1: 
#    Zadanie: znajdz wszystkie metody modułu re,
#     które zawierają w nazwie 'find'
import re
temp = []
lista = dir(re)
for el in lista:
    if 'find' in el:
        temp.append(el)
temp.sort()
print(temp)

#Ćwiczenie 2:
alfabet = "abcdefghijklmnopqrstuvwxyz" 
print("f" in alfabet) 
print("F" in alfabet) 
print("1" in alfabet) 
print("ghi" in alfabet) 
print("Xyz" in alfabet)


# Stringi są niemutowalne (są stałe, nieedytowalne ciągi znaków):
  - nie można podmienić lub usunąć jednego czy kilku znaków z danego ciągu,
  	text = "Przykładowy string"
	text[-6:] = "!ciag!"
        txt[2] = 'a'
	del text[0]
  - nie mają metody append(), insert(), ani del(),
  - można jedynie usunąć łańcuch jako całość
        del txt
  - tworzenie nowej kopii łańcucha znaków za każdym razem, gdy modyfikowana jest jego zawartość, 
        text = text[:5] + "XYZ" + text[5:]
  - nieco pogarsza nieco efektywność kodu. To nie jest problem.

#Operacje na łańcuchach znaków:
# a) Funkcje min/max  (warunek: sekwencja nie może być pusta, inaczej ValueError)

t = 'The Knights Who Say "No!"'
print('[' + max(t) + ']')
print('[' + min(t) + ']')
print(min("aAbByYzZ")) 

print("*** Metoda index() - szukany element musi występować w sekwencji - jego brak spowoduje wystąpienie wyjątku ValueError.")

print("aAbByYzZaA".index("B"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A", 3))
print("aAbByYzZaA".index("Q"))

print("***Metoda find()***")
#jest podobna do metody index()- szuka ona podłańcucha znaków i zwraca indeks pierwszego jego wystąpienia, ale:
#   • jest bezpieczniejsza - nie generuje błędu dla argumentu zawierającego nieistniejący podłańcuch znaków (zwraca w takim przypadku -1) 
#   • działa wyłącznie z łańcuchami znaków - nie próbuj stosować jej do żadnej innej sekwencji. 
print("aAbByYzZaA".find("B"))
print("aAbByYzZaA".find("Z"))
print("aAbByYzZaA".find("A", 3))
print("aAbByYzZaA".find("Q"))

# find() dwuargumentowy - drugi argument określa indeks, na którym rozpocznie się wyszukiwanie 
txt = """Umilkli strzelce, stali szczwacze zadziwieni
Mocą, czystością, dziwną harmoniją pieni.
Starzec cały kunszt, którym niegdyś w lasach słynął,
Jeszcze raz przed uszami myśliwców rozwinął;
Napełnił wnet, ożywił knieje i dąbrowy,
Jakby psiarnię w nie wpuścił i rozpoczął łowy.
Bo w graniu była łowów historyja krótka:
Zrazu odzew dźwięczący, rześki - to pobudka;
Potem jęki po jękach skomlą - to psów granie;
A gdzieniegdzie ton twardszy jak grzmot - to strzelanie.
Tu przerwał, lecz róg trzymał; wszystkim się zdawało,
Że Wojski wciąż gra jeszcze, a to echo grało."""
fnd = txt.find('to')
while fnd != -1:
    print(fnd)
    fnd = txt.find('to', fnd + 1) 

# find() trójargumentowy - trzeci argument wskazuje na pierwszy indeks, który nie będzie brany pod uwagę podczas wyszukiwania 
(tak naprawdę jest to górny limit wyszukiwania).
print('Ala ma kota i psa'.find('a', 0, 10))
print('Ala ma kota i psa'.find('a', 5, 10)) 

print("***Metoda rfind()***")  # jak find, tylko od końca

print("Ala Ola Ela Ula Ewa Iza".find("la")) 
print("Ala Ola Ela Ula Ewa Iza".rfind("la")) 
print("Ala Ola Ela Ula Ewa Iza".find("la", 6)) 
print("Ala Ola Ela Ula Ewa Iza".rfind("la", 6)) 
print("Ala Ola Ela Ula Ewa Iza".find("la", 5, 10))
print("Ala Ola Ela Ula Ewa Iza".rfind("la", 5, 10))

print("Funkcja list() ")
print(list("AlaOlaElaUlaEwaIza"))
print(tuple("AlaOlaElaUlaEwaIza"))

print("*** Metoda count()") 
print("Ala Ola Ela Ula Ewa Iza".count("la"))
print('Ala Ola Ela Ula Ewa Iza'.count("E"))

print("*** Metoda capitalize()")
print('litwo ojCzYZNO MoJA TY jESTeś jak ZDRowie'.capitalize())
print('ALPHA'.capitalize()) 
print('123'.capitalize()) 
print("αβγδ".capitalize()) 

print("*** Metody lower() i upper()") 
print("SiGmA=60".lower())
print("SiGmA=60".upper())

print("*** Metoda center()")
print('[' + 'alpha'.center(50) + ']')
print('[' + 'alpha'.center(50,"^") + ']')

print("*** Metoda startswithswith()")
if "epsilon".startswith("Eps"):
    print("Tak, zaczyna się na 'eps'.")
else:
    print("A skądże, nie zaczyna się na 'eps")

print("*** Metoda endswith() ")
if "epsilon".endswith("on"):
    print("I owszem")
else:
    print("W życiu")

print("*** Metoda isalnum()") 
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

print("*** Metoda isalpha()")
print("Moooo".isalpha())
print('Mu40'.isalpha())

print("*** Metoda isdigit() ")
print('2018'.isdigit())
print("Year2019".isdigit())

print("*** Metody islower() i isupper()") 
print("Moooo".islower())
print('moooo'.islower())
print("MOOO".isupper())
print('moOOOoo'.isupper())

print("*** Metoda isspace()" )
print('\n\r   \t'.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

print("*** Metoda join()" )
#    • metoda ta wykonuje połączenie - oczekuje jednego argumentu jako listy; wszystkie elementy listy muszą być łańcuchami - jeśli nie metoda zgłosi wyjątek TypeError; 
#    • wszystkie elementy listy zostaną połączone w jeden łańcuch, ale łańcuch znaków, z którego wywołano metodę, zostanie użyty jako separator; 

print("\n".join("Ala Ola Ela Ula Ewa Iza"))
print(" i ".join("Ala Ola Ela Ula Ewa Iza"))
print("-".join("Ala Ola Ela Ula Ewa Iza"))

print("***Metoda  lstrip()***""")
# Bezparametrowa metoda lstrip() zwraca łańcuch nowo utworzony z oryginalnego łańcucha, 
# usuwając wszystkie wiodące spacje i inne białe znaki.
print(" \n\t Ala ma kota ")
print(" \n\t Ala ma kota ".lstrip())

# Metoda jednoparametrowa lstrip() działa tak samo, jak jej bezparametrowa wersja, 
#ale usuwa wszystkie znaki wpisane w jej argument (łańcuch), a nie tylko spacje:
print("www.cisco.com".lstrip("w.")) 
print("www.cisco.com".lstrip("w.c")) 
print("www.cisco.com".lstrip("w.i")) 
print("www.cisco.com".lstrip("w.cis")) 

print("***Metoda rstrip()***""")
print("www.cisco.com".rstrip("m")) 
print("www.cisco.com".rstrip(".com")) 
print("www.cisco.com".rstrip("moc.")) 
print("www.cisco.com".rstrip("mo.cis")) 

print("***Metoda strip() = lstrip i rstrip w jednym***""")
print("  \n\t  Ala ma kota \t\n   ")
print("  \n\t  Ala ma kota \t\n   ".strip())
print("www.cisco.com".strip("w.cm"))

print("*** Metoda split()" )
print("This is Hogwarts!!!! Muggle!".split())
print("This is Hogwarts!!!! Muggle!".split('!'))

print("*** Metoda replace() ***") 
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it! is this it? is?".replace("is", "are", 2)) # trzeci parametr ogranicza liczbę zmian
print("Apple juice".replace("juice", ""))

text3 = "Python institute course."
print(text3.replace("institute", "language"))
print(text3)

print("*** Metoda swapcase() ***") 
print("Ala Ma Kota".swapcase())

print("*** Metoda title() ***") 
print("ala ma kota".title())

#-------------------------------------

#Porównywanie łańcuchów znaków
#Operatory, które mogą być użyte do porównywania łańcuchów znaków:
    • == 
    • != 
    • > 
    • >= 
    • < 
    • <=
# 1. Python porównuje wartości punktów kodowych, znak po znaku
# 2. Ostateczna relacja między łańcuchami znaków jest determinowana przez porównanie pierwszych różniących się znaków w obydwu łańcuchach znaków
# 3. Jeśli krótszy z łańcuchów jest taki sam jak początek dłuższego, dłuższy łańcuch znaków uważa się za większy
# 4. Jeśli łańcuch znaków zawiera wyłącznie cyfry, w dalszym ciągu nie jest to liczba
# 5. Porównywanie łańcuchów znaków z liczbami jest złym pomysłem.

print("Ala" < "Ola")
print("Ala" < "ala")
print("Ala" < "Ala ")
print("Ala" != "Ola")
print("Ala" == "Ala ")
print("10" == 10)
print('10' > 10)

# Sortowanie list zawierających łańcuchy znaków:
imiona = ['Ola', 'Ula', 'Iza', 'Ela', 'Ala'] 
print(sorted(imiona))

# Zamiana liczby (całkowitą lub rzeczywistą) w łańcuch znaków:
itg = 13
flt = 1.3
si = str(itg)
sf = str(flt)
print(si + ' ' + sf) 

# Transformacja w odwrotną stronę (przemiana łańcucha znaków na liczbę) 
# jest możliwa wtedy i tylko wtedy, kiedy łańcuch znaków reprezentuje poprawną liczbę. 
# Jeśli warunek nie zostanie spełniony, otrzymamy wyjątek ValueError.

si = '13' 
sf = '1.3' 
itg = int(si) 
flt = float(sf) 
print(itg + flt) 

'''
