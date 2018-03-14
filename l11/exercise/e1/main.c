#include<stdio.h>
#include<math.h>
#include<gsl/gsl_multimin.h>
#include<gsl/gsl_vector.h>


double rosenfun(const gsl_vector *v, void *params){
	double x,y;
	double *p= (double*)params;

	x = gsl_vector_get(v,0);
	y = gsl_vector_get(v,1);

	return p[0]*pow(1-x,2.0)+p[1]*pow(y-x*x,2.0);
}

int main(){
	double p[2] = {1,100};
	size_t iter = 0;
	int status;

	const gsl_multimin_fminimizer_type *T; 
	T = gsl_multimin_fminimizer_nmsimplex2;
	gsl_multimin_fminimizer *s = gsl_multimin_fminimizer_alloc(T,2);
	
	gsl_multimin_function F= {.n=2,.f=&rosenfun,.params=(void *)p};
	
	gsl_vector *step = gsl_vector_alloc(2);
	gsl_vector_set(step,0,0.01);
	gsl_vector_set(step,1,0.01);
	// Starting point
	gsl_vector *x = gsl_vector_alloc(2);
	gsl_vector_set(x,0,5);
	gsl_vector_set(x,1,5);
	
	gsl_multimin_fminimizer_set(s,&F,x,step);
	do{
		iter++;
		status = gsl_multimin_fminimizer_iterate(s);
		if(status){
			fprintf(stderr,"Iteration failed, error %i\n",status);
			break;
		}
		status = gsl_multimin_test_size(s->size,1e-3);

		printf("%lu %g %g %g\n",iter,
			gsl_vector_get(s->x,0),
			gsl_vector_get(s->x,1),
			s->fval);
		if(status == GSL_SUCCESS)
			printf("\n\nMinimum found at f=%g\n",s->fval);
	}while(status==GSL_CONTINUE && iter<1e5);
	

	gsl_multimin_fminimizer_free(s);
	gsl_vector_free(x);
	gsl_vector_free(step);
	return 0;
}
