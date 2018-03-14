#include<gsl/gsl_sf_airy.h>
#include<gsl/gsl_sf.h>
#include<stdio.h>

int main(){
	for(double i=-200;i<41;i++){
		double x = i/20;
		gsl_mode_t acc = GSL_PREC_DOUBLE;
		double a = gsl_sf_airy_Ai(x, acc);
		double b = gsl_sf_airy_Bi(x, acc);
		printf("%lg \t %lg \t %lg\n",x,a,b);
	}
	return 0;
}
