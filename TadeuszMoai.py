import time
from os import strerror
try:
    licznik = 0
    s = open("C:\\Users\\p23kseln\\Desktop\\PanTadeusz.txt", "rt", encoding='utf-8')
    zawartosc = s.readline()
    while zawartosc != '':
        print(zawartosc,end='')
        zawartosc = s.readline()
    s.close()
except IOError as e:
    print("Blad I/O: ", strerror(e.errno))
