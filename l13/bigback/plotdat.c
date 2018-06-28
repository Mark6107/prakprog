#include<stdio.h>

int bessel(int n, double x);

int main(){
	
	int i,k;
	double ki;
	for(i=0;i<=3;i++){
		for(k=0;k<=200;k++){
			ki=k/10.0;
			int status = bessel(i,ki);
		}
		printf("\n\n");
	}
	
	return 0;
}
