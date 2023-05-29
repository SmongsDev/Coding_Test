#include <iostream>
#include <stack>

using namespace std;

stack<char> stk;
stack<char> tmp;

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	
	string str; cin >> str;
	for(char s : str){
		stk.push(s);
	}
	int n; cin >> n;
	
	for(int i=0;i<n;i++){
		char edit; cin >> edit;
		
		if(edit == 'L'){
			if(!stk.empty()){
				tmp.push(stk.top());
				stk.pop();
			}
		}
		else if(edit == 'D'){
			if(!tmp.empty()){
				stk.push(tmp.top());
				tmp.pop();
			}
		}
		else if(edit == 'B'){
			if(!stk.empty()){
				stk.pop();
			}
		}
		else if(edit == 'P'){
			char c; cin >> c;
			stk.push(c);
		}
	}
	
	while(!stk.empty()){
		tmp.push(stk.top());
		stk.pop();
	}
	while(!tmp.empty()){
		cout << tmp.top();
		tmp.pop();
	}
	
	
	
	return 0;
}