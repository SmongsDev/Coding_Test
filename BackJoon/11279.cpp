#include <iostream>
#include <queue>

using namespace std;

priority_queue<int> qu;

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	
	int N; cin >> N;
	
	for(int i=0;i<N;i++){
		int n; cin >> n;
		
		if(n == 0){
			if(qu.empty()){
				cout << "0" << "\n";
			}
			else{
				cout << qu.top() << "\n";
				qu.pop();
			}
		}
		else{
			qu.push(n);
		}
	}
	
	return 0;
}