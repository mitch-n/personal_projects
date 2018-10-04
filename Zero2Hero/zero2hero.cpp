#include <iostream>
#include <string>
#include "zero2hero.h"

using namespace std;

int main(){
	
	greeting();
	
	//Hero's position
	int posx=0;
	int posy=0;
	
	//Hero's last position
	int curx;
	int cury;
	
	//Hitpoints and tile marker
	int hp=15;
	int turns=0;
	int tile;
	
	//Creating the map
	int map[10][20] = {{0}};
	create_map(map);
	draw(map, 0, 0, 0, 0,"The lights are about to go out.\nDon't worry, you have a flashlight.");
	
	
	//Start Game
	string direction;
	bool bad_input;
	bool alive=true;
	while(alive){
		//Choose a direction. Change HP
		cout<<"HP: "<<hp<<endl;
		cout<<"Turns: "<<turns<<endl;
		bad_input=true;
		while(bad_input){
			cout<<"choose n,s,e or w, then press <ENTER>: ";
			curx=posx;
			cury=posy;
			cin>>direction;
			if(direction=="n"){
				if(posy<=0){
					cout<<"There is a wall there"<<endl;
				}
				else {
					posy--;
					bad_input=false;
				}
			}
			else if(direction=="s"){
				if(posy>=9){
					cout<<"There is a wall there"<<endl;
				}
				else {
					posy++; 
					bad_input=false;
				}
			}
			else if(direction=="e"){
				if(posx>=19){
					cout<<"There is a wall there"<<endl;
				}
				else {
					posx++; 
					bad_input=false;
				}
			}
			else if(direction=="w"){
				if(posx<=0){
					cout<<"There is a wall there"<<endl;
				}
				else {
					posx--; 
					bad_input=false;
				}
			}
			else if(direction=="uuddlrlrab"){
				hp+=100;
				draw(map,curx,cury,posx,posy,"");
				cout<<"HP: "<<hp<<endl;
				cout<<"Turns: "<<turns<<endl;
			}
			
			else cout<<"bad input"<<endl;
		}
		
		tile=map[posy][posx];
		
		//If tile is even, add that much hp
		//If tile is odd, remove that much hp
		//If tile is empty, you die
		//If tile is 0, you win.
		if(tile==0) break;
		
		if(tile<10){
			if(tile%2==0) hp+=tile;
			else hp-=(tile*2);
		}
		else hp=0;
		
		if(hp<=0) break;
		
		
		flashlight(map,curx,cury,posx,posy);
		turns++;
				
		//cout<<"x,y = "<<posx<<","<<posy<<endl;
	}
	draw(map,curx,cury,posx,posy,"Hey, the lights came back on!");
	//clear screen
	//cout<<string(100,'\n');
	cout<<endl;
	
	score(hp, turns);
	
}