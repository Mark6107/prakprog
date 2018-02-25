#include<stdio.h>
#include<stdlib.h>
double* foo(){static double a[]={0,0,0}; return a;};
int main(){
	double* a=foo(); a[2]=1;
	double* b=foo(); b[2]=2;
	printf("a[2] = %g\n",a[2]);
return EXIT_SUCCESS;}
