#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

priority_queue<int> qu;
	
int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	
	int N;
	cin >> N;
	
	for (int i = 0; i < N; i++){
		int num;
		cin >> num;
		
		if(num == 0){
			if(qu.empty()){
				cout << "0" << "\n";
			}
			else{
				cout << -qu.top() << "\n";
				qu.pop();
			}
		}
		else{
			qu.push(-num);
		}
		
	}
	
	return 0;
}