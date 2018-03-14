#include<stdio.h>
#include<gsl/gsl_multimin.h>
#include<gsl/gsl_vector.h>
#include<math.h>

struct exp_dat {int n; double *t,*y,*e;};

double master(const gsl_vector *x, void *params) {
	double  A = gsl_vector_get(x,0);
	double  T = gsl_vector_get(x,1);
	double  B = gsl_vector_get(x,2);
	struct exp_dat *p = (struct exp_dat*) params;
	int     n = p->n;
	double *t = p->t;
	double *y = p->y;
	double *e = p->e;
	double sum=0;
	#define f(t) A*exp(-(t)/T) + B
	for(int i=0;i<n;i++){ sum+= pow( (f(t[i]) - y[i]) /e[i] ,2.0);};
	return sum;
}

int main(){
	//Setup of data
	double t[]= {0.47,1.41,2.36,3.30,4.24,5.18,6.13,7.07,8.01,8.95};
	double y[]= {5.49,4.08,3.54,2.61,2.09,1.91,1.55,1.47,1.45,1.25};
	double e[]= {0.26,0.12,0.27,0.10,0.15,0.11,0.13,0.07,0.15,0.09};
	int n = sizeof(t)/sizeof(t[0]);
	
	struct exp_dat p = {.n=n,.t=t,.y=y,.e=e};
	
	// Setup of environment
	const gsl_multimin_fminimizer_type *T;
	T = gsl_multimin_fminimizer_nmsimplex2;
	gsl_multimin_fminimizer *s = gsl_multimin_fminimizer_alloc(T,3);
	gsl_multimin_function F = {.n=3,.f=&master,.params=(struct exp_dat*)&p};
	
	// Guess of starting steps
	gsl_vector *step = gsl_vector_alloc(3);
	gsl_vector_set(step,0,0.1);
	gsl_vector_set(step,1,0.1);
	gsl_vector_set(step,2,0.1);
	
	// Starting point
	gsl_vector *x = gsl_vector_alloc(3);
	gsl_vector_set(x,0,1.0);
	gsl_vector_set(x,1,1.0);
	gsl_vector_set(x,2,1.0);
	
	size_t iter=0;
	int status;

	gsl_multimin_fminimizer_set(s,&F,x,step);
	do{
		iter++;
		status = gsl_multimin_fminimizer_iterate(s);
		if(status){
			fprintf(stderr,"Iteration failed, error %i\n",status);
			break;
		}
		status = gsl_multimin_test_size(s->size,1e-3);
		
		if(status == GSL_SUCCESS)
			fprintf(stderr,"Fitting succeeded!\n");
	}while(status==GSL_CONTINUE && iter<1e5);

	double Af = gsl_vector_get(s->x,0);
	double Tf = gsl_vector_get(s->x,1);
	double Bf = gsl_vector_get(s->x,2);
	
	int i;
	for(i=0;i<n;i++){
		printf("%g %g %g\n",t[i],y[i],e[i]);
	}
	printf("\n\n");
	double tt;
	#define ff(t) Af*exp(-(t)/Tf) + Bf
	for(i=0;i<=100;i++){
		tt = i/10.0;
		printf("%g %g\n",tt,ff(tt));
	}
		
	gsl_multimin_fminimizer_free(s);
	gsl_vector_free(x);
	gsl_vector_free(step);

	return 0;
}
