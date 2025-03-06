#Funkcja funkcji: DEKOMPOZYCJA KODU
#Skąd się biorą:
# - integralna część Pythona (funkcje wbudowane, np.print(), input())
# - preinstalowane moduły
# - definiowane przez programistów
# - funkcje anonimowe lambda  # print((lambda x, y: x**y)(2,10))
# - metody w klasach
'''
def funkcja(par1, par2):
    print("111")
    #return None
    print("222")
    print(par1)
    print("333")
    return par2 *2, par1 *2
    print("444")

print('Przed wywołaniem funkcji')
x,y  = funkcja("NAPIS", 7)
print(x, y)        		# lub od razu print(funkcja("NAPIS", 7)
print('Po wywołaniu funkcji')

x = funkcja("NAPIS", 7) #ciekawe wywołanie
print(x) 

# funkcje można redefiniować 

def input(par1):
    return par1 + 1
print(input(3))   

# Parametry pozycyjne (title, positional parameters):
def funkcja(par1, par2, par3):
    print(par1,par2,par3)
funkcja(3,5,7)

# Parametry predefiniowane:
def funkcja(par1=2, par2=4, par3=6):
    print(par1,par2, par3)
funkcja(3,5,7)

def funkcja(par1=2, par2=4, par3=6):
    print(par1,par2, par3)
funkcja(3)

def funkcja(par1=2, par2, par3=6):
    print(par1,par2, par3)
funkcja(3,5)

def funkcja(par1=2, par2=4, par3=6):
    print(par1,par2,par3)
funkcja(3,5,7)

# Parametry nazwane (keyword parameters)
def funkcja(par1=2, par2=4, par3=6):
    print(par1,par2, par3)
funkcja(33,par3=55,par2=13)

def funkcja(par1=2, par2=4, par3=6):
    print(par1,par2, par3)
funkcja(33,77,par3=55)

# Parametry pozycyjne muszą być przed nazwanymi
# Parametry pozycyjne muszą być przed predefiniowanymi

#--------------------------------------
# RETURN:
# Brak return
# Return bez wartości ( zwraca None)
# Return z wartością

def happy_new_year(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return
    print("Happy New Year!")

happy_new_year(False)
happy_new_year()
#----------------------

# None - wynik użyteczny w 2 przypadkach:
value = None        #1 przypisanie do zmiennej
if value is None:   #2 porównanie
    print("Sorry, you don't carry any value")

# Uwaga: Jeśli funkcja nic nie zwraca, lub zawiera tylko return, to zwraca None:
def fun1():
    print("Zwracam None!")

def fun2():
    print("Zwracam None!")
    return

def fun3():
    print("Zwracam None!")
    return None

print(fun1(), fun3(), fun3())

#-----------------------
def strange_function(n):
    if(n % 2 == 0):
        return True
print(strange_function(2))
print(strange_function(1))
#---------------------------------------------------
2024-10-31:
# funkcje i listy:
def list_sum(lst):
    s = 0
    for elem in lst:
        s += elem
    return s

print(list_sum([5, 4, 3]))
#---------------------------------------------------
def strange_list_fun(n):
    strange_list = []
    for i in range(0, n):
        strange_list.insert(0, i)
    return strange_list
print(strange_list_fun(5))

#--------------------------------------------------

#Ćwiczenie 1: Jaki będzie wynik:
def is_int(data):
    if type(data) == int:
        return True
    elif type(data) == float:
        return False

print(is_int(5))
print(is_int(5.0))
print(is_int("5"))

(TFN)

#Ćwiczenie 2: Jaki będzie wynik:
def even_num_lst(ran):
    lst = []
    for num in range(ran):
        if num % 2 == 0:
            lst.append(num)
    return lst
print(even_num_lst(11))

[0,2,4,6,8,10]

#Ćwiczenie 3: Jaki będzie wynik:
def list_updater(lst):
    upd_list = []
    for elem in lst:
        elem **= 2
        upd_list.append(elem)
    return upd_list
foo = [1, 2, 3, 4, 5]
print(list_updater(foo))

[1, 4, 9, 16, 25]

#--------------------------------------------------

#ZAKRESY:

def scope_test():
    x = 123
scope_test()
print(x)  # zmienna x żyje tylko tylko z funkcji
#-------------------
# Dziwne zachowanie:
def my_function():
    #var +=1 #tak nie działa, bez tego OK.
    print("Znam tę zmienną?", var)
var = 1
my_function()
print(var)

#---------------------
def my_function():
    var =7  # wewnątrzprocedurowa zamienna var
    print("Znam tę zmienną?", var)
var = 5  # inna zmianna var
my_function()
print(var)
#-----------------------
# słowo kluczowe global:
def my_function():
    global var
    var = 3
    print("Znam tę zmienną?", var)
var = 1
my_function()
print(var)
#-------------------------
# Przekazanie parametrów:
def my_function(n):
    print("Dostałem", n)
    n += 1
    print("Teraz mam", n)
var = 1
my_function(var)
print("Wartość w procedurze nadrzędnej", var)

#---------------------------------
#Przykład: Silnia metoda iteracyjna:
def silnia(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product

for n in range(1, 25):  # testing
    print(n, silnia(n))
#------------------------------------
#Przykład: Fibonacci metoda iteracyjna:
#fib_1 = 1
#fib_2 = 1
#fib_3 = 1 + 1 = 2
#fib_4 = 1 + 2 = 3
#fib_5 = 2 + 3 = 5

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


for n in range(1, 10):  # testing
    print(n, "->", fib(n))
#---------------------------------
# Rekurencja (ważne: warunkek zakończnia)

#Przykład: Silnia rekurencyjnie:
def silnia(n):
    if n < 0:  
        return None
    if n < 2:
        return 1 
    return n * silnia(n - 1)
for n in range(1, 10):  # testing
    print(n, silnia(n))

#---------------------------------
#Przykład: Fibonacci rekurencyjnie:
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

for n in range(1, 10):  # testing
    print(n, "->", fib(n))
#---------------------------------
#Ćwiczenie 4: Jaki będzie wynik:
#1:
def factorial(n):
    return n * factorial(n - 1)
print(factorial(4))

#Ćwiczenie 5: 
def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)
print(fun(25))
#---------------------------------------------------------------------------


'''
