#include <iostream>
#include <stack>

using namespace std;

int main(int argc, char* argv[]) {
	string S;
	cin >> S;
	
	stack<char> arr1;
	stack<int> arr2;
	
	int len = 0;
	
	for(int i = 0; i < S.length(); i++){
		char ch = S[i];
		if(ch == '('){
			arr1.push((char)S[i-1]);
			arr2.push(len-1);
			len = 0;
		}
		else if(ch == ')'){
			char tmp = arr1.top();
			int Len = arr2.top();
			arr1.pop();
			arr2.pop();
			
			len = Len + (((int)tmp-48) * len);
			
		}
		else{
			len = len + 1;
		}
	}
	cout << len << endl;
}