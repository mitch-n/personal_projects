from random import randint
from time import sleep
import os

player_one=[]
player_two=[]
pot=[]
rounds=0

def shuffle():
    global player_one, player_two
    deck=[]
    player_one=[]
    player_two=[]

    spades=[2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
    hearts=[2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
    diamonds=[2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
    clubs=[2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']

    suits=[spades, hearts, diamonds, clubs]

    while len(spades)>0 or len(hearts)>0 or len(diamonds)>0 or len(clubs)>0:

        suit = suits[randint(0,len(suits)-1)]
        if suit==spades:
            suitname=" of Spades"
        if suit==hearts:
            suitname=" of Hearts"
        if suit==diamonds:
            suitname=" of Diamonds"
        if suit==clubs:
            suitname=" of Clubs"

        if len(suit)>0:
            card=suit[randint(0, len(suit)-1)]
            deck.append(card)
            suit.remove(card)

    i=True
    while len(deck)>0:
        card=deck[randint(0,len(deck)-1)]
        if i==True:
            player_one.append(card)
            deck.remove(card)
        if i==False:
            player_two.append(card)
            deck.remove(card)

        i = not i

    face_cards=['Jack','Queen','King','Ace']

def draw_decks():
    global player_one, player_two, pot
    numCards=len(player_one)+len(player_two)
    running=('------------'+str(numCards)+'\n')
    for r in range(max(len(player_one), len(player_two))):
        if r<len(player_one):
            num1=str(player_one[r])
        else:
            num1=''

        if r<len(player_two):
            num2=str(player_two[r])
        else:
            num2=''

        running+=(num1+"\t"+num2)

        if num1==num2:
            running+=("\tD")

        running+=('\n')
    running+=('------------\n')
    os.system('cls')
    print(running)
    sleep(.2)

def game():
    global player_one, player_two, rounds

    shuffle()
    rounds=0
    while len(player_one)>0 and len(player_two)>0:
        rounds+=1

        draw_decks()

        card_one=player_one.pop(0)
        card_two=player_two.pop(0)

        if face2num(card_one) > face2num(card_two):
            player_one.append(card_two)
            player_one.append(card_one)
        elif face2num(card_two) > face2num(card_one):
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


        if face2num(gamble_one) > face2num(gamble_two):
##            print("One is greater")
##            input()
            pot.append(gamble_one)
            pot.append(gamble_two)
            for card in pot:
                player_one.append(card)
            pot=[]

        elif face2num(gamble_two) > face2num(gamble_one):
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

def face2num(card):
    if card=='Jack':
        return 11
    elif card=='Queen':
        return 12
    elif card=='King':
        return 13
    elif card=='Ace':
        return 14
    else:
        return card

def game_over():
    global player_one, player_two, rounds
    if len(player_one)>0:
        print("Player One Wins!")
    else:
        print("Player Two Wins!")

    print("Rounds: "+str(rounds))

game()









