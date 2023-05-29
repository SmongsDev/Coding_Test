#include <iostream>
#include <stack>

using namespace std;

stack<char> stk;

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	
	string str;
	cin >> str;
	int result = 0;
	
	for (int i=0; i<str.length(); i++){
		char s = (char)str[i];
		if(s == '('){
			stk.push(s);
		}
		else if (s == ')'){
			if((char)str[i-1] == '('){
				stk.pop();
				result += stk.size();
			}
			else{
				stk.pop();
				result++;
			}
		}
	}
	cout << result;
	
	return 0;
}