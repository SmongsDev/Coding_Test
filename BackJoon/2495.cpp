#include <iostream>

using namespace std;

int main(int argc, char* argv[]) {
	string str;
	for(int i = 0; i < 3; i++){		
		cin >> str;
		
		int maxCnt = 1;
		int cnt = 1;
		for(int j = 1; j < str.length(); j++){
			if(str[j-1] == str[j]){
				cnt++;
			}
			else {
				cnt = 1;
			}
			if(cnt > maxCnt){
				maxCnt = cnt;
			}
		}
		cout << maxCnt << endl;
	}
	
}