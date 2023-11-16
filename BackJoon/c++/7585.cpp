#include <iostream>
#include <stack>

using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	
	string str;
	while(getline(cin, str)){
		if(str == "#"){
			break;
		}
		
		int check = 0;
		stack<char> stk;		
		for(char c : str){
			if(c == '('){
				stk.push(c);
			}
			else if(c == '['){
				stk.push(c);
			}
			else if(c == '{'){
				stk.push(c);
			}
			else if(c == ')'){
				if(stk.top() == '('){
					stk.pop();
				}
				else{
					check = 1;
					break;
				}
			}
			else if(c == ']'){
				if(stk.top() == '['){
					stk.pop();
				}
				else{
					check = 1;
					break;
				}
			}
			else if(c == '}'){
				if(stk.top() == '{'){
					stk.pop();
				}
				else{
					check = 1;
					break;
				}
			}
		}
		if(!stk.empty()){
			cout << "Illegal" << "\n";
		}
		else if(check == 0){
			cout << "Legal" << "\n";
		}
		else{
			cout << "Illegal" << "\n";
		}
	}
	
	return 0;
}