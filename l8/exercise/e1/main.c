#include<stdio.h>
#include<math.h>
#include<gsl/gsl_matrix.h>
#include<gsl/gsl_odeiv2.h>

int func(double t, double* y, double* f,void * params){
	(void)(t);
	(void)(params);
	double b = *y;
	*f = b * (1.0-b);
	return GSL_SUCCESS;
}


int jac(double t, const double * y, double *dfdy, double *dfdt, void *params){
	(void)(t);
	*dfdt = 1.0-*y;
	return GSL_SUCCESS;
}

int main(){
	
	gsl_odeiv2_system sys = {func, jac, 1};
	
	gsl_odeiv2_driver * d = 
	gsl_odeiv2_driver_alloc_y_new(&sys, gsl_odeiv2_step_rk8pd, 1e-6,1e-6,0.0);
	double x = 0;
	double y = 0.5;
	double s = 0.0;

	for(int i=1; i<=300.;i++){
		double xi = i/100;
		int status = gsl_odeiv2_driver_apply(d,&x,xi,&y);
		
		if(status != GSL_SUCCESS)
		{printf("Error, return value = %d\n", status);break;}
		s = s + y;
		printf("%.5e %.5e\n",x,y);
	}
	gsl_odeiv2_driver_free(d);
	return 0;
}
