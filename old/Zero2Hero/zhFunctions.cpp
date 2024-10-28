#include <iostream>
#include <string>
#include <stdlib.h>
#include <ctime>
#include <conio.h>

using namespace std;
void greeting(){
	//clear screen
	cout<<string(100,'\n');
	
	//Greeting and instructions
	cout<<"  __________ ____   ___   "<<endl;
	cout<<" |__  / ____|  _ \\ / _ \\  "<<endl;
	cout<<"   / /|  _| | |_) | | | | "<<endl;
	cout<<"  / /_| |___|  _ <| |_| | "<<endl;
	cout<<" /____|_____|_| \\_\\\\___/  "<<endl;
	cout<<endl<<"            2"<<endl;
	cout<<"  _   _ _____ ____   ___  "<<endl;
	cout<<" | | | | ____|  _ \\ / _ \\ "<<endl;
	cout<<" | |_| |  _| | |_) | | | |"<<endl;
	cout<<" |  _  | |___|  _ <| |_| |"<<endl;
	cout<<" |_| |_|_____|_| \\_\\\\___/ "<<endl;
	cout<<"--------------------------"<<endl;
	cout<<"Hello, Zero."<<endl;
	cout<<"This is you --> 0"<<endl;
	cout<<"You are on a quest to rescue your twin brother."<<endl;
	cout<<"You are in the TOP LEFT space, your brother is in the BOTTOM RIGHT."<<endl<<endl;
	cout<<"When you step on an EVEN tile, you will gain that much HP."<<endl;
	cout<<"When you step on an ODD tile, you will lose DOUBLE that much HP."<<endl;
	cout<<"After stepping on a tile, it will disappear."<<endl;	
	cout<<"Empty tiles are holes, and you will die if you try to step on one."<<endl<<endl;
	cout<<"Each turn counts against you at the end of the game."<<endl;
	cout<<"To become a HERO, you must earn more HP than turns taken to reach your twin."<<endl<<endl;
	cout<<"Good Luck. Press <ENTER> to begin...";
	cin.clear();
}

void draw(int (&map)[10][20], int curx, int cury, int posx, int posy, const char* msg){
	
	//clear screen
	cout<<string(100,'\n');
	if (msg!="") cout<<"**"<<msg<<"**"<<endl;
	//put a 10 in the last tile hero was on.
	//put a 0 in the current tile hero is on.
	map[cury][curx]=10;
	map[posy][posx]=0;
	
	//draw the map
	for(int i=0; i<41 ; i++) cout<<'-';
	cout<<endl;
	
    for (int i=0; i<(sizeof(map)/sizeof(*map)); i++){
		cout<<' ';
        for(int j=0; j<(sizeof(map[i])/sizeof(*map[i])); j++){
			if(map[i][j]>9) cout<<"  ";
            else cout<<map[i][j]<<' ';
        }
        cout<<endl;
    }
	
	for(int i=0; i<41 ; i++) cout<<'-';
	cout<<endl;
}

void flashlight(int (&map)[10][20], int curx, int cury, int posx, int posy){
	
	//clear screen
	cout<<string(100,'\n');
	
	//put a 10 in the last tile hero was on.
	//put a 0 in the current tile hero is on.
	map[cury][curx]=10;
	map[posy][posx]=0;
	
	//draw the map
	for(int i=0; i<41 ; i++) cout<<'-';
	cout<<endl;
	
    for (int i=0; i<(sizeof(map)/sizeof(*map)); i++){
		cout<<' ';
        for(int j=0; j<(sizeof(map[i])/sizeof(*map[i])); j++){
			if(map[i][j]<10 
			&&	((i-posy>=-1&&i-posy<=1) 
			&&	((j-posx>=-1&&j-posx<=1))
			||	i==9&&j==19)){
				cout<<map[i][j]<<' ';
			}
			else{
				cout<<"  ";
			}
        }
        cout<<endl;
    }
	
	for(int i=0; i<41 ; i++) cout<<'-';
	cout<<endl;
}

void create_map(int (&map)[10][20]){
	//Randomly fill map with numbers
	srand(time(NULL));
	for (int i=0; i<(sizeof(map)/sizeof(*map)); i++){
        for(int j=0; j<(sizeof(map[i])/sizeof(*map[i])); j++){
			map[i][j]=rand()%11+1;
        }
    }
	//Try to prevent impossible maps
	//cout<<endl<<"map[0][1]="<<map[0][1]<<" map[1][0]="<<map[1][0]<<endl;
	getch();
	if((map[0][1]%2!=0 && map[1][0]%2!=0)||
	(map[0][1]%2!=0 && map[1][0]>9)||
	(map[0][1]>9 && map[1][0]%2!=0)||
	(map[0][1]%2>9 && map[1][0]%2>9)){
					create_map(map);
				}
			
	//Starting and Destination points
	map[0][0]=0;
	map[9][19]=0;
}

void score(int hp, int turns){
	//If hero has more hp than turns, you won the game, otherwise, you lost
	if(hp>0 && (hp-turns)>0){
		cout<<"  _   _ _____ ____   ___  "<<endl;
		cout<<" | | | | ____|  _ \\ / _ \\ "<<endl;
		cout<<" | |_| |  _| | |_) | | | |"<<endl;
		cout<<" |  _  | |___|  _ <| |_| |"<<endl;
		cout<<" |_| |_|_____|_| \\_\\\\___/ "<<endl;
		cout<<"--------------------------";
		cout<<endl<<" YOU WIN!"<<endl
		<<" hp: "<<hp<<endl
		<<" turns: "<<turns<<endl
		<<" Your score is "<<hp-turns<<endl;
	}
	
	else{
		cout<<"  __________ ____   ___   "<<endl;
		cout<<" |__  / ____|  _ \\ / _ \\  "<<endl;
		cout<<"   / /|  _| | |_) | | | | "<<endl;
		cout<<"  / /_| |___|  _ <| |_| | "<<endl;
		cout<<" /____|_____|_| \\_\\\\___/  "<<endl;
		cout<<"--------------------------";
		cout<<endl<<" YOU LOSE!"<<endl
		<<" hp: "<<hp<<endl
		<<" turns: "<<turns<<endl
		<<" Your score is "<<hp-turns<<endl;

		}
	cin.clear();
}