import tkinter as tk
from tkinter import PhotoImage
win = tk.Tk()
win.title("Twoja stara je beret")
win.geometry("500x500")
lab = tk.Label(win, text="twoja stara 🗿").pack()

##image = PhotoImage(file="Moai_Rano_raraku.jpg")

##image_label = tk.Label(win, image=image)
##image_label.pack()
##logo = tk.PhotoImage(file="Moai_Rano_raraku.jpg")
##lab1 = tk.Label(win, image=logo, text=napis,fg="blue", font="Verdana 12 bold, width=20")

button = tk.Button(win, text='A wiesz co? Twój stary 🗿🗿🗿', width=25, command=win.destroy)
button.pack()

win.mainloop()
