#include<stdio.h>
#include<limits.h>
#include<float.h>

int main(){
	int max=INT_MAX/2;
	float sum_upf=0.0; float sum_downf=0.0;
	double sum_upd = 0.0; double sum_downd = 0.0;
	int s=1;
	for(s=1; s<=max; ++s){
		sum_upf += 1.0f/s;
		sum_downf += 1.0f/(max-s+1);
		sum_upd += 1.0/s;
		sum_downd += 1.0/(max-s+1);
		}
	printf("Sum up float: %g\nSum down float: %g\n",sum_upf,sum_downf);
	printf("At sum up, it first starts to remember the long-out decimals later, while sum down remembers the long-out decimals from the start.\n");
	printf("No, as the numerical difference of float gives this difference.\n");
	printf("Sum up double: %g\nSum down double: %g\n",sum_upd,sum_downd);
}
