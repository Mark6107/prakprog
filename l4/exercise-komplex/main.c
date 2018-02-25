#include"komplex.h"
#include<stdio.h>
#include<math.h>
#define TINY 1e-6

int main(){
	komplex a = {1,2}, b = {3,4};
	komplex_print("a=",a);
	komplex_print("b=",b);

	printf("Testing add...\n");
	komplex r1 = komplex_add(a,b);
	komplex R1 = {4,6};
	komplex_print("Add = ",r1);

	if(komplex_equal(R1,r1) )
		printf("Test 'add' passed! \n");
	else
		printf("Test 'add' failed, please debug...\n");

	printf("Testing sub...\n");
	komplex r2 = komplex_sub(a,b);
	komplex R2 = {-2,-2};
	komplex_print("Sub = ",r2);

	if(komplex_equal(R2,r2) )
		printf("Test 'sub' passed! \n");
	else
		printf("Test 'sub' failed, please debug...\n");

	printf("Testing mul...\n");
	komplex r3 = komplex_mul(a,b);
	komplex R3 = {-5,10};
	komplex_print("Mul = ",r3);

	if(komplex_equal(R3,r3) )
		printf("Test 'mul' passed! \n");
	else
		printf("Test 'mul' failed, please debug...\n");
	
	printf("Testing div...\n");
	komplex r4 = komplex_div(a,b);
	komplex R4 = {11/25,2/25};
	komplex_print("Div = ",r4);

	if(komplex_equal(R4,r4) )
		printf("Test 'div' passed! \n");
	else
		printf("Test 'div' failed, please debug...\n");
	
	printf("Testing conjugate...\n");
	komplex r5 = komplex_conju(a);
	komplex R5 = {1,-2};
	komplex_print("Conjugate = ",r5);

	if(komplex_equal(R5,r5) )
		printf("Test 'conju' passed! \n");
	else
		printf("Test 'conju' failed, please debug...\n");
	
	printf("Testing absolute...\n");
	komplex r6 = komplex_abs(a);
	komplex R6 = {pow(5,0.5),0};
	komplex_print("Absolute = ",r6);

	if(komplex_equal(R6,r6) )
		printf("Test 'abs' passed! \n");
	else
		printf("Test 'abs' failed, please debug...\n");
	
	printf("Testing exp...\n");
	komplex r7 = komplex_exp(a);
	komplex R7 = {exp(1)*cos(2),exp(1)*sin(2)};
	komplex_print("Exp = ",r7);

	if(komplex_equal(R7,r7) )
		printf("Test 'exp' passed! \n");
	else
		printf("Test 'exp' failed, please debug...\n");

	printf("Testing sin...\n");
	komplex r8 = komplex_sin(a);
	komplex R8 = {sin(1)*cosh(2),cos(1)*sinh(2)};
	komplex_print("Sin = ",r8);

	if(komplex_equal(R8,r8) )
		printf("Test 'sin' passed! \n");
	else
		printf("Test 'sin' failed, please debug...\n");
	
	printf("Testing cos...\n");
	komplex r9 = komplex_cos(a);
	komplex R9 = {cos(1)*cosh(2),-sin(1)*sinh(2)};
	komplex_print("Cos = ",r9);

	if(komplex_equal(R9,r9) )
		printf("Test 'cos' passed! \n");
	else
		printf("Test 'cos' failed, please debug...\n");

	printf("Testing sqrt...\n");
	komplex r10 = komplex_sqrt(a);
	komplex R10 = {pow((1+pow(5,0.5))/2,0.5),pow((-1+pow(5,0.5))/2,0.5)};
	komplex_print("Sqrt = ",r10);

	if(komplex_equal(R10,r10) )
		printf("Test 'sqrt' passed! \n");
	else
		printf("Test 'sqrt' failed, please debug...\n");
}
