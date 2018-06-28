#include<stdio.h>
#include<assert.h>
#include<math.h>
#include<gsl/gsl_integration.h>

struct bess_params{double x; int n;};

double bess(double t, void * p){
	struct bess_params * params = (struct bess_params *)p;
	double x = (params->x);
	int n = (params->n);
	double f = cos(n*t-x*sin(t))/M_PI;
	return f;
}

int besplot(int n, double x){
	struct bess_params params = {x,n};

	gsl_integration_workspace * w = gsl_integration_workspace_alloc(1e5);
	
	gsl_function F;
	F.function = &bess;
	F.params = &params;

	double result,error;

	gsl_integration_qags(&F,0,M_PI,1e-7,1e-7,1e5,w,&result,&error);

	printf("%i\t%lg\t%lg\t%lg\t%lg\n",n,x,result,jn(n,x),result-jn(n,x));

	gsl_integration_workspace_free(w);
	

	return 0;
}
