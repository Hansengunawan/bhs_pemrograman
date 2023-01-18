import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo
import os

root = Tk()
root.title = ("app")
root.geometry = ('400x580')


def hati_kosong():
    showinfo(title='INFO', message='Terisi')
    if showinfo == True:
        hati_penuh()
    else:
        return hatikosong()
def hati_penuh():
    showinfo(title='info', message='sudah penuh')


#button hatikosong
hatikosong = PhotoImage(file="./gambar/hatikosong.png")
button_hatikosong = Button(root, image=hatikosong,borderwidth=0, cursor="hand2", command=hati_kosong)
button_hatikosong.place(x=2, y=3)

#button hatipenuh
hatipenuh= PhotoImage(file="./gambar/hatipenuh.png")
button_hatipenuh = Button(root, image=hatipenuh,borderwidth=0, cursor="hand2", command=hati_penuh)
button_hatipenuh.place(x=250, y=10)

#button out
keluar = PhotoImage(file="./gambar/out.png")
button_keluar = Button(root, image=keluar,borderwidth=0, cursor="hand2",command=root.destroy)
button_keluar.place(x=25, y=300)

root.mainloop()