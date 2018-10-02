from tkinter import *
from tkinter import ttk

history = []
hist_index=0

def update_history(string):
    global history, hist_index
    history=history[0:hist_index+1]
    history.append(string)
    hist_index=len(history)-1

def replace_text(text_box, text):
    text_box.delete('1.0',END)
    text_box.insert('1.0', text)

def reverse_text():
    update_history(text1.get('1.0',END))
    new_string=text1.get('1.0',END).strip()
    replace_text(text1, new_string[::-1])

def pig_latin():
    update_history(text1.get('1.0',END))
    new_string=text1.get('1.0',END).strip().split(' ')
    vowels='a e i o u'.split(' ')
    pig_string=''
    
    for word in new_string:
        try:
            if word[1].lower() == 'h' and word[0].lower() not in vowels:
                first_letter=word[:2]
                word=word[2:]+first_letter
                
            else:
                first_letter=word[0]
                if first_letter.lower() not in vowels:
                    word=word[1:]+word[0]
        except IndexError:
            word=word
            
        word+=('ay')
        pig_string+=(word+' ')
        
    replace_text(text1, pig_string)

def to_lower():
    update_history(text1.get('1.0',END))
    replace_text(text1, text1.get('1.0',END).lower())

def undo():
    global history, hist_index

    if hist_index==len(history)-1 and\
    history[hist_index]!=history[hist_index-1]:
        update_history(text1.get('1.0',END))

    if hist_index>0:
        hist_index-=1    
    replace_text(text1, history[hist_index])

def redo():
    global history, hist_index
    if hist_index<len(history)-1:
        hist_index+=1
    replace_text(text1, history[hist_index])
    
root = Tk()
root.title("Text Modification")



button_frame = Frame(root)
button1 = ttk.Button(button_frame, text='Reverse', command=reverse_text)
button2 = ttk.Button(button_frame, text='Pig Latin', command=pig_latin)
button3 = ttk.Button(button_frame, text='Lowercase', command=to_lower)
button4 = ttk.Button(button_frame, text='Undo', command=undo)
button5 = ttk.Button(button_frame, text='Redo', command=redo)

text1 = Text(root, height=10, width=80)

button_frame.grid(row=0, column=0)
text1.grid(row=1, column=0)
button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)
button4.grid(row=0, column=3)
button5.grid(row=0, column=4)

root.mainloop()







