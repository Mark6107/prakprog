#include<stdio.h>
void print_f_of_one(double (*f)(double)){printf("%g\n",f(1.0));}
int main(){
	#define f(x) (x)+(x)
	printf("%g\n",f(1.0));
	return 0;
}
