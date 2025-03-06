'''
Windows: c:\\katalog\\plik.txt
Unix:	 /katalog/plik

c:\\katalog\\plik.txt (W Pythonie "\" - znak ucieczki)
ale można c:/katalog/plik.txt

Komunikacja odbywa się za pomocą uchwytów, (lub strumieni -tu: synonimy)
Łączenie strumienia z plikiem, to otwieranie pliku, odłączenie, to zamykanie

Co może się wydarzyć:
-fizyczny plik istnieje, ale program nie może go otworzyć. 
-program otworzył zbyt wiele strumieni, a system operacyjny może nie zezwalać na jednoczesne otwarcie więcej niż n plików

-otwarcie strumienia powinno zadeklarować sposób przetwarzania strumienia. Ta deklaracja nazywa się trybem otwarcia.
 Program będzie mógł wykonywać tylko te operacje, które są zgodne z zadeklarowanym trybem otwarcia.

W strumieniu wykonywane są 2 podstawowe operacje:
    • odczyt ze strumienia: fragmenty danych są pobierane z pliku i umieszczane w obszarze pamięci zarządzanym 
      przez program (np. zmienna); 
    • zapis w strumieniu: fragmenty danych z pamięci (np. zmienna) są przesyłane do pliku. 

Istnieją trzy podstawowe tryby otwarcia strumienia:
    • tryb odczytu: strumień pozwala tylko na operacje odczytu; próba zapisu w strumieniu spowoduje wyjątek 
      (wyjątek ma nazwę UnsupportedOperation, który dziedziczy OSError i ValueError, i pochodzi z modułu io)
    • tryb zapisu: strumień otwarty w tym trybie umożliwia tylko operacje zapisu,
      próba odczytania strumienia spowoduje w/w wyjątek, 
    • tryb aktualizacji: strumień otwarty w tym trybie pozwala na zarówno zapis, jak i odczyt.
 
Każdy plik jest ukryty za obiektem odpowiedniej klasy.
Obiekt jest tworzony gdy otwieramy plik i usuwany momencie zamknięcia.

Funkcja open() - tworzy obiekt (nie konstruktor)
Funkcja close() - zamyka

Strumienie mogą być:
- tekstowe (zawierają tekst ułożony w rzędy odczytywany znak po znaku lub liniami|)
- binarne (zawierają dowolne ciągi bajtów)
 
Znak końca linii w windows: \r\n
Znak końca linii w unix: \n

W środowisku Windows, zachodzi tłumaczenie znaków nowej linii: gdy odczytujemy linię z pliku, każda para znaków \r\n 
jest automatycznie zamieniana na pojedynczy znak \n, podczas zapisu, każdy znak \n jest zamieniany na parę znaków \r\n; 
#-------------------------------------

stream = open(plik, tryb = 'r', kodowanie = None) 

• jeśli otwarcie się powiedzie, funkcja zwraca obiekt strumienia; w przeciwnym razie powstaje wyjątek (np. FileNotFoundError)
• pierwszy parametr funkcji (plik) określa nazwę pliku; 
• drugi parametr (tryb) określa tryb otwarty używany dla strumienia; jest łańcuchem znaków wypełnionym sekwencją znaków, 
  a każda z nich ma swoje specjalne znaczenie (więcej szczegółów wkrótce); 
• trzeci parametr (kodowanie) określa typ kodowania (np. UTF-8 podczas pracy z plikami tekstowymi) 
• otwarcie musi być pierwszą operacją wykonywaną w strumieniu. 
• argumenty tryb i kodowanie można pominąć - przyjmowane są wtedy ich wartości domyślne. 
  Domyślnym trybem otwierania jest odczyt w trybie tekstowym, a domyślne kodowanie zależy od używanej platformy.

Tryby:
r  odczyt (ang. read)
    • strumień zostanie otwarty w trybie odczytu; 
    • plik powiązany ze strumieniem musi istnieć i musi być czytelny, w przeciwnym razie funkcja open() zgłasza wyjątek. 
w  zapis (ang. write)
    • strumień zostanie otwarty w trybie zapisu; 
    • plik powiązany ze strumieniem nie musi istnieć; jeśli nie istnieje, zostanie utworzony; jeśli istnieje, 
      zostanie obcięty do długości zera (skasowany); 
      jeśli utworzenie nie jest możliwe (np. z powodu uprawnień systemu) funkcja open() zgłasza wyjątek. 
a  dopisywanie (ang. append)
    • strumień zostanie otwarty w trybie dopisywania; 
    • plik powiązany ze strumieniem nie musi istnieć; jeśli nie istnieje, zostanie stworzony; 
      jeśli istnieje, wirtualna zapisująca głowica zostanie ustawiona na końcu pliku (poprzednia zawartość pliku pozostaje nietknięta). 
r+ odczyt i aktualizacja (ang. read and update)
    • strumień zostanie otwarty w trybie odczytu i aktualizacji; 
    • plik powiązany ze strumieniem musi istnieć i musi być zapisywalny, w przeciwnym razie funkcja open() zgłasza wyjątek; 
    • zarówno operacje odczytu, jak i zapisu są dozwolone dla strumienia. 
w+ zapis i aktualizacja (ang. write and update)
    • strumień zostanie otwarty w trybie zapisu i aktualizacji; 
    • plik powiązany ze strumieniem nie musi istnieć; jeśli nie istnieje, zostanie stworzony; poprzednia zawartość pliku pozostaje nietknięta; 
    • zarówno operacje odczytu, jak i zapisu są dozwolone dla strumienia. 

Jeśli na końcu łańcucha trybów znajduje się litera b, oznacza to, że strumień ma zostać otwarty w trybie binarnym.
Jeśli łańcuch trybu kończy się literą t, strumień jest otwierany w trybie tekstowym (domyślnie).

Otwarcie pliku ustawi bieżącą pozycję pliku (wirtualną głowicę do odczytu/zapisu) przed pierwszym bajtem pliku 
jeśli tryb NIE jest ustawiony na a i po ostatnim bajcie pliku jeśli tryb JEST ustawiony na a.

Tryb tekstowy	Tryb binarny	Opis
	rt	    rb		odczyt
	wt	    wb		zapis
	at	    ab		dopisywanie
	r+t	    r+b		odczyt i aktualizacja
	w+t	    w+b		zapis i aktualizacja

Można też otworzyć plik do wyłącznego tworzenia za pomocą trybu otwartego x. 
Jeśli plik już istnieje, funkcja open() zgłosi wyjątek.

try: 
    strumien = open("C:\\Users\\admin\\Desktop\\Plik.txt", "rt")
    # przetwarzanie
    strumien.close() 
except Exception as exc: 
    print("Nie mozna otworzyc pliku:", exc)  
#----------------------------------
3 strumienie są standardowo otwarte i nie wymagają żadnych dodatkowych przygotowań:
    • sys.stdin (czyli standard input).  Jest zwykle związany z klawiaturą, wstępnie otwarty do odczytu 
        i traktowany jako główne źródło danych dla uruchomionych programów; Funkcja input() domyślnie odczytuje dane z stdin. 
    • sys.stdout (czyli standard output). Jest zwykle związany z ekranem, wstępnie otwarty do zapisu, 
          uważany za główny cel dla wyprowadzania danych przez działający program; Funkcja print() przekazuje dane do strumienia stdout. 
    • sys.stderr (czyli standard error output). Jest zwykle związany z ekranem, wstępnie otwarty do zapisu, uważany za główne miejsce, 
          do którego uruchomiony program powinien przesyłać informacje o błędach napotkanych podczas pracy; 
          Separacja stdout (użyteczne wyniki generowane przez program) od stderr (komunikaty o błędach) daje możliwość przekierowania tych dwóch rodzajów informacji 
          do różnych miejsc docelowych.
#----------------------------------
Zamknięcie strumienia: stream.close().
    • funkcja nie oczekuje żadnych argumentów; strumienia nie trzeba otwierać 
    • funkcja nie zwraca nic, ale w razie błędu zgłasza wyjątek IOError; 
    • funkcja close() zazwyczaj kończy się sukcesem, ale:
	jeśli strumień został otwarty do zapisu, a następnie przeprowadzono serię operacji zapisu, 
        może się zdarzyć, że dane wysłane do strumienia nie zostały jeszcze przesłane do urządzenia fizycznego 
        (z powodu mechanizmu zwanego cachowaniem lub buforowaniem). 
        Ponieważ zamknięcie strumienia zmusza bufory do ich opróżnienia, może się zdarzyć, że opróżnienie się nie powiedzie 
        i dlatego też close() również się nie powiedzie. 
    • brak zamknięcia strumienia może spowodować niewyłanie do pliku zawartości buforów
#----------------------------------

Właściwość errno (przykł.poniżej):

try: 
    strumien = open("C:\\Users\\admin\\Desktop\\Plik.txt", "rt")
    # przetwarzanie
    strumien.close() 
except IOError as exc: 
    print("Nie mozna otworzyc pliku:", exc) 

Wybrane stałe:
errno.EACCES → Permission denied	 Błąd występuje np. przy próbie otwarcia do zapisu, pliku z atrybutem tylko do odczytu.
errno.EBADF → Bad file number		 Błąd występuje np. przy próbied działania na nieotwartym strumieniu.
errno.EEXIST → File exists		 Błąd występuje np. przy próbie zmiany nazwy pliku na poprzednią nazwę
errno.EFBIG → File too large		 Błąd występuje np. przy próbie utworzenia pliku większego niż maksymalny dozwolony przez system operacyjny.
errno.EISDIR → Is a directory		 Błąd występuje przy próbie użycia katalogu jak zwykłego pliku.
errno.EMFILE → Too many open files	 Błąd występuje przy próbie otwarcia jednocześnie więcej strumieni niż jest to dozwolone dla systemu operacyjnego.
errno.ENOENT → No such file or directory Błąd występuje przy próbie uzyskania dostępu do nieistniejącego pliku/katalogu. 
errno.ENOSPC → No space left on device   Błąd występuje, gdy na nośniku nie ma wolnego miejsca.

#Przykład:
import errno, os
try:
    s = open("C:\\Users\\admin\\Desktop\\Plik.txt", "rt")
    # przetwarzanie
    s.close()
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("Plik nie istnieje.")
    elif exc.errno == errno.EMFILE:
        print("Otworzyles zbyt wiele plikow.")
    else:
        print("Numer błędu:", exc.errno)
        #print("Plik nie mogl zostac otwarty:", os.strerror(exc.errno))  #<- lub tak:

Funkcja strerror() z modułu os upraszcza kod obsługi błędów i wymaga ona tylko jednego argumentu - numeru błędu:
Uwaga: przekazanie nieistniejącgo kodu błędu spowoduje, że funkcja zgłosi wyjątek ValueError.

#-------------------------------
Przetwarzanie plików tekstowych:

strumien = open('file.txt', 'rt', encoding='utf-8')  # UTF-8

Funkcja read() pozwala:
    • odczytać pożądaną liczbę znaków (w tym tylko jeden) z pliku i zwrócić je jako łańcuch znaków
    • odczytać całą zawartość pliku i zwrócić ją jako łańcuch znaków
    • jeśli nie ma już nic więcej do odczytu, funkcja zwraca pusty łańcuch

from os import strerror
try:
    licznik = 0
    s = open('C:\\Users\\admin\\Desktop\\Plik.txt', "rt") , encoding='utf-8')
    zn = s.read(1)  # 10

    while zn != "":
        print(zn, end="")
        licznik += 1
        zn = s.read(1)  #10

    s.close()
    print("\nZnaki w pliku:", licznik)

except IOError as e:
    print("Blad I/O: ", strerror(e.errno)) 

Jeśli masz ABSOLUTNĄ PEWNOŚĆ, że długość pliku jest bezpieczna i możesz od razu odczytać cały plik do pamięci, 
możesz to zrobić - funkcja read(), wywołaną bez żadnych argumentów.
Odczytanie jednak pliku długiego na terabajt za pomocą tej metody może spowodować błąd alokacji pamięci.

Wczytanie całości, drukowanie po znaku:
from os import strerror
try:
    licznik = 0
    s = open('C:\\Users\\admin\\Desktop\\Plik.txt', encoding='utf-8')
    zawartosc = s.read()
    for zn in zawartosc:
        print(zn, end='')
        licznik += 1
    s.close()
    print("\nZnaki w pliku:", licznik)
except IOError as e:
    print("Blad I/O: ", strerror(e.errno))

#Wczytanie i drukowanie całości:

from os import strerror
try:
    licznik = 0
    s = open('C:\\Users\\admin\\Desktop\\Plik.txt', "rt", encoding='utf-8')
    zawartosc = s.read()
    print(zawartosc, end='')
    s.close()
except IOError as e:
    print("Blad I/O: ", strerror(e.errno))
#----------------------------------
Funkcja readline() - plik jako zbiór linii (nie sekwencja znaków):
Funkcja próbuje odczytać kompletną linię tekstu z pliku.

from os import strerror
try:
    licznikZn = licznikL = 0
    s = open("C:\\Users\\admin\\Desktop\\Plik.txt", "rt")
    linia = s.readline()
    while linia != '':
        licznikL += 1
        print(linia, end = '')
        linia = s.readline()
    s.close()
    print("Linie w pliku:     ", licznikL)
except IOError as e:
    print("Blad I/O:", strerror(e.errno))
#------------------------------------
Metoda readlines(), po wywołaniu bez argumentów, próbuje odczytać całą zawartość pliku 
i zwraca listę łańcuchów znaków, po jednym elemencie na linię pliku.
Gdy nie ma nic do odczytania z pliku, metoda zwraca pustą listę - można tego użyć, aby wykryć koniec pliku.

from os import strerror
try:
    licznikZn = licznikL = 0
    s = open('C:\\Users\\admin\\Desktop\\Plik1.txt', 'rt', encoding='utf-8')
    linie = s.readlines(5)  # 5 linii
    while len(linie) != 0:
        for linia in linie:
            licznikL += 1
            print(linia, end='')
        linie = s.readlines(5)
    s.close()
    print("\nLinie w pliku:     ", licznikL)
except IOError as e:
    print("Blad I/O:", strerror(e.errno))

#-----------------------------------------
#Metoda write() - porzebuje tylko 1 parametru - łańcucha znaków do zapisania)

from os import strerror
try:
    Plik = open('C:\\Users\\admin\\Desktop\\NowyPlik.txt', 'wt') # utworono nowy plik (nowytxt.txt)
    for i in range(10):
        s = "linia #" + str(i+1) + "\n"
        for zn in s:         # można bez tej pętli zapisywać całymi liniami
            Plik.write(zn)   # Plik.write(s)
    Plik.close()  # zró uwagę na wcięcia!!!
except IOError as e:
    print("Blad I/O: ", strerror(e.errno))

Metody write() można użyć do zapisu w strumieniu stderr, ale nie należy jej otwierać, ponieważ jest ona zawsze
otwarta niejawnie. Np, jeśli chcemy wysłać łańcuch znaków do stderr w celu odróżnienia go od normalnego wyniku 
programu, może to wyglądać tak:
import sys 
sys.stderr.write("Komunikat o bledzie")
#--------------------------------------
bytearray - jedna ze specjalistycznych klas używanych przez Python do przechowywania bezpostaciowych danych.
Dane bezpostaciowe to dane, które nie mają określonego kształtu ani formy -tylko serię bajtów (np pliki grafiki)

data = bytearray(10) - Takie wywołanie tworzy obiekt bytearray, który może przechowywać dziesięć bajtów.
Uwaga: konstruktor wypełnia całą tablicę zerami.

Bytearray przypomina listę: 
-jest mutowalna, 
-jest przedmiotem funkcji len() 
-można uzyskać dostęp do jej elementów za pomocą indeksowania.
-nie można ustawiać żadnych elementów tablicy bajtowej o wartości, która nie jest liczbą całkowitą (TypeError) 
-nie można przypisać wartości, która nie pochodzi z zakresu od 0 do 255 włącznie (ValueError.)
-można traktować elementy tablicy bajtowej jako wartości całkowite 

Jak zapisać tablicę bajtów w pliku binarnym:
    • inicjujemy bytearray z określonymi wartościami; 
    • tworzymy plik za pomocą funkcji open() - jedyną różnicą w stosunku do pliku tekstowego
      jest tryb otwarty zawierający flagę b; 
    • metoda write() przyjmuje swój argument (bytearray) i wysyła go (jako całość) do pliku; 
    • zamykany strumień;

Metoda write() zwraca liczbę poprawnie zapisanych bajtów
Jeśli wartości różnią się od długości argumentów metody, może ona zasygnalizować błędy zapisu.
Nie zawsze musimy wykorzystać wynik.

from os import strerror
dane = bytearray(10)
for i in range(len(dane)):
    dane[i] = 10 + i
try:
    bf = open('C:\\Users\\admin\\Desktop\\NowyPlikB.txt', 'wb')
    bf.write(dane)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

#LUB:
from os import strerror
dane = bytearray(10)
ileb = 0
for i in range(len(dane)):
    dane[i] = 10 + i
try:
    bf = open('C:\\MN\\NowyPlikB.txt', 'wb')
    ileb=bf.write(dane)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
print('Zapisano:', ileb, 'bajtów')
#-------------------------------------------------

Odczyt z pliku binarnego:

from os import strerror
dane = bytearray(10)
try:
    bf = open('C:\\Users\\admin\\Desktop\\NowyPlik.txt', 'rb')
    bf.readinto(dane)
    bf.close()
    for b in dane:
        print(hex(b), end=' ')     #print(chr(b), end=' ')
except IOError as e:    
    print("Blad I/O:", strerror(e.errno))

#LUB:
from os import strerror
dane = bytearray(10)
try:
    bf = open('C:\\Users\\admin\\Desktop\\NowyPlik.txt', 'rb')
    ileb=bf.readinto(dane) ###
    bf.close()
    print(ileb)            ###
    for b in dane:
        print(hex(b), end=' ')
except IOError as e:
    print("Blad I/O:", strerror(e.errno))

#LUB:

from os import strerror
try:
    bf = open('file.bin', 'rb')
    dane = bytearray(bf.read())  # rozmiar tablicy wzięty z odczytanego strumienia
                                 # trzeba mieć pewność, że nie zabraknie pamięci
    #dane = bytearray(bf.read(8)) # można podać max liczbę bajtów do odczytania  
                   		 # reszta bajtów nadal czaka na odczyt (należy to zrtobić w pętli)
    #print(len(dane))		 # wyświetlenie liczby faktycznie odczytanych bajtów

    bf.close()
    for b in dane:
        print(hex(b), end=' ')
except IOError as e:
    print("Blad I/O:", strerror(e.errno)) 

---------------------------------------------
'''




