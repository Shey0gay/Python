try: 
    import tkinter as tk
    from tkinter import Menu
    from tkinter import messagebox as mb
    from tkinter import ttk
    from tkinter.filedialog import askopenfilename, asksaveasfilename
    from tkinter.messagebox import showinfo
except: 
    print('Jeden importow nie powiodl sie.')

nameF = ''  #nazwa pliku

win = tk.Tk()
win.title("Edyta: " + nameF)
win.geometry("750x500")

tekst=''
txt1 = tk.Text(win, height=30, width=350, wrap=tk.NONE)
scb1 = tk.Scrollbar(win)
scb1.pack(side=tk.RIGHT, fill=tk.Y)
scb1.config(command=txt1.yview)

scb2 = tk.Scrollbar(win, orient="horizontal")
scb2.pack(side=tk.BOTTOM, fill=tk.X)
scb2.config(command=txt1.xview)
txt1.config(xscrollcommand=scb2.set, yscrollcommand=scb1.set)

#font = ("Comic Sans MS", 20, "bold")
font=('Tempus Sans ITC', 12, 'bold')
txt1.configure(font = font)
#txt1.tag_configure('bldItal', font=('Arial', 12, 'bold', 'italic'))    #to lub to poniżej
#txt1.tag_configure('kolor', foreground='#476042', font=('Tempus Sans ITC', 12, 'bold'))
#txt1.insert(tk.END, tekst, 'kolor')   # kolor lub blItal
txt1.pack()

mainMenu=Menu(win)  
win.config(menu=mainMenu)

#Functions:
def wyjście():
    if mb.askokcancel(title='Pytanko:',
                message='Czy na pewno chcesz zakończyć działanie programu?'):
        win.quit()
        win.destroy()

def mn_atrapa():
    mn_label=tk.Label(win, text="Atrapa").pack()

def plikNowy():
    hide_all_frames()
    if mb.askokcancel(title='Pytanko:',
                message='Czy na pewno chcesz rozpocząć edycję nowego pliku?'):
        tekst = ''
        txt1.delete(1.0,tk.END)
        txt1.insert(tk.END, tekst, 'kolor')
        nameF = ''
        win.title("Edyta: " + nameF)
        
def plikOtwórz():
    global nameF
    tekst = ''
    nameF = askopenfilename()
    if nameF!='':
        infile = open(nameF, 'rt', encoding='utf-8')
        for linia in infile:
            tekst+=linia
            if len(linia) > 65535:
                print('Plik zbyt duży, wczytano pierwsze 65535 bajtów')
                break
        infile.close()
        txt1.delete(1.0,tk.END)
        txt1.insert(1.0, tekst, 'kolor')
        win.title("Edyta: " + nameF)

def plikZapisz():
    global nameF
    if nameF == '':
        nameF = asksaveasfilename()   
    #nameF='C:\\MN\\__LEKCJE_2024-2025\\__PYTHON\\tkInter\\ala.txt'
    if nameF!='':
        hide_all_frames()
        #file_new_frame.pack(fill="both", expand=1)
        with open(nameF, 'wt', encoding='utf-8') as outFile:
            outFile.write(txt1.get("1.0","end-1c"))

def plikZapiszJako():
    global nameF
    nameF = asksaveasfilename()
    if nameF!='':
        with open(nameF, 'wt', encoding='utf-8') as outFile:
            outFile.write(txt1.get("1.0","end-1c"))
    win.title("Edyta: " + nameF)
        
#Hidel all frames:
def hide_all_frames():
    file_new_frame.pack_forget()
    #edit_cut_frame.pack_forget()

def kopiuj():
    showinfo(title='Kopiuj', message='Wybrałeś opcję Edytuj/Kopiuj')

def wytnij():
    showinfo(title='Wytnij', message='Wybrałeś opcję Edytuj/Wytnij')    


#Create a File menu
fileMenu=Menu(mainMenu)
mainMenu.add_cascade(label="Plik", menu=fileMenu)
fileMenu.add_command(label="Nowy",   command=plikNowy)  #
fileMenu.add_command(label="Otwórz", command=plikOtwórz) 
fileMenu.add_command(label="Zapisz", command=plikZapisz) # 
fileMenu.add_command(label="Zapisz jako", command=plikZapiszJako) #
fileMenu.add_separator()
fileMenu.add_command(label="Wyjście", command=wyjście)

#Create an Edit menu
editMenu=Menu(mainMenu)
mainMenu.add_cascade(label="Edycja", menu=editMenu)
editMenu.add_command(label="Kopiuj", command=kopiuj) #
editMenu.add_command(label="Wytnij", command=wytnij) # 
editMenu.add_command(label="Wklej",  command=mn_atrapa) #

#Create an Opcje menu
optMenu=Menu(mainMenu)
mainMenu.add_cascade(label="Opcje", menu=optMenu)       
optMenu.add_command(label="Opcja1", command=mn_atrapa)  #
optMenu.add_command(label="Opcja2", command=mn_atrapa)  # 
optMenu.add_command(label="Opcja3", command=mn_atrapa)  #

# Create frames
file_new_frame=tk.Frame(win, width=400, height=400)



win.protocol('WM_DELETE_WINDOW', wyjście)  # reakcja na 'X'
win.mainloop()
