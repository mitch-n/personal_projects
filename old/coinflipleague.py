from random import randint
from time import sleep
from sys import stdout
from sys import argv


players=[]

try:
	num_players = int(argv[1])
except:
	num_players = 32

for i in range(1,num_players+1):
	players.append(f"Player {i}")

class Match():
	def __init__(self, match_num, round_num):
		self.players=[]
		self.winner=""
		self.match_num=match_num
		self.round_num=round_num
		
		
	def add_player(self, player):
		if len(self.players)<=2:
			self.players.append(player)
	def add_winner(self, winner):
		if not self.winner:
			self.winner=self.players[winner]

match_history=[]
round_num=1
print("""
MNkc;,,,,,,,,,,,,,,,,,,,,,,,,,,',l0WMMW0kkkdlcccccccllccccclo0W
Mk'............................;oXMMMMMWkokOd;;ldc;;okd:,,,,,c0
Mx...........................'kNWMWXKKNWXdx0Ol,cxOxc;lkOo;,,,:O
Mx...........................xWMWWNNKOOKNxd0Kd;,,ck0o;;o0k:,,:O
Mx..........................oNWNXXWNXXKkKxd0Kk:,,,;d0d;,l0k:,:O
Mx.........................:KXKNNWWX0KK0XxoKKk:,,,,;xKo,,o0d,:O
Mx.........,'..'l:.........xWXXWWWNKKKOKXdxXXx;,,,,,:OO:,:OOc:O
Mx........'kx. ;0x........,0NKNMMWNX0OOXKokXKo,,,,,,,dKl,,xKo:O
Mx.........kO' .kO'.......cXWXNWWWMW0OXWkoOKOc,,,,,,,oOo,,lxc:O
Mx.........oKc..lKl.......oWMWWMMMMN00WKox00x;,,,,,,,;:;,,,,,:O
Mx.........'kO,..x0:......oNNNMMMMMXkOKxo0KOc,,,,,,,,,,,,,,,,:O
Mx..........,Ok,.'x0c.....cXXKKKKKK00KkoOX0o,,,,,,,,,,,,,,,,,:O
Mx...........,xOc..cOx;...,0MWNXXXXXXkokK0o;,,,,,,,,,,,,,,,,,:O
Mx.............ckkc.'okl...cXMMMMMWKddk0Ol;,,,,,,,,,,,,,,,,,,:O
MXl..............::.........;x0K0OkxxOkd:,,,,,,,,,,,,,,,,,,,:xX
MMNkoccccccccccccccccccccccccloddd0XK0xooooooooooooooooooood0NW""")
print(""" _____     _        _____ _ _        __                        
|     |___|_|___   |   __| |_|___   |  |   ___ ___ ___ _ _ ___ 
|   --| . | |   |  |   __| | | . |  |  |__| -_| .'| . | | | -_|
|_____|___|_|_|_|  |__|  |_|_|  _|  |_____|___|__,|_  |___|___|
                             |_|                  |___|        """)

while len(players)>1:
	print(f"Round {round_num}")
	print(f"{len(players)} Players")
	print()
	input("<Enter> to begin...")
	print()
	round_num +=1 

	matches = []
	match_num=1
	# Create Matches
	for i in range(0,len(players),2):
		match = Match(match_num, round_num)
		match_num += 1
		match.add_player(players[i])
		try:
			match.add_player(players[i+1])
		except IndexError:
			pass
			
		matches.append(match)

	# Play Matches
	extra_space = False
	players = []
	for match in matches:
		#sleep(.5)	
		if len(match.players)==2:
			# Flip a coin
			match.add_winner(randint(0,10000)%2)
		if len(match.players)==1:
			if randint(0,10000)%2:
				match.add_winner(0)
				
		print(match.match_num, end=": ")
		#print(match.players, end=" -> ")
		if len(match.players)==2:
			print(f"{match.players[0]} vs {match.players[1]} -> ", end="")
		else:
			print(f"{match.players[0]} Solo Flip -> ", end="")
		stdout.flush()
		#sleep(1)
		if match.winner:
			players.append(match.winner)

			print(match.winner)
		else: 
			print("Elimination")
		
		if extra_space:
			print()
		extra_space = not extra_space
		
		match_history.append(match)

	print("----------------------------------")

print()
print(f"The Winner Is {players[0]}!")
print()
