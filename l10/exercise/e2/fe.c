#include<assert.h>
#include<gsl/gsl_odeiv2.h>
#include<gsl/gsl_errno.h>
#include<math.h>
#include<stdio.h>

int wavefun(double r, const double y[], double f[], void* params){
	double e = *(double*)params;
	f[0] = y[1];
	f[1] = -2*(1/r+e)*y[0];
	return GSL_SUCCESS;
}

double fe(double e, double r){
	assert(r>=0.0);
	const double rmin = 1e-3;
	if(r<rmin) return r-r*r;
	
	gsl_odeiv2_system system = {wavefun,NULL,2,&e};
	
	gsl_odeiv2_driver* d = gsl_odeiv2_driver_alloc_y_new
		(&system,gsl_odeiv2_step_rkf45,1e-3,1e-6,1e-6);

	double t=rmin, y[] = {t-t*t, 1-2*t};
	int status = gsl_odeiv2_driver_apply(d, &t, r, y);
	if(status != GSL_SUCCESS) fprintf(stderr,"odeiv2 error in fe: %d\n",status);

	gsl_odeiv2_driver_free(d);

	return y[0];
}
