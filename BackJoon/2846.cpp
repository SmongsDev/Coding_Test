#include <iostream>

using namespace std;

int main(int argc, char* argv[]) {
	int N;
	cin >> N;
	
	int arr[N];
	for(int i = 0; i < N; i++){
		cin >> arr[i];
	}
	
	int maxHeight = 0;
	int height = 0;
	for(int i = 1; i < N; i++){
		if(arr[i-1] < arr[i]){
			height = height + (arr[i] - arr[i-1]);
		}
		else{
			height = 0;
		}
		if(maxHeight < height){
			maxHeight = height;
		}
	}
	cout << maxHeight << endl;
}