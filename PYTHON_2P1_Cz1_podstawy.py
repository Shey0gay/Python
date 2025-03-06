'''
Pycharm
IDLE

ZALETY
KOMPILACJA
    • wykonywanie przetłumaczonego kodu jest zazwyczaj szybsze,
    • tylko programista musi mieć kompilator - użytkownik końcowy może
      używać tego kodu bez niego,
    • przetłumaczony kod jest przechowywany w języku maszynowym - ponieważ
      bardzo trudno go zrozumieć, twoje własne wynalazki i sztuczki
      programistyczne prawdopodobnie pozostaną twoją tajemnicą.
INTERPRETACJA
    • możesz uruchomić kod zaraz po jego zakończeniu - nie ma dodatkowych
      etapów tłumaczenia,
    • kod jest przechowywany za pomocą języka programowania,
      a nie języka maszynowego - oznacza to,
      że można go uruchomić na komputerach używających różnych
      języków maszynowych; nie kompilujesz kodu
      osobno dla innej architektury.

WADY
KOMPILACJA
    • sama kompilacja może być bardzo czasochłonna - możesz nie być
      w stanie uruchomić swojego kodu
      natychmiast po każdej zmianie,
    • musisz mieć tyle kompilatorów, ile platform sprzętowych,
      na których chcesz uruchomić twój kod.
INTERPRETACJA
    • nie oczekuj, że interpretacja sprawi, że twój kod będzie szybszy
      - twój kod podzieli moc komputera
      z interpreterem, więc nie może być naprawdę szybki,
    • zarówno ty, jak i użytkownik końcowy, musicie mieć interpreter
      do uruchomienia kodu.

#======================================================

end="\n" - default
sep=" "  - default

print('Hello ', end='')
print('Python')

print("Hello", "Python!", sep=" ", end = "\n")
print("Hello", "Python!", sep=",", end = "")
print("Hello", "Python!", sep=":", end = "=")

print("Halo", "Pyton!", sep="\n")
print("Halo\nPyton!")

print("\t")
print("\\")
print("\"")
print("I like \"Monty Python\"")
print('I like "Monty Python"')

#2024.09.05

#Wyświetlić jednym printem:
"I'm"
""learning""
"""Python"""

Odp.:
print("\"I'm\"\n\"\"learning\"\"\n\"\"\"Python\"\"\"")

print("Programming","Essentials","in", sep="***", end="...")
print("Python")

REPLIKACJA:

print("ABCD"*5)

#Kwadrat:
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 4, end="")
print("+" + 10 * "-" + "+")


#123 is a literal, and c is not.

print(555,555)
print(-555_555)
print(+555.555)
#print(555 555)

print(3E8)
#    the exponent (the value after the E) has to be an integer;
#    the base (the value in front of the E) may be an integer.

print(6.62607E-34)
print(0.0000000000000000000001, 1e-22)

print(0X123)
print(0x123)
print(0o123)
print(0b1100)
print(bin(10000)[2:])

print(2.5)
print(-0.4)
print(.4)
print(4.)

#Boolean:
print(True > False)
print(True < False)

#Jakie to typy: "1.5", 2.0, 528, False 

Operatory: +, -, *, /, //, %, **
print(2+3)

#Sprawdź typ wyniku podstawiając różne operatory:
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

print(7 / 3)
print(7 / 3.)
print(7. / 3)
print(7. / 3.)
print(6 / 3)

print(7 // 3)
print(7 // 3.)
print(7. // 3)
print(7. // 3.)

print(-7 // 3)
print(-7 // 3.)
print(-7. // 3)
print(-7. // 3.)

print(-7 % 3)
print(-7 % 3.)
print(-7.  % 3)
print(-7. % 3.)

print(14 % 4)

bo: 14 // 4 gives 3 → this is the integer quotient;
    3 * 4 gives 12 → as a result of quotient and divisor multiplication;
    14 - 12 gives 2 → this is the remainder.

print(12 % 4.5)
#print(12 //4.5)
What is the result ? 3.0 - not 3 but 3.0 
the rule still works: 
     12 // 4.5 gives 2.0; 
     2.0 * 4.5 gives 9.0; 
     12 - 9.0 gives 3.0

Kolejność:
print(2 + 3 * 5)
print(9 % 6 % 2)   #od lewej
print(2 ** 2 ** 3) #od prawej

----------------------
Zmienna ma:
    nazwa (duże lub małe litery, cyfry i znak "_") 
           Musi się zaczynać od litery . "_" jest literą
           duże i małe litery są rozróżniane
           nie mogą być takie same jak słowa kluczowe
    wartość

OK: MyVariable, i, t34, Exchange_Rate, counter, days_to_christmas, theNameIsSoLongThatYouWillMakeMistakesWithIt, _.
OK: Adiós_Señora, sûr_la_mer, Einbahnstraße, переменная. 
--------
Exercise 2. Which of the following variable names are illegal in Python?
my_var
m
101
averylongvariablename
m101
m 101
Del
del

#-----------------------------------

Rekomendowane:
  małe litery  (ew. cammel back)
  funkcja tak samo jak zmienne

SŁOWA KLUCZOWE: 'False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 
                'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 
                'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 
                'return', 'try', 'while', 'with', 'yield'

nie można nazwać zmiennej def , ale można Def, DEF, dEf itp.

#Ile wyświetli: 
var = 100
var = 200 + 300
print(var)

#Ile wyświetli:
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)

#Operatory skrócone:

x = x * 2         	-> x *= 2
sheep = sheep + 1 	-> sheep += 1
i = i + 2 * j           => i += 2 * j
var = var / 2           => var /= 2
rem = rem % 10          => rem %= 10
j = j - (i + var + rem) => j -= (i + var + rem)
x = x ** 2              => x **= 2

----------------------------------
# Exercise 1. What is the output of the following snippet?
var = 2
var = 3
print(var)


#Exercise 3. What is the output of the following snippet?
a = '1'
b = "1"
print(a + b)
print(5 * a + b)

#Exercise 4. What is the output of the following snippet?
a = 6
b = 3
a /= 2 * b
print(a)


---------2.5.1.1-----------------------------
Komentarze: od # do końca linii  (CTRL + / ale w IDLE nie działa)

Przykład przegadanego kodu:
#this program computes the number of seconds in a given number of hours
# this program has been written two days ago
a = 2 # number of hours
seconds = 3600 # number of seconds in 1 hour
print("Hours: ", a) #printing the number of hours
# print("Seconds in Hours: ", a * seconds) # printing the number of seconds in a given number of hours
#here we should also print "Goodbye", but a programmer didn't have time to write any code
#this is the end of the program that computes the number of seconds in 3 hour

Lepsze są znaczące nazwy zmiennych (self-commenting)


--------2.6.1.1-------------------------
#Funkcja input:

print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")


fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")


#Teraz liczba:
anything = input("Enter a number: ")
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

Dlaczego błąd?
Bo brak konwersji typów.

anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)


y = 3x3 - 2x2 + 3x - 1

Przykład1:
    

print("Program liczący wartość funkcji y=3x3-2x2+3x-1")
x=float(input("Wprowadź wartość x="))
print("y=", 3 * x ** 3 - 2 * x ** 2 + 3 * x - 1)
print("y= %s" % (3 * x ** 3 - 2 * x ** 2 + 3 * x - 1))
print("y=  {}".format(3 * x ** 3 - 2 * x ** 2 + 3 * x - 1))

print("y= %s %s" % (3 * x ** 3 - 2 * x ** 2 + 3 * x - 1, 100))
print("y=  {} {}".format(3 * x ** 3 - 2 * x ** 2 + 3 * x - 1, 100))
'''
#funkcja anonimowa lambda (dykteryjka):
prin("lambda: y=", (lambda x: 3 * x ** 3 - 2 * x ** 2 + 3 * x - 1)(5))
print((lambda x, y: x**y)(2,10))


