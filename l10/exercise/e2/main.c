#include<stdio.h>
#include<math.h>
#include<gsl/gsl_odeiv2.h>
#include<gsl/gsl_multiroots.h>
#include<assert.h>
#include<gsl/gsl_vector.h>

double fe(double e, double r);

int master(const gsl_vector *ev, void *params, gsl_vector *f){
	double e = gsl_vector_get(ev,0);
	assert(e<0);
	double rmax = *(double*)params;
	double fval = fe(e,rmax);
	gsl_vector_set(f,0,fval);
	return GSL_SUCCESS;
}

int main(){
	double rmax = 8;

	gsl_multiroot_fsolver * s = gsl_multiroot_fsolver_alloc(gsl_multiroot_fsolver_hybrid, 1);
	
	gsl_multiroot_function F;
	F.f = master;
	F.n = 1;
	F.params = &rmax;
	
	gsl_vector *ev = gsl_vector_alloc(1);
	gsl_vector_set(ev,0,-1);

	gsl_multiroot_fsolver_set(s, &F, ev);

	int status, iter=0;
	
	do{
		iter++;
		status = gsl_multiroot_fsolver_iterate(s);
		if(status){
			fprintf(stderr,"Break, error in multiroot iterate!");
			break;}
		fprintf(stderr,"Iteration %i\n",iter);
		
		status = gsl_multiroot_test_residual(s->f,1e-3);
		if(status==GSL_SUCCESS)fprintf(stderr,"Function converged!\n");
	}while(status==GSL_CONTINUE && iter<500);

	double e = gsl_vector_get(s->x,0);
	printf("%g %g\n\n\n",rmax,e);
	for(double r=0.0;r<=rmax;r+=rmax/64)printf("%g %g %g\n",r,fe(e,r),r*exp(-r));
	

	gsl_multiroot_fsolver_free(s);
	gsl_vector_free(ev);
	return 0;
}
