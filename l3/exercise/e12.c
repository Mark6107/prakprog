#include<limits.h>
#include<float.h>
#include<stdio.h>
int main(){
	int i=0; while(i-1<i){i--;}
	printf("My while min: %i. INT_MIN: %i\n",i,INT_MIN);
	
	int h=0;
	for(int j=0; j-1<j;j--){h--;}
	printf("My for min: %i. INT_MIN: %i\n",h,INT_MIN);

	int k=0;
	do k++; while(k-1<k);
	printf("My do min: %i. INT_MIN: %i\n",k,INT_MIN);

	
return 0;
}
