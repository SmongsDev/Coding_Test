#include <iostream>
#include <algorithm>

using namespace std;

int arr[10000];

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	
	int n;
	cin >> n;
	
	int prefix = 0;
	int minN = 0;
	int result = -10000;
	
	for(int i = 0; i < n; i++){
		cin >> arr[i];
		prefix+=arr[i];
		result=max(result,prefix-minN);
		minN=min(minN,prefix);
	}
	cout << result;
	return 0;
}