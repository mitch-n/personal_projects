// Example program
#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool is_running=true;

int menu_return(){
    cout<<endl<<"Would you like to return to the menu? (y/n): ";
    char selection;
    cin>>selection;
    switch(selection){
        case 'y':break;
        case 'Y':break;
        case 'n':is_running=false;
        case 'N':is_running=false;
        default:break;
    }
    return 0;
}

int mean(){
    /*
        Okay, so I forgot that MEAN is not the MEDIAN. This function
        sorts all the numbers and it took me a long time and I am proud of it. 
		In the end I adjusted it to find the mean, but I don't want to 
		start over.
    */
	cout<<endl<<"**FIND MEAN**"<<endl;
    vector<int> nums;
    cout << "Enter a list of numbers separated by commas (ie. 1,2,3), then press ENTER...\n";
    string input;

    cin >> input;
    input+=",";
    
    string num_str;
    int num;
    
    //Split input string into vector of ints
    for(int i=0; i < input.length(); i++){
   
        if(input[i]==','){
            if(num_str.size()>0){
                num = stoi(num_str);
                nums.push_back(num);
                num_str="";
            }
        }
        else num_str+=input[i];    
    }
    
    //sort nums
    int min=nums[0];
    int min_index=0;
    vector<int> nums_sorted;
    while(nums.size()>0){
        min=nums[0];
        min_index=0;
        for(int i=1; i< nums.size(); i++){
            if (nums[i]<min){
                min=nums[i];
                min_index=i;
            }
        }
        //remove min from nums, add to nums_sorted
        nums.erase(nums.begin() + min_index);
        nums_sorted.push_back(min);   
    }
    
    //remove max and min if there are at least 3 numbers
    if(nums_sorted.size()>2){
        cout<<"Removing max("<<nums_sorted[nums_sorted.size()-1]<<") and min("<<nums_sorted[0]<<").."<<endl;
        nums_sorted.erase(nums_sorted.begin()+0);
        nums_sorted.erase(nums_sorted.begin()+(nums_sorted.size()-1));
    }
    
    //find mean of remaining numbers
    int sum=0;
    for (int i=0; i<nums_sorted.size(); i++){
        sum+=nums_sorted[i];   
    }
    
    float mean = float(sum)/float(nums_sorted.size());
    
    cout<<"The mean is "<<mean<<endl;
    
    menu_return();
    
    cout<<endl;
    
    return 0;
}

int area_circle(){
	cout<<endl<<"**FIND AREA OF A CIRCLE**"<<endl;
	//used the first 8 places of pi, so this is acurate to 8 decimal places
    double pi = 3.14159265;
    double radius;
    
	//get radius from user
    cout << "What is the radius of the circle?"<<endl;
    cin >> radius;
    
	//calculate area
    double area = (radius*radius)*pi;
    
    cout << "The area of the circle is "<<area<<endl;
    
    menu_return();
    
    cout<<endl;
    
    return 0;   
}

int gcd()
{
	cout<<endl<<"**FIND GREATEST COMMON DIVISOR**"<<endl;
    int a;
    int b;
   
    cout<<"Type a number: ";
    cin>>a;
    cout<<"Type another number: ";
    cin>>b;
   
    int min = (abs(a)<abs(b) ? abs(a):abs(b));
    int gcd=1;
    for (int i=2; i<=min ; i++){
        if (a%i==0 && b%i==0) gcd=i;
    }
    cout<<"The Greatest Common Divisor is: "<<gcd<<endl;
    
    menu_return();
    
    cout<<endl;
    
	return 0;
}

int sum_ints()
{
	cout<<endl<<"**FIND SUM OF NUMBERS**"<<endl;
    string num_str;
    int num;
    vector<int> nums;
   
    cout<<"Type a number: ";
    cin>>num_str;
   
    for (int i=0 ; i<num_str.size() ; i++){
        nums.push_back(num_str[i]-'0');
    }
   
    int total=0;
    for (int i=0 ; i<nums.size() ; i++){
        total+=nums[i];
    }
   
    cout<<"Total="<<total<<endl;
	
	menu_return();
	
	cout<<endl;
	
	return 0;
}

int main(){
	
	int selection;
	bool not_exit=true;
	while(not_exit && is_running){
		cout<<"-------------Math Menu-------------\n";
		cout<<"1) Find Mean"<<endl;
		cout<<"2) Find Area of a Circle"<<endl;
		cout<<"3) Find Greatest Common Divisor"<<endl;
		cout<<"4) Find Sum of Numbers"<<endl;
		cout<<"0) Exit"<<endl;
		cout<<"-----------------------------------\n";
		
		bool bad_selection=true;
		while(bad_selection){
			cout<<"Please make a selection: ";
			cin>>selection;
			switch(selection){
				case 1:mean(); bad_selection=false; break;
				case 2:area_circle(); bad_selection=false; break;
				case 3:gcd(); bad_selection=false; break;
				case 4:sum_ints(); bad_selection=false; break;
				case 0:not_exit=false; bad_selection=false; break;
				default: cout<<"invalid selection"<<endl;
			}
		}
	}
	
	cout<<endl<<"Goodbye!"<<endl;
	return 0;
	
}