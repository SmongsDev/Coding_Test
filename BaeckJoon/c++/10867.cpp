#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> v;

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	
	int N; cin >> N;
	
	for(int i=0;i<N;i++){
		int tmp; cin >> tmp;
		v.push_back(tmp);
	}
	
	sort(v.begin(), v.end());
	// unique의 리턴값은 중복되지 않은 마지막 요소의 다음 값이다.
	// 1 2 2 3 => 1 2 3 2(리턴값) 그래서 erase의 첫 값이 2(리턴값)이 됨.
	v.erase(unique(v.begin(), v.end()), v.end()); 
	
	for(int i=0; i<v.size();i++){
		cout << v[i] << " ";
	}
	
	return 0;
}