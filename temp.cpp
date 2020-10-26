#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int T,arr[100];
	int sum=0;
	long long temp;
	cin>>T;
	for (int i=0;i<T;i++){
	    cin>>temp;
	    sum=0;
	    while (temp!=0){
	        sum+=temp%10;
	        temp=temp/10;
	    }
	    arr[i]=sum;
	    
	}
	for(int j=0;j<T;j++){
	    cout<<arr[j]<<endl;
	}
	
	
}
