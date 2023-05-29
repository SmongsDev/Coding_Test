#include <iostream>
#include <deque>

using namespace std;

deque<int> du;

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	
	int n, m; cin >> n >> m;
	int cnt = 0;
	
	for(int i=1;i<=n;i++){
		du.push_back(i);
	}
	
	while(m--){
		int num; cin >> num;
		int idx;
		int len = du.size();
		for(int i=0;i<len;i++){
			if(du[i] == num){
				idx = i;
			}
		}
		if((idx+1) <= (len-idx)){
			for(int j=0;j<idx;j++){
				du.push_back(du.front());
				du.pop_front();
			}
			cnt += idx;
			du.pop_front();
		}
		else{
			for(int j=0;j<(len-idx);j++){
				du.push_front(du.back());
				du.pop_back();
			}
			cnt += len-idx;
			du.pop_front();
		}
	}
	cout << cnt;
	
	return 0;
}