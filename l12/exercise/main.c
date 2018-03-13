#include<stdio.h>
#include<gsl/gsl_integration.h>
#include<math.h>
#include<assert.h>

double errf(double x, void * params){
    double f = 2/sqrt(M_PI)*exp(-x*x);
    return f;    
}

int main(int argc, char * argv[]){
    assert(argc==4);
    double a,b,dx;
    sscanf(argv[1],"%lg",&a);
    sscanf(argv[2],"%lg",&b);
    sscanf(argv[3],"%lg",&dx);
    
    double result, error;

    gsl_integration_workspace * w = gsl_integration_workspace_alloc(1000);

    gsl_function F;
    F.function = &errf;
    F.params = NULL;
    for(a;a<=b;a+=dx){

    gsl_integration_qags(&F,0,a,1e-7,1e-7,1000,w,&result,&error);
    
    printf("%lg\t%lg\t%lg\n",a,result,error);
    }
    gsl_integration_workspace_free(w);
    
    return 0;
}
