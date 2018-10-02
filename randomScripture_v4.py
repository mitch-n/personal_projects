import random, requests, bs4, re, os
from tkinter import *
from tkinter import ttk

#make book list
def get_books():
    global book_urls, chapter_urls, verses
    r = requests.get('https://www.lds.org/scriptures/bofm?lang=eng')
    soup = bs4.BeautifulSoup(r.content, features="html.parser")
    sections = soup.find_all('ul', {'class':'books'})
    for section in sections:
        all_books=section.find_all('a', {"class":"tocEntry"})
        for book in all_books:
            book_urls.append((book.attrs['href']))

# Make chapter list
def get_chapters():
    global book_urls, chapter_urls, verses
    for book_url in book_urls:
        if not re.search(r'/[0-9]\?', book_url):
            r = requests.get(book_url)
            soup = bs4.BeautifulSoup(r.content, features="html.parser")
            soup = soup.find('div', {'class':'chapters'})

            all_chapters=soup('a', {"class":"titleNumber"})
            all_chapters=soup.find_all('a', {"class":"titleNumber"})
        for chapter in all_chapters:
            chapter_urls.append((chapter.attrs['href']))

        else:
            chapter_urls.append(book_url)

    temp_chapter_urls=[]
    for url in chapter_urls:
        if re.search(r'/[0-9]+\?', url):
            temp_chapter_urls.append(url)

    chapter_urls=list(set(temp_chapter_urls[:]))

#chapter_urls=sorted(chapter_urls)

chapter_url=""

#choose verse
def get_verse():
    global book_urls, chapter_urls, verses, chapter_url
    chapter_url = chapter_urls[random.randint(0,len(chapter_urls)-1)]

    #print(chapter_url)

    r = requests.get(chapter_url)
    soup = bs4.BeautifulSoup(r.content, features="html.parser")
    article = soup.find('div', {'class':'article'})

    all_verses=article('p', {"class":"verse"})
    verse = all_verses[random.randint(0,len(all_verses)-1)]
    
    #print(verse)

    book=soup.find('span',{'class':'dominant'}).text
    chapter=soup.find('h2',{'id':'title_number1'}).text

    verse=bs4.BeautifulSoup(re.sub('>[a-z]<','',str(verse)), features="html.parser")
    # print()
    # print(book)
    # print(chapter)
    # print(verse.text)
    # print()
    book=book.lower().replace('the ','')
    book=book.lower().replace('book','')
    book=book.lower().replace('of','')
    book=re.sub('\s{2,}',' ', book)
    chapter = re.sub('\D','',chapter)
    title_text.config(text=book.title()+' '+chapter)
    verse_text.config(text=verse.text)

def visit_link():
    global chapter_url
    os.system("start firefox.exe "+chapter_url)
    #print(chapter_url)

root = Tk()
root.wm_title("Random Scripture")
footer = Label(root, text="Getting Books...", bd=1, relief=SUNKEN, anchor=W)
display_area=Frame(root)
button_area=Frame(display_area)
title_text = Label(display_area, text="  ", font='helvetica 25')
verse_text = Label(display_area, text="  ", font='helvetica 15', \
wraplength=500, width=50)
randomize=ttk.Button(button_area, text="New Verse", command=get_verse)
link = ttk.Button(button_area, text="Open Chapter", command=visit_link)

display_area.pack(side=TOP)
title_text.grid(row=0,padx=(25,25),pady=(10,5))
verse_text.grid(row=1,padx=(25,25),pady=(5,10))
button_area.grid(row=2)
randomize.grid(row=0,column=0)
link.grid(row=0,column=1)

footer.pack(side=BOTTOM, fill=X)

footer.update()

book_urls=[]
chapter_urls=[]
verses=[]

#Do it all
get_books()
footer.config(text='Getting Chapters...')
footer.update
get_chapters()
footer.config(text='Ready')
footer.update()
get_verse()

root.mainloop()

