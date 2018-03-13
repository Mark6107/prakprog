#include<stdio.h>
#include<math.h>
#include<gsl/gsl_integration.h>

double norm(double x, void * params){
	double alpha = *(double *) params;
	double norm = exp(-alpha*x*x);
	return norm;
}

double ham(double x, void * params){
	double alpha = *(double *) params;
	double ham = exp(-alpha*x*x)*(-alpha*alpha*x*x/2+alpha/2+x*x/2);
	return ham;
}

int main(){
	
	gsl_integration_workspace * w = gsl_integration_workspace_alloc(5000);

	double result1, result2, err1, err2;
	double energy, err;
	double alpha;
	
	gsl_function Norm;
	gsl_function Ham;
	Norm.function = &norm;
	Ham.function = &ham;
	Norm.params = &alpha;
	Ham.params = &alpha;
	
	int i;
	
	for(i=1;i<=300;i++){
		alpha = i/100.;
		gsl_integration_qagi(&Ham,0,1e-3,5000,w,&result1,&err1);
		gsl_integration_qagi(&Norm,0,1e-3,5000,w,&result2,&err2);
		energy = result1/result2;
		err = sqrt(pow(err1,2.)*pow(result2,-2.)+pow(err2,2.)*pow(result1,2.)*pow(result2,-4.));
		printf("%.2f %.5f %.5f\n",alpha,energy,err);
	}
	gsl_integration_workspace_free(w);
	return 0;
}
