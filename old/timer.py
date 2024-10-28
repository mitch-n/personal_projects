from tkinter import *
from tkinter import ttk
from time import time
from time import sleep

count = 0

def replace_text(text_box, text):
    text_box.delete('1.0',END)
    text_box.insert('1.0', text)

def get_time():
    global count
    try:
        count=int(text.get('1.0',END).strip())
        info.destroy()
    except Exception:
        replace_text(text, '')

info = Tk()
info.state('zoomed')
info.bind('<Escape>', lambda e: info.destroy())
frame=Frame(info)

text=Text(frame, height=1, width=8,font='helvetica 30')

start_button=Button(frame, text='Start',font='helvetica 30', command=get_time)
info.bind('<Return>', lambda f: get_time())

frame.pack(expand=True)
text.grid(row=0,column=0, padx=(25,25))
start_button.grid(row=0,column=1)

text.focus_set()

info.mainloop()

print(count)

root = Tk()
root.state('zoomed')
root.bind('<Escape>', lambda e: root.destroy())

start = time()

check = 0
elapsed=0
label = Label(root,width=3, text=count, font='helvetica 530')
label.pack()

while count+elapsed >= 0:
    label.update()
    elapsed=int(start-time())
    if elapsed != check:
        label.config(text=count+elapsed)
        #print(count+elapsed)
        check=elapsed

sleep(2)
root.destroy()

root.mainloop()
