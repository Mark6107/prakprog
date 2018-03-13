#include<stdio.h>
#include<math.h>
#include<gsl/gsl_multiroots.h>
#include<gsl/gsl_vector.h>

int print_state(size_t iter, gsl_multiroot_fsolver * s){
	printf("iter = %3u , x = %.3f,%.3f , f(x) = % .3e,% .3e\n",
			iter,
			gsl_vector_get(s->x, 0),
			gsl_vector_get(s->x, 1),
			gsl_vector_get(s->f, 0),
			gsl_vector_get(s->f, 1));
	return 0;
}

int rosengrad(const gsl_vector * x, void *params, gsl_vector * f){
	double a = *(double *) params;
	const double x0 = gsl_vector_get(x,0);
	const double x1 = gsl_vector_get(x,1);
	
	const double f0 = 2*x1-2-400*(x1-pow(x0,2.0));
	const double f1 = 200*(x1-pow(x0,2.0));

	gsl_vector_set(f,0,f0);
	gsl_vector_set(f,1,f1);
	return GSL_SUCCESS;
}

int main(){
	const gsl_multiroot_fsolver_type *T;
	gsl_multiroot_fsolver *s;
	
	int status;
	size_t i, iter = 0;

	const size_t n = 2;
	double a = 0.0;
	gsl_multiroot_function f = {&rosengrad, n, &a};

	double x_init[2] = {-10.0, -5.0};
	gsl_vector *x = gsl_vector_alloc(n);

	gsl_vector_set(x, 0, x_init[0]);
	gsl_vector_set(x, 1, x_init[1]);

	T = gsl_multiroot_fsolver_hybrids;
	s = gsl_multiroot_fsolver_alloc(T, 2);
	gsl_multiroot_fsolver_set(s,&f, x);
	
	printf("Following is the iteration numbers (iter), the points where the algorithm calculated the gradient (x), and the gradients of the points (f(x))\n");
	
	print_state(iter, s);
	do{
		iter+=1;
		status = gsl_multiroot_fsolver_iterate(s);

		print_state(iter, s);
		if(status)
			break;

		status = gsl_multiroot_test_residual(s->f, 1e-7);
	}
	while(status == GSL_CONTINUE && iter < 1000);
	printf("Status = %s\n",gsl_strerror(status));
	printf("Total number of iterations = %3u\n",iter);
	gsl_multiroot_fsolver_free(s);
	gsl_vector_free(x);
	
	return 0;
}
