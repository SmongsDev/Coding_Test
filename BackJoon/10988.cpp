#include <iostream>

using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	
	string str;	cin >> str;
	
	for(int i=0;i<str.length()/2;i++){
		if(str[i] != str[str.length()-i-1]){
			cout << "0";
			exit(0);
		}
	}
	cout << "1";
	return 0;
}