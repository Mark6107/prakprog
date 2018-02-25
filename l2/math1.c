#include<stdio.h>
#include<math.h>
#include<complex.h>
int main(){
	double n1=gamma(5);
	printf("Gamma(5)=%g\n",n1);
	double n2=j1(0.5);
	printf("Bessel(0.5)=%g\n",n2);
	double complex n3=cpow(-2.0,0.5),n4=cpow(M_E,I),n5=cpow(M_E,I*M_PI),n6=cpow(I,M_E);
	printf("Sqrt(-2)=%g+%gi\n",creal(n3),cimag(n3));
	printf("exp(i)=%g+%gi\n",creal(n4),cimag(n4));
	printf("exp(i*pi)=%g+%gi\n",creal(n5),cimag(n5));
	printf("i**e=%g+%gi\n",creal(n6),cimag(n6));
	return 0;
}
