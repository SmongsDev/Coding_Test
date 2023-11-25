#include <iostream>
#include <stack>
#include <utility>

using namespace std;

stack<pair<int, int>> stk;

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	
	int N; cin >> N;
	stk.push(make_pair(100000001,0));
	for(int i=1;i<=N;i++){
		int top; cin >> top;
		
		while(stk.top().first < top){
			stk.pop();
		}
		
		cout << stk.top().second << " ";
		stk.push(make_pair(top,i));
	}
	
	return 0;
}