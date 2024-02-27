#include <iostream>

using namespace std;

int arr[26];

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	
    string s; cin >> s;
    
    for(int i=0; i<s.size(); i++){
        arr[s[i] - 'a']++;
    }
    for(int i=0; i<26; i++){
        cout << arr[i] << " ";
    }	
	return 0;
}