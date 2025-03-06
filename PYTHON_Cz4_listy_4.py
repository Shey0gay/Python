'''
#Listy: #Numerowanie elementów od zera

numbers = [10, 5, 7, 2, 1]
print("Oryg.lista:", numbers)  

numbers[0] = 111
print("Nowa lista: ", numbers)  

numbers[1] = numbers[4] 
print("Nowsza lista:", numbers) 

print("\nDługość listy:", len(numbers)) 

del numbers[1]  #Usunięcie elementu nr 1
print("Nowy rozmiar listy:", len(numbers))  
print("\nNowa zawartość listy:", numbers)  

# nie można odwołać się do nieistniejącego elelmentu listy:
#print(numbers[4])
#numbers[4] = 1

numbers = [111, 7, 2, 1]
print(numbers[-1])
print(numbers[-3])
print(numbers[-4])

#---------------------------------------
# FUNKCJE i METODY:
# Metoda jest specyficznym rodzajem funkcji - zachowuje się jak funkcja i wygląda 
# jak funkcja, ale różni się sposobem działania i stylem wywołania.

# Funkcja nie należy do żadnych danych - pobiera dane, może tworzyć nowe dane 
# i (generalnie) daje wynik.

# Metoda robi wszystkie te rzeczy, ale jest również w stanie zmienić stan wybranej 
# jednostki.

# Właścicielem metody są dane, dla których działa, a funkcja jest własnością całego 
# kodu. 

# Wywoływanie metody wymaga pewnej specyfikacji danych, z których wywoływana jest metoda.
# Typowe wywołanie funkcji wygląda tak: wynik = funkcja(arg)
# Funkcja pobiera argument, robi coś i zwraca wynik.

# Typowe wywołanie metody zwykle wygląda tak: wynik = data.method(arg)
# Uwaga: nazwa metody poprzedzona jest nazwą danych, do których należy metoda. 
# Następnie dodajesz kropkę, po której następuje nazwa metody i para nawiasów 
# zawierających argumenty.
# Metoda będzie zachowywać się jak funkcja, ale może zrobić coś więcej - może zmienić 
# wewnętrzny stan danych, z których została wywołana. 

numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

numbers.append(4)
print(len(numbers))
print(numbers)

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

numbers.insert(2, 333)
print(len(numbers))
print(numbers)

numbers.insert(-1, 444)  # ???
print(len(numbers))
print(numbers)


my_list = []  # utworzenie pustej listy
for i in range(5):
    my_list.append(i + 1)
print(my_list)


my_list = []  # utworzenie pustej listy
for i in range(5):
    my_list.insert(0, i + 1)
print(my_list)

#liczenie sumy 1:
my_list = [10, 1, 8, 3, 5]
total = 0
for i in my_list:
    total += i
print(total)


#liczenie sumy 2:
my_list = [10, 1, 8, 3, 5]
total = 0
for i in range(len(my_list)):
    total += my_list[i]
print(total)

x = [1, "234",  3.0, 17,  [123, 345, [9, "sdas"]]]
print(x[-1][2][1])

#----------------------------------------------------------
Zamiana wartości:
var1 = 1
var2 = 2

aux = var1
var1 = var2
var2 = aux

# ale lepiej tak:
var1 = 1
var2 = 2

var1, var2 = var2, var1

# albo tak:
my_list = [10, 1, 8, 3, 5]
length = len(my_list)
for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
print(my_list)

#----------------------------------------------------------

#Ćwiczenie 1:
lst = [1, 2, 3, 4, 5]
lst.insert(1, 6)
del lst[0]
lst.append(1)
print(lst)

#Ćwiczenie 2:
lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0

for number in lst:
    add += number
    lst_2.append(add)
print(lst_2)

#Ćwiczenie 3:
lst = []
#del lst
print(lst)

#Ćwicznie 4:
lst = [1, [2, 3], 4]
print(lst[1])
print(len(lst))

#----------------------------------

#Sortowanie bąbelkowe:
my_list = [8, 10, 6, 2, 4]  # list to sort
swapped = True  # It's a little fake, we need it to enter the while loop.
while swapped:
    swapped = False  # no swaps so far
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # a swap occurred!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
print(my_list)

# ale lepiej tak:
my_list = [8, 10, 6, 2, 4]  # list to sort
my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)

#=======20241010==============2P1=====

# Jaki będzie wynik?   
list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)

# Kopia całej listy
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Kopia części listy.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

# ujemne indeksy:
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)

# Jaki będzie wynik?
my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print(new_list)

# Jaki będzie wynik?
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)

# Jaki będzie wynik?
my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list)

# Jaki będzie wynik?
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)

# Jaki będzie wynik?
my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)

# Jaki będzie wynik?
my_list = [10, 8, 6, 4, 2]
#del my_list
print(my_list)

my_list = [0, 3, 12, 8, 2]
print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)

#---------------------------------------

#Przykład 1 
#Znajdź największy element:

my_list = [17, 3, 11, 5, 108, 9, 7, 15, 13]
largest = my_list[0]
for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]
print(largest)

# lub lepiej:
my_list = [17, 3, 11, 55, 1, 9, 7, 15, 13]
largest = my_list[0]
for i in my_list[1:]:
    if i > largest:
        largest = i
print(largest)


#------------------------------

#Przykład 2
# gdzie jest Nemo:
my_list = ['Ala', 'Ela', 'Ola', 'Ula', 'Nemo', 'Iza', 'Ania']
to_find = 'Nemo'
found = False
for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break
if found:
    print("Nemo znaleziony na pozycji", i)
else:
    print("nima")

#--------------------------------
#Przykład 3
# Lotto:

skreślono  = [5, 11, 9, 42, 3, 49]
wylosowano = [3, 7, 11, 42, 34, 49]
trafiono   = 0

for number in wylosowano:
    if number in skreślono:
        trafiono += 1

print(trafiono)

#-------------------------
# Eliminacja powtórzeń:    To można dać na sprawdzian (nie pokazałem wyniku na lekcji)
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []
for number in my_list:  # Browse all numbers from the source list.
	if number not in new_list:  # If the number doesn't appear within the new list...
		new_list.append(number)  # ...append it here.
my_list = new_list[:]  # Make a copy of new_list.
print("The list with unique elements only:")
print(my_list)

#---------------------------------------
# Ćwiczenie 5:
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2
del list_1[0]
del list_2[0]
print(list_3)

# Ćwiczenie :
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2

print(list_3)

# Ćwiczenie 7:
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[:]

print(list_3)

# Ćwiczenie 8:
list_1 = ["A", "B", "C"]
list_2 = list_1[:]
list_3 = list_2[:]

del list_1[0]
del list_2[1]
print(list_1)
print(list_2)
print(list_3)


# Ćwiczenie 9:
#Jakiego należy użyć operatora?:
my_list = [1, 2, "in", True, "ABC"]

print(1 ??? my_list)      # outputs True
print("A" ??? my_list)    # outputs True
print(3 ??? my_list)      # outputs True
print(False ??? my_list)  # outputs False

my_list = [1, 2, "in", True, "ABC"]

print(1 in my_list)        # outputs True
print("A" not in my_list)  # outputs True
print(3 not in my_list)    # outputs True
print(False in my_list)    # outputs False

#---------------------------------
#Listy w listach:
row = []
for i in range(8):
    row.append('XYZ')
print(row)
#---------------------------------
dwójki = [2 ** i for i in range(10)]
print(dwójki)

#---------------------------------
squares = [x ** 2 for x in range(10)]
print(squares)

odds = [x for x in squares if x % 2 != 0 ]
print(odds)

#---------------------------------
# Listy 2 wymiarowe:
board = []
for i in range(5):
    row = ['X' for i in range(8)]
    board.append(row)
#print(row)
print(board)

# lub:
board = [['X' for i in range(8)] for j in range(8)]
print(board)
'''
2024-10-17===================
#---------------------------------



'''
