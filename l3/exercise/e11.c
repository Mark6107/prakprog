#include<limits.h>
#include<float.h>
#include<stdio.h>
int main(){
	int i=1; while(i+1>i){i++;}
	printf("My while max: %i. INT_MAX: %i\n",i,INT_MAX);
	
	int h=0;
	for(int j=0; j<j+1;j++){h++;}
	printf("My for max: %i. INT_MAX: %i\n",h,INT_MAX);

	int k=0;
	do k++; while(k<k+1);
	printf("My do max: %i. INT_MAX: %i\n",k,INT_MAX);

	
return 0;
}
