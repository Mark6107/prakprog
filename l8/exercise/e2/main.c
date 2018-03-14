#include<stdio.h>
#include<gsl/gsl_matrix.h>
#include<gsl/gsl_odeiv2.h>
#include<math.h>

// Function for integration
int func(double t, const double y[], double f[], void *params){
	// Avoiding warning if unused
	(void)(t);
	double eps = *(double *)params;
	// Differential equations
	f[0] = y[1];
	f[1] = 1-y[0]+eps*y[0]*y[0];
	return GSL_SUCCESS;
}

// Jacobian function of system
int jac(double t, const double y[], double *dfdy, double dfdt[], void *params){
	// Avoiding warning if unused
	(void)(t); 	double eps = *(double *)params; 
	// Make matrix of dfdy array
	gsl_matrix_view dfdy_mat = gsl_matrix_view_array(dfdy, 2, 2);
	// Pointer for easier use of matrix
	gsl_matrix * m = &dfdy_mat.matrix;
	// Set indexes of the jacobian matrix
	gsl_matrix_set(m,0,0,0.0);
	gsl_matrix_set(m,1,0,-1+2*y[0]);
	gsl_matrix_set(m,0,1,1);
	gsl_matrix_set(m,1,1,0);
	// Dfdt values of system
	dfdt[0] = 0.0;
	dfdt[1] = 0.0;
	return GSL_SUCCESS;
}

int main(){
	double eps;
	// Declaring the general system of equations
	gsl_odeiv2_system sys = {func, jac, 2, &eps};
	// Declaring pointer to driver, that increments functions in steps 1e-6 up to the given increment when called
	gsl_odeiv2_driver * d = gsl_odeiv2_driver_alloc_y_new (&sys, gsl_odeiv2_step_rk8pd,1e-6,1e-6,0.0);
	// Constants for integration
	int i;
	int k;
	double t, t1 = 4*M_PI;
	double y[2];
	double E[3] = {0.0,0.0,0.01};
	double y1[3] = {0.0,-0.5,-0.5};
	
	// Loop over the 3 different cases
	for(k=1;k<=3;k++){
		t = 0.0;	
		y[0] = 1;
		y[1] = y1[k-1];
		eps = E[k-1];

	for(i=1; i<=300;i++){
		// Increments
		double ti = i*t1/300.0;
		// Applying driver, telling it to go from t to ti
		int status = gsl_odeiv2_driver_apply(d,&t,ti,y);
		// If something goes wrong, stop integrating
		if(status != GSL_SUCCESS){
			printf("Error, return value=%d\n",status);
			break;
		}
		// Print out results in seperate lines for each iteration
		printf("%.5e %.5e %.5e\n",t,y[0],y[1]);
	}
	// Make 2 blank lines between each of the three cases
	printf("\n\n");
	}
	// Free up the designated space for driver
	gsl_odeiv2_driver_free(d);
	
	return 0;
}
