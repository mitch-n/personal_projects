## War

from random import randint
from time import sleep
from tkinter import *
from tkinter import ttk
import os

player_one=[]
player_two=[]
pot=[]
cards=[]
rounds=0

root=Tk()

class Card():
    def __init__(self, value, suit, image):
        self.value=value
        self.suit=suit
        self.image=image
    def get_value(self):
        return self.value
    def get_suit(self):
        return self.suit
    def get_image(self):
        return self.image



def make_cards():
    global cards
    spades=[2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
    hearts=[2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
    diamonds=[2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
    clubs=[2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']

    suits=[spades, hearts, diamonds, clubs]

    for suit in range(len(suits)):
        print(suit)
        suit_name=''
        if suit == 0:
            suit_name='spades'
        elif suit == 1:
            suit_name='hearts'
        elif suit == 2:
            suit_name='diamonds'
        elif suit == 3:
            suit_name='clubs'

        for card in suits[suit]:
            value=''
            suit=''
            image=''
            try:
                value=int(card)
            except Exception:
                if card=='Jack':
                    value=11
                elif card=='Queen':
                    value=12
                elif card=='King':
                    value=13
                elif card=='Ace':
                    value=14
            suit=suit_name

            image_path= r'C:\Users\Mitchell\Documents\scripts\python\war\card_art'
            image_path+='\\'+str(card)+"_"+str(suit_name)+".gif"
            image=PhotoImage(file = image_path).subsample(5, 5)
            cards.append(Card(value, suit, image))

score1=ttk.Label(root, text = '26', font='helvetica 120')
score2=ttk.Label(root, text = '26', font='helvetica 120')
label1=ttk.Label(root)
label2=ttk.Label(root)
#debug=ttk.Label(root, justify = LEFT, wraplength='2500')
score1.grid(row=0, column=0)
label1.grid(row=0, column=1)
label2.grid(row=0, column=2)
score2.grid(row=0, column=3)
#debug.grid(row=1, columnspan=4)
make_cards()
 
def shuffle():
    global player_one, player_two, cards
    player_one=[]
    player_two=[]

    i=True
    while len(cards)>0:
        card=cards[randint(0,len(cards)-1)]
        if i==True:
            player_one.append(card)
            cards.remove(card)
        if i==False:
            player_two.append(card)
            cards.remove(card)

        i = not i

def draw_decks():
    global player_one, player_two, pot
    numCards=len(player_one)+len(player_two)
    score1.config(text=str(len(player_one)))
    score2.config(text=str(len(player_two)))
    if len(player_one) and len(player_two)>0:
        label1.config(image=player_one[0].get_image())
        label2.config(image=player_two[0].get_image())
    label1.update()
    label2.update()
    score1.update()
    score2.update()
    sleep(.5)

def game():
    global player_one, player_two, rounds

    shuffle()
    rounds=0
    while len(player_one)>0 and len(player_two)>0:
        rounds+=1

        draw_decks()

        card_one=player_one.pop(0)
        card_two=player_two.pop(0)

        if card_one.get_value() > card_two.get_value():
            player_one.append(card_two)
            player_one.append(card_one)
        elif card_two.get_value() > card_one.get_value():
            player_two.append(card_one)
            player_two.append(card_two)
        else:
            tieBreaker(card_one, card_two)
            
    draw_decks()
    game_over()

def tieBreaker(card_one, card_two):
    global player_one, player_two, pot
##    print("tie breaker:", card_one, card_two)
##    input()
    if len(player_one)>3 and len(player_two)>3:
        tempPot=[player_one.pop(0),player_one.pop(0),player_one.pop(0),
             player_two.pop(0),player_two.pop(0),player_two.pop(0),
             card_one, card_two]
        for card in tempPot:
            pot.append(card)

        gamble_one=player_one.pop(0)
        gamble_two=player_two.pop(0)

##        print("gambles:", gamble_one, gamble_two)
##        print("Pot: "+str(pot))
##        input()

        if gamble_one.get_value() > gamble_two.get_value():
##            print("One is greater")
##            input()
            pot.append(gamble_one)
            pot.append(gamble_two)
            for card in pot:
                player_one.append(card)
            pot=[]

        elif gamble_two.get_value() > gamble_one.get_value():
##            print("Two is greater")
##            input()
            pot.append(gamble_one)
            pot.append(gamble_two)
            for card in pot:
                player_two.append(card)
            pot=[]
        else:
##            print("It's a tie.")
##            input()
            tieBreaker(gamble_one, gamble_two)

    else:
        pot.append(card_one)
        pot.append(card_two)
        if len(player_one)<=3:
            for card in pot:
                player_two.append(card)
            pot=[]
            for i in range(len(player_one)):
                player_two.append(player_one.pop())
                
        elif len(player_two)<=3:
            
            for card in pot:
                player_one.append(card)
            pot=[]
            for i in range(len(player_two)):
                player_one.append(player_two.pop())

def game_over():
    global player_one, player_two, rounds
    if len(player_one)>0:
        print("Player One Wins!")
    else:
        print("Player Two Wins!")

    print("Rounds: "+str(rounds))

game()

root.mainloop()
