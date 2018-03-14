#include<stdio.h>
#include<gsl/gsl_linalg.h>
#include<gsl/gsl_blas.h>

int main(){
	double A_data[] = {	6.13, -2.90, 5.86,
						8.08, -6.31,-3.89,
					   -4.36,  1.00, 0.19};
	double b_data[] = {6.23, 5.37, 2.29};
	gsl_matrix_view A = gsl_matrix_view_array(A_data, 3, 3);
	gsl_vector_view b = gsl_vector_view_array(b_data, 3);
	gsl_vector *x = gsl_vector_alloc(3);
	
	int s;
	gsl_permutation * p = gsl_permutation_alloc(3);

	gsl_linalg_LU_decomp(&A.matrix, p, &s);
	gsl_linalg_LU_solve(&A.matrix, p, &b.vector, x);
	

	printf("x = \n");
	gsl_vector_fprintf(stdout, x, "%g");
	
	
	double An_data[] = {	6.13, -2.90, 5.86,
						8.08, -6.31,-3.89,
					   -4.36,  1.00, 0.19};
	gsl_matrix_view An = gsl_matrix_view_array(An_data, 3, 3);
	double c[] = { 0.00, 0.00, 0.00};
	gsl_vector_view C = gsl_vector_view_array(c, 3);
	gsl_blas_dgemv	(CblasNoTrans, 1.0, &An.matrix, x, 0.0, &C.vector);
	printf("A*x = \n %g \n %g \n %g \n",c[0],c[1],c[2]);
	
	gsl_permutation_free(p);
	gsl_vector_free(x);
	return 0;
}
