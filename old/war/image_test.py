from tkinter import *
from tkinter import ttk

root=Tk()

card = PhotoImage(file = r'C:\Users\Mitchell\Documents\scripts\python\war\card_art\3_diamonds.gif').subsample(5, 5)

label1 = ttk.Label(root, image=card)

label1.pack()

root.mainloop()

