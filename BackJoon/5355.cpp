#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	
	int n; cin >> n;
	for(int i=0;i<n;i++){
		double num; cin >> num;
		
		while(1){
			char tmp; 
			tmp = cin.get();
			if(tmp == '\n'){
				break;
			}
			else if(tmp == '@'){
				num *= 3;
			}
			else if(tmp == '%'){
				num += 5;
			}
			else if(tmp == '#'){
				num -= 7;
			}
		}
		cout << fixed; // 소수점 아래 숫자의 출력 범위만 설정
		cout.precision(2); // 전체(실수의 정수부와 소수부를 합친) 범위를 설정하는 함수
		cout << num << "\n";
		
	}
	
	return 0;
}