#include <iostream>
using namespace std; 

int main (){

string first_name, occupation, age ;


cout << " Please enter your first name : " ;
cin >> first_name; 

cout << " Pleasure to meet you " << first_name ; 

cout << ". Now " << first_name << ", please provide your occupation: ";
cin >> occupation ; 

cout << " So your a " << occupation << ", exciting." <<  endl; 

cout << "  Lastly, please tell me how old your are and we'll begin the next phase" << endl;
cout << " Age: " ; 

cin >> age;

return 0 ;


}
