'''
"""
W podejściu proceduralnym można wyróżnić dwa całkowicie oddzielne światy: świat danych i świat kodu.
W podejściu obiektowym dane i kod są ujęte w tym samym świecie, podzielone na klasy.
Klasa m.in. to zestaw obiektów. 
Obiekt jest wcieleniem wymagań, cech i charakterystyk przypisanych do konkretnej klasy.
Hierarchia rośnie od góry do dołu, podobnie jak korzenie drzew
Najbardziej ogólna i najszersza klasa jest zawsze na szczycie (nadklasa), podczas gdy jej pochodne znajdują się poniżej (podklasy).
Każda podklasa jest bardziej wyspecjalizowana niż jej nadklasa. 
Każda nadklasa jest coraz bardziej ogólna (bardziej abstrakcyjna) niż każda z jej podklas (nie zawsze jednak klasa może mieć tylko jedną nadklasę).

Dziedziczenie:
	Każdy obiekt dziedziczy wszystkie cechy zdefiniowane w dowolnej z nadklas.
	Klasa obiektu może definiować nowe cechy, które będą dziedziczone przez każdą z jej podklas.

Każdy istniejący obiekt może być wyposażony w trzy grupy atrybutów:
    • obiekt ma nazwę, która jednoznacznie identyfikuje go w macierzystej przestrzeni nazw (chociaż mogą istnieć również anonimowe obiekty) 
    • obiekt ma zestaw indywidualnych właściwości, które czynią go oryginalnym, unikalnym lub wybitnym (chociaż możliwe jest, że niektóre obiekty nie będą mieć żadnych właściwości) 
    • obiekt ma zestaw umiejętności do wykonywania określonych czynności, zdolnych zmienić sam obiekt lub niektóre inne obiekty. 

Kolejki FIFO, LIFO
#---------------------------------------------
#1. Przykład stosu w podejsciu proceduralnym:
stack = []
#stack2= []

def push(stos, val):
    stos.append(val)

def pop(stos):
    val = stos[-1]
    del stos[-1]
    return val

push(stack, 3)
push(stack, 2)
push(stack, 1)

print(pop(stack))
print(pop(stack))
print(pop(stack))

#push(stack2, "A")
#push(stack2, "B")
#push(stack2, "C")

#print(pop(stack2))
#print(pop(stack2))
#print(pop(stack2))
#-------------------------------------------
Wady podejścia proceduralnego:
a. istotna zmienna (lista stosu) - każdy może ją modyfikować, niszcząc stos; 
   np. w wyniku niedbalstwa, gdy ktoś myli różne nazwy: stack[0] = 0,
b. może się również zdarzyć, że będzie potrzeba posiadania więcej niż jednego stosu - trzeba będzie
   utworzyć kolejną listę do przechowywania stosu i prawdopodobnie nowe push i pop, 
   oraz inne potrzebne funkcje. 

Zalety podejśca obiektowego:
a. możliwość ukrycia (ochrony) wybranych wartości przed nieautoryzowanym dostępem (enkapsulacją); 
   do enkapsulowanych wartości nie można uzyskać dostępu ani ich modyfikować,
b. jeśli istnieje klasa, która implementuje wszystkie potrzebne zachowania stosu, można wytworzyć 
   dowolną liczbę stosów, bez konieczności kopiowania ani replikowania żadnej części kodu,
c. możliwość wzbogacenia stosu o nowe funkcje (dziedziczenie). Można utworzyć nową klasę (podklasę), 
   która dziedziczy wszystkie istniejące cechy z nadklasy i dodaje nowe cechy. 

#-------------------------------------------
#2. Przykład stosu napisanego obiektowo
#--------> nie komentować
class Stack:
    def __init__(self):          #tworzymy konstruktor
        self.__stackList = []    #magazyn stosu - tworzymy listę wewnątrz każdego obiektu klasy i ją ukrywamy (self)
        self.abc = 123

    def __del__(self):  	 # Deleting (Calling destructor)
        print('Destructor called.')

    def push(self, val):         #uwaga: parametr self (o tem potem)
        self.__stackList.append(val)

    def pop(self):
        try:
            val = self.__stackList[-1]
            del self.__stackList[-1]
        except IndexError:
             return None
        return val

    def show_me_my_stack(self):
        return self.__stackList

    def stack_len(self):
        return len(self.__stackList)
# <--------------nie komentować
#------------------------------------------------
KONSTRUKTOR:
    • nazwa konstruktora to zawsze __init__
    • jest wywoływany automatycznie i domyślnie, gdy tworzony jest nowy obiekt 
    • musi on mieć co najmniej jeden parametr (self), który służy do reprezentacji nowo utworzonego obiektu
      można go użyć do manipulowania obiektem i do wzbogacenia go o potrzebne właściwości, 
    • parametr obowiązkowy jest zwykle nazywany self (to tylko konwencja, ale należy jej przestrzegać
      upraszcza to proces czytania i rozumienia kodu) 
    • może (ale nie musi) mieć więcej parametrów niż tylko self;
      jeśli ma więcej parametrów, sposób, w jaki nazwa klasy jest używana do utworzenia obiektu, 
      musi odzwierciedlać definicję __init__; 
    • może służyć do stworzenia obiektu, tzn. poprawnie zainicjować jego stan wewnętrzny, 
      utworzyć zmienne instancji, utworzyć instancję dowolnych innych obiektów, 
      jeśli ich istnienie jest wymagane, itp. 
    • nie może zwrócić wartości, ponieważ jest przeznaczony do zwrócenia nowo utworzonego obiektu 
      i niczego więcej; 
    • nie może zostać wywołany bezpośrednio z obiektu lub z wewnątrz klasy (ale można wywołać konstruktor 
      z dowolnej nadklasy obiektu). 

self:
a. Wszystkie metody muszą mieć parametr self. 
b. Pozwala on na dostęp do elementów (właściwości i działań/metod) realizowanych przez rzeczywisty obiekt. 
c. Nie można go pominąć. 
d. Za każdym razem, gdy język Python wywołuje metodę, domyślnie wysyła bieżący obiekt jako pierwszy argument.
   Oznacza to, że metoda ma obowiązek posiadania co najmniej jednego parametru, który jest używany przez sam 
   język Python -nie mamy na to żadnego wpływu.
e. Nawet jeśli metoda nie wymaga żadnych parametrów, to self ten należy określić. 
   Jeśli jest przeznaczona do przetwarzania tylko jednego parametru, musisz określić dwa, a rola pierwszego 
   z nich jest wciąż taka sama.

#2a jeden stos ----------------------------------
s1 = Stack()

for i in range(5):
    s1.push(i)

print(s1.show_me_my_stack())

for i in range(len(s1.show_me_my_stack())):  #brak parametru self 
    print(s1.pop())

#2b 2 stosy--------------------------------------

s1 = Stack()
s2 = Stack()

for i in range(5):
    s1.push(i)

for i in range(5):
    s2.push(chr(ord('A') + i))

print(s1.show_me_my_stack())
print(s2.show_me_my_stack())

for i in range(len(s1.show_me_my_stack())): 
    print(s1.pop())

#for i in range(len(s2.show_me_my_stack())):
#    print(s2.pop())

print(s1.show_me_my_stack())
#print(s2.show_me_my_stack())

#-------------------------------------------
# Użycie konstruktora i destruktora:

class Employee:
 
    # Initializing
    def __init__(self):
        print('Obiekt utworzony')
 
    # Calling destructor
    def __del__(self):
        print("Obiekt zniszczony")
 
print('Tworzenie obiektu...')
obj = Employee()
print('Koniec programu...')
del obj 

#-------------------------------------------
#Ukrywanie właściwości przed światem:
#A. lista widoczna

class Stack: 
    def __init__(self): 
        self.stackList = [1,2,3] #lista widoczna

    def show_stack(self):
        return self.stackList
    
stackObject = Stack()
#print(stackObject.stackList) 
print(stackObject.show_stack())  # lista widoczna

#------------------------------------------
#B. lista niewidoczna
#Gdy jakikolwiek komponent klasy ma nazwę zaczynającą się od dwóch podkreśleń (__), staje się on prywatny, 
#tj. można uzyskać do niego dostęp tylko z poziomu klasy. Nie można go zobaczyć z zewnątrz (koncepcja enkapsulacji)

class Stack: 
    def __init__(self): 
        self.__stackList = [] #lista niewidoczna

    def show_stack(self):
        return self.__stackList

    def push(self, val):         #uwaga: parametr self (o tem potem)
        self.__stackList.append(val)

    def pop(self):
        try:
            val = self.__stackList[-1]
            del self.__stackList[-1]
        except IndexError:
             return None
        return val
    
    def stack_len(self):
        return len(self.__stackList)
    
stackObject = Stack()
#print(stackObject.__stackList) 
print(stackObject.show_stack())   #lista niewidoczna zgłoszony zostaje wyjątek
print(stackObject._Stack__stackList)       #sposób na dostanie się do zaenkapsulowanych atrybutów

#------------------------------------------
# jak dostać się do zaenkapsulowanych atrybutów klasy: używamy ._<nazwa_klasy><nazwa_atrybutu>, np. print(s1._Stack__stackList)

Sposób wywoływania metod ze zmiennej __stackList.
    • pierwszy etap dostarcza obiektu jako całości → self; 
    • następnie, należy dostać się do listy __stackList (self.__stackList), 
    • Gdy __stackList jest gotowa do użycia, można wykonać ostatni krok → self.__stackList.append(val). 

#------------------------------------------
#Podklasa:
#Definiujemy nową podklasę wskazującą na klasę:

class AddingStack(Stack): 
    pass 

Klasa nie definiuje jeszcze żadnego nowego komponentu, ale to nie znaczy, że jest pusta. 
Otrzymuje wszystkie komponenty zdefiniowane przez swoją nadklasę - nazwa nadklasy jest zapisywana po dwukropku bezpośrednio po nazwie nowej klasy.

Teraz od nowego stosu chcemy:
    • aby metoda push nie tylko dodała wartość do stosu, ale także by dodała wartość do zmiennej sum; 
    • aby funkcja pop nie tylko odjęła wartość ze stosu, ale także by odjęła wartość ze zmiennej sum. 

Składnia:
    • określamy nazwę nadklasy (jest to klasa, której konstruktor chcesz uruchomić) 
    • wstawiamyz po niej kropkę (.); 
    • określamy nazwę konstruktora; 
    • wskazujemy obiekt (instancję klasy), który musi zostać zainicjalizowany przez konstruktor -
      dlatego musimy podać argument i użyć tutaj zmiennej self; 
      Uwaga: wywoływanie dowolnej metody (w tym konstruktorów) spoza klasy nigdy nie wymaga umieszczania 
      argumentu self na liście argumentów - wywoływanie metody z klasy wymaga jawnego użycia argumentu self 
      i musi być on umieszczony jako pierwszy na liście. 
      Uwaga: na ogół zaleca się wywoływanie konstruktora nadklasy przed innymi inicjalizacjami, 
             które chcemy wykonać wewnątrz podklasy.

#-------------------------------------------------

class AddingStack(Stack): 
    def __init__(self): 
        Stack.__init__(self)  #jawne wywoływanie konstruktora nadklasy  
        self.__sum = 0        #zmienna przechowyje sumy wartości stosu
    
    def push(self, val):  #metoda push została nadpisana
        self.__sum +=val
        Stack.push(self, val)  

    def pop(self):        #metoda pop została nadpisana
        if (self.stack_len() > 0):
           val = Stack.pop(self) 
           self.__sum -= val
           return val     
    
    def show_sum(self):
        return self.__sum
    
st = AddingStack()
print(st.__dict__)
print(st.show_sum(), st.show_stack())
st.push(7)
print(st.show_sum(), st.show_stack())
st.push(8)
print(st.show_sum(), st.show_stack())
st.push(9)
print(st.show_sum(), st.show_stack())
st.pop()
print(st.show_sum(), st.show_stack())
st.pop()
print(st.show_sum(), st.show_stack())
st.pop()
print(st.show_sum(), st.show_stack())

# ZMIENNE INSTANCJI:-----------------------------------
Klasa może być wyposażona w dwie grupy danych tworzące właściwości danej klasy. 
Pierwszy rodzaj istnieje tylko wtedy, kiedy jest jawnie stworzona i dodana do obiektu. 
Można to uczynić podczas inicjalizacji obiektu wykonywanej przez konstruktor.
Można tego dokonać w dowolnym momencie życia obiektu. 
Istniejąca właściwość może też zostać usunięta w dowolnym momencie.

Takie podejście pociąga za sobą istotne konsekwencje:
    • różne obiekty tej samej klasy mogą posiadać różne zestawy właściwości; 
    • musi istnieć sposób, by bezpiecznie sprawdzić, czy określony obiekt posiada daną właściwość, 
      którą chcemy się posłużyć (chyba, że chcesz wymusić wyjątek - zawsze warto rozważyć taki przypadek) 
    • każdy obiekt niesie ze sobą własny zestaw właściwości - nie zakłócają one siebie nawzajem. 

Takie zmienne (właściwości) nazywane są zmiennymi instancji.
Słowo instancja sugeruje, że są one blisko powiązane z obiektami (które są instancjami klasy), a nie z samymi klasami.
#-----------------------------------

class Klasa:

    def __init__(self, wartość = 1):
        self.ala = wartość
        self.__ala = wartość + 0.5

    def ustawEla(self, wartość):
        self.ela = wartość
        self.__ela = wartość + 0.5

Obiekt1 = Klasa()
Obiekt2 = Klasa()
Obiekt2.ustawEla(3)

Obiekt3 = Klasa(4)
Obiekt3.ola = 5
Obiekt3.__ola = 5.5
Obiekt3.__ula = 6

print(Obiekt1.__dict__)   #Obiekt1 ma właściwości o nazwie ala i _ala;
print(Obiekt2.__dict__)   #Obiekt2 ma właściwości: ala, __ala , ela i __ela; 
print(Obiekt3.__dict__)   #Obiekt3 został wzbogacony o właściwość spoza kodeu klasy - to możliwe i w pełni dozwolone.
print(Obiekt3.__ula)
print(Obiekt3._Klasa__ula) # tu zniekształcanie nie zadziała - pełny dostęp do zmiennej

#--Wynik:-------------------------
{'ala': 1, '_Klasa__ala': 1.5}
{'ala': 1, '_Klasa__ala': 1.5, 'ela': 3, '_Klasa__ela': 3.5}
{'ala': 4, '_Klasa__ala': 4.5, 'ola': 5, '__ola': 5.5, '__ula': 6}
6
Błąd
#---------------------------------
#UWAGA:
Obiekty języka Python, podczas tworzenia, otrzymują mały zestaw predefiniowanych właściwości i metod. 
Jedna z nich to zmienna o nazwie __dict__ (słownik). Zmienna ta zawiera nazwy i wartości wszystkich właściwości, które obecnie posiada obiekt. 

Czyli:	* zmienne instancji są od siebie zupełnie odizolowane.
	* modyfikowanie zmiennej instancji dowolnego obiektu nie ma wpływu na pozostałe obiekty. 	

Przykład jak wyżej + "__" przed nazwami zmiennych:
Python zniekształca operację w następujący sposób:
    • umiejscawia nazwę klasy przed nazwą, którą nadajesz; 
    • dodaje dodatkowy podkreślnik na początku. 
    • Zniekształcanie nie zadziała jeśli dodasz zmienną instancji spoza kodu klasy.

WAŻNE:
Zmienne KLASY (jak pole statyczne):
a. Zmienna klasy jest właściwością, która istnieje tylko w jednym egzemplarzu i jest przechowywana 
   poza którymkolwiek z obiektów.
b. żadna zmienna instancji nie istnieje jeśli klasa nie posiada obiektu; 
   zmienna klasy istnieje w jednym egzemplarzu nawet jeśli sama klasa nie posiada żadnych obiektów.
c. zmienne klasy nie są ukazane w obiekcie __dict__ , bo nie są częścią składową obiektu

class Klasa:
    licznik = 0
    def __init__(self, wartość = 1):
        self.__wart = wartość

Klasa.licznik = 11  #zmienna klasy
Obiekt1 = Klasa()
Klasa.licznik = 12
Obiekt2 = Klasa(2)
Obiekt3 = Klasa(4)
Klasa.licznik = 13

print(Obiekt1.__dict__, Obiekt1.licznik) #zmienne klasy nie są ukazane w obiekcie __dict__
print(Obiekt2.__dict__, Obiekt2.licznik)
print(Obiekt3.__dict__, Obiekt3.licznik)
ObiektA = Klasa()        
ObiektA.licznik = 14     #zmienna instancji
ObiektB = Klasa()
ObiektB.licznik = 15     
ObiektC = Klasa()  
ObiektC.licznik = 16
print(ObiektA.__dict__, ObiektA.licznik)
print(ObiektB.__dict__, ObiektB.licznik)
print(ObiektC.__dict__, ObiektC.licznik)
print(Obiekt1.__dict__, Obiekt1.licznik)
print(Obiekt2.__dict__, Obiekt2.licznik)
print(Obiekt3.__dict__, Obiekt3.licznik)

#-----------------------------------------------
#Sprawdzanie, czy dany atrybut istnieje:

class Klasa:
    def __init__(self, wartosc):
        if wartosc % 2 != 0:
            self.a = 1    #istnieje albo atrybut a albo atrybut b
        else:
            self.b = 2

Obiekt = Klasa()
print(Obiekt.a)  #AttributeError: 'KlasaPrzykl' object has no attribute 'a'
print(Obiekt.b)

#-----------------------------------------
#Można użyć bloku try-catch:

Obiekt1 = Klasa(2)
Obiekt2 = Klasa(3)

try:
    print("1a.", Obiekt1.a)
    print("1b.", Obiekt1.b)
except AttributeError:
    print('Błąd atrybutu')

try:
    print("2a.", Obiekt2.a)
    print("2b.", Obiekt2.b)
except AttributeError:
    print('Błąd atrybutu')

#------------------------------------------
#Lub funkcji hasattr:

if hasattr(Obiekt1, 'a'):
    print('1a.',Obiekt1.a)
if hasattr(Obiekt1, 'b'):
    print('1b.',Obiekt1.b)

if hasattr(Obiekt2, 'a'):
    print('2a.',Obiekt2.a)
if hasattr(Obiekt2, 'b'):
    print('2b.',Obiekt2.b)

#------------------------------------------
Metody w szczegółach:
* metoda jest funkcją osadzoną w klasie,
* metoda musi mieć przynajmniej jeden parametr (nie ma czegoś takiego jak metody bez parametrów 
  - metoda może być wywołana bez argumentu, ale nie może być zadeklarowana bez parametrów)
* pierwszy (lub jedyny) parametr zazwyczaj nosi nazwę self (self sugeruje cel parametru 
  - identyfikuje obiekt, dla którego wywołana jest metoda.),
* jeśli chcemy wywołać metodę, nie możemy przekazać argumentu dla parametru self - zrobi to Python
* parametr self jest używany w celu uzyskania dostępu do instancji obiektu i zmiennych klasy.

Aby metoda akceptowała parametry inne niż self, trzeba:
    • umieścić je po self w definicji metody; 
    • podać je podczas wywoływania bez określania self (jak poprzednio) 
#------------------------------------------
class Classy: 
    def metoda1(self): 
        print("metoda1")

    def metoda2(self, par): 
        print("metoda2", par) 
        self.metoda1() 

obj = Classy() 
obj.metoda2(1) 
obj.metoda2(2) 
obj.metoda2(3)
obj.metoda1()
#------------------------------------------
KONSTRUKTOR (cd):

class Classy: 
    def __init__(self, wartosc = None): #dodatkowy parametr wartosc
        self.zmienna = wartosc 

obj1 = Classy("obiekt") 
obj2 = Classy() 
print(obj1.zmienna) 
print(obj2.zmienna)
#--------------------

#ukrywanie metod:
class Classy: 
    def widoczny(self): 
        print("widoczny") 

    def __ukryty(self): 
        print("ukryty") 

obj = Classy() 
obj.widoczny() 

try: 
    obj.__ukryty() 
except: 
    print("niepowodzenie") 

obj._Classy__ukryty()

#-------------------------------
WEWNĘTRZNE ŻYCIE KLAS I OBIEKTÓW:
Każda klasa języka Python i każdy obiekt języka Pythona jest wstępnie wyposażony w zestaw przydatnych 
atrybutów, które można wykorzystać do zbadania jego możliwości.

__dict__  - słownik. 
__name__, - łańcuch znaków - zawiera nazwę klasy (atrybut __name__ jest nieobecny w obiekcie - istnieje 
            tylko wewnątrz klas),
type()    - jest w stanie znaleźć klasę, która została użyta do utworzenia instancji dowolnego obiektu,
__module__ - łańcuch znaków-przechowuje nazwę modułu, który zawiera definicję klasy
__bases__  - krotka-zawiera klasy (nie nazwy klas), które są bezpośrednimi nadklasami dla klasy.

#--------------------

#Przykład:
class NadKlasa:
    print("tu jest Nadklasa do Klasa")  

class Klasa(NadKlasa):
    print("tu jest Klasa")
    def widoczna(self): 
        print("Metoda widoczna") 

    def __ukryta(self): 
        print("Metoda ukryta") 

obj = Klasa() 
obj.widoczna()  # widoczny

try: 
    obj.__ukryta() 
except: 
    print("NIEPOWODZENIE")  

obj._Klasa__ukryta()         
print("A", Klasa.__name__)   
obj = Klasa()                         
print("B", type(obj).__name__) 

print('1', Klasa.__module__) 
obj = Klasa() 
print('2', obj.__module__)
#print('3', obj.__bases__) #błąd
print('4', Klasa.__bases__)

#--------------------------------
#Przykład: __bases__   (i dziedziczenie wielokrotne):

class SuperJeden: 
    pass 

class SuperDwa(SuperJeden): 
    pass 

class SuperTrzy(): 
    pass

class Sub1(SuperDwa): 
    pass 

class Sub2(SuperJeden, SuperTrzy):
    pass

def printBases(cls): 
    for x in cls.__bases__: 
        print(cls.__name__,"-->",x.__name__, end=' ') 
    print()

printBases(SuperJeden) 
printBases(SuperDwa)
printBases(SuperTrzy) 
printBases(Sub1)
printBases(Sub2)
#lub tak:
print(Sub1.__name__, Sub1.__bases__)   

#-----------------------------
Kompozycja i diamenty

Powyższe środki pozwalają wykonać dwie ważne czynności:
    • introspekcja, czyli zdolność programu do sprawdzenia typu lub właściwości obiektu w środowisku wykonawczym; 
    • refleksja, która jest zdolnością programu do manipulowania wartościami, właściwościami i/lub funkcjami obiektu w środowisku wykonawczym. 
Czyli, nie musimy znać kompletnej definicji klasy/obiektu, aby manipulować obiektem, ponieważ obiekt i/lub jego klasa 
zawierają metadane umożliwiające rozpoznanie ich cech podczas wykonywania programu.
Zarówno refleksja, jak i introspekcja umożliwiają programiście zrobienie czegokolwiek z każdym obiektem, bez względu na to, skąd taki obiekt pochodzi.

-----------------------------------------------------------
>>DZIEDZICZENIE<<:

Dziedziczenie to praktyka (w programowaniu obiektowym) przekazywania atrybutów i metod z nadklasy (zdefiniowanej i istniejącej) 
do nowo utworzonej klasy, zwanej podklasą. Czyli budowanie nowej klasy, nie od zera, ale poprzez użycie już zdefiniowanego repertuaru cech. 
Nowa klasa dziedziczy (i to jest klucz) wszystkie istniejące elementy, ale w razie potrzeby może dodać nowe.
Dzięki temu możliwe jest budowanie bardziej wyspecjalizowanych (bardziej konkretnych) klas przy użyciu niektórych zestawów 
wstępnie zdefiniowanych ogólnych reguł i zachowań.
Najważniejszym czynnikiem w procesie jest relacja między nadklasą i wszystkimi jej podklasami 
(uwaga: jeśli B jest podklasą A a C jest podklasą B oznacza to również, że C jest podklasą A).

#-------------------------
>>POLIMORFIZM:<<

Sytuacja, w której podklasa jest w stanie zmodyfikować zachowanie swej nadklasy (tak jak w przykładzie) nazywa się polimorfizmem. 
Innymi słowy, żadna klasa nie jest dana raz na zawsze. Zachowanie każdej klasy może być w dowolnym momencie modyfikowane przez każdą z jej podklas.

#-------------------------

>>KOMPOZYCJA:<<
  Kompozycja przedstawia klasę jako kontener zdolny przechowywać i wykorzystywać inne obiekty (pochodzące z innych klas),
  z których każdy implementuje część pożądanego zachowania klasy.

#-------------------------
#1. issubclass()
#   isinstance()

class Pojazdy:
    def ruch(self):
        print("Silnik działa")

class PojazdyLadowe(Pojazdy): 
    def ruch(self):
        print("Przekaż napęd")

class PojazdyGasiennicowe(PojazdyLadowe): 
    def ruch(self):
        print("Przesuwaj gąsiennice")

class PojazdyKolowe(PojazdyLadowe): 
    def ruch(self):
        print("Obracaj koła")

class PojazdyWodne(Pojazdy): 
    def ruch(self):
        print("Obracaj śrubę")


print('A. ',issubclass(PojazdyKolowe, Pojazdy))
print('B. ',issubclass(PojazdyGasiennicowe, PojazdyKolowe))
print('C. ',issubclass(PojazdyLadowe, Pojazdy))
print('D. ',issubclass(Pojazdy, Pojazdy))   # ciekawostka - klasa jest podklasą samej siebie
print('E. ',issubclass(PojazdyWodne, Pojazdy))

samochod=PojazdyKolowe()
czolg=PojazdyGasiennicowe()
taczki=PojazdyLadowe()
samochod.ruch()
czolg.ruch()
taczki.ruch()
motorowka=PojazdyWodne()
motorowka.ruch()

print('E. ',isinstance(czolg, Pojazdy))
print('F. ',isinstance(taczki, PojazdyKolowe))
print('G. ',isinstance(samochod, PojazdyGasiennicowe))
print('H. ',isinstance(samochod, PojazdyLadowe))
2025-03-06

'''


