#include <iostream>
#include <algorithm>
#include <map>

using namespace std;

// long long arr[100000000] = {1};
map<long long, long long> arr = {{0,1}};
long long N, P, Q;

long long func(long long x){
	if(arr[x]){
		return arr[x];
	}
	else{
		return arr[x] = func(x / P) + func(x / Q);
	}	
}

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	
	cin >> N >> P >> Q;
	
	cout << func(N);
	return 0;
}