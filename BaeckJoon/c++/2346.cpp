#include <iostream>
#include <deque>

using namespace std;

deque<pair<int,int>> du;

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	
	int n; cin >> n;
	
	for(int i=1;i<=n;i++){
		int tmp; cin >> tmp;
		du.push_back(make_pair(tmp,i));
	}
	
	while(!du.empty()){
		int value = du.front().first;
		cout << du.front().second << " ";
		du.pop_front();
		
		if(value > 0){
			for(int i=1;i<value;i++){
				du.push_back(du.front());
				du.pop_front();
			}
		}
		else{
			for(int i=0;i<abs(value);i++){
				du.push_front(du.back());
				du.pop_back();
			}
		}
	}
	
	return 0;
}