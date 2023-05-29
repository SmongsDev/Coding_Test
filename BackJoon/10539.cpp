#include <iostream>

using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	
	int n;
	cin >> n;
	
	int result;
	int tmp = 0;
	for(int i=1;i<=n;i++){
		int seq; cin >> seq;
		
		cout << seq * i - tmp << " ";
		tmp = seq * i;
	}
	
	return 0;
}