print("1 po angielsku: %s \n2 po angielsku: %s" % ('one', 'two'))
print("1 po angielsku: {} \n2 po angielsku: {}".format('one', 'two'))
print("Cyfra %d poprzedza %d" % (7, 8))

#Ten zapis „mówi” Pythonowi:
#%6.3f – przeznacz 6 znaków na zapisanie liczby zmiennoprzecinkowej, z czego 3 będą po kropce
#%16s – przeznacz 16 znaków na zapisanie string’a
#%10s – przeznacz 10 znaków na zapisanie string’a

print("Rekord świata na 100m to %f ustanowił go %s" % (9.58, 'Usain Bolt'))
print("Rekord świata na 100m to %.2f ustanowił go %s" % (9.5877, 'Usain Bolt'))
print("Rekord świata na 100m padł %s i wynosi poniżej %.1f sekund - wow!" % ('16 sierpnia 2009', 9.58))
print("Rekord świata na 100m to {} ustanowił go {}".format(9.58, 'Usain Bolt'))
print("Rekord świata na 100m to {:.2f} ustanowił go {}".format(9.5877, 'Usain Bolt'))
print("Rekord świata na 100m padł {} i wynosi poniżej {:.1f} sekund - wow!".format('16 sierpnia 2009', 9.58))

--------------
x = int(input("Enter a number: ")) # The user enters 2
print(x * "5")
--------------
x = input("Enter a number: ") # The user enters 2
print(type(x))
--------------

y=ax2+bx+c
dlt=b**2-4ac
x1= (-b - dlt ** .5) / 2a
x2= (-b + dlt ** .5) / 2a

#-------------
# =  przypisanie
# == porównanie
print(2 == 2)
print(2 == 2.0)

Priorytet 	Operator 	
1 		+, - 		1 arg.
2	 	** 	
3 		*, /, //, % 	
4	 	+, - 		2 arg.
5 		<, <=, >, >= 	
6	 	==, !=


#========= ĆWICZENIE 1 ================
#Mile na kilometry:  
kilometers = 12.25
miles = 7.38

miles_to_kilometers = ###
kilometers_to_miles = ###

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

Rozwiązanie:
miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

#========= ĆWICZENIE 2 ================
Oblicz: y = 3x3 - 2x2 + 3x - 1 dla różnych wartości x:
x = 3
#x = float(x)  # jeśli chcemy wynik w float
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

#========= ĆWICZENIE 3 ================
#Przeciwprostokątna: podaj długości boków
leg_a = float(input("1 przyprostokątna: "))
leg_b = float(input("2 przyprostokątna: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Przeciwprostokątna", hypo)   # lub print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))

#========= ĆWICZENIE 4 ================

2024-09-12:


#Taki sobie kalkulator: (rózne działania na 2 liczbach)

a = float(input("Podaj a: "))
b = float(input("Podaj b: "))

#========= ĆWICZENIE 5 ================

#Start o określonej godz+min, i trwanie w minutach. Oblicz czas zakończenia:
hour = int(input("Start (godz): "))
mins = int(input("Start (minuty): "))
trwanie = int(input("Czas trwania (minuty): "))


'''

