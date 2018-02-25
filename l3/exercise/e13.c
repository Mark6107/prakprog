#include<float.h>
#include<stdio.h>
int main(){
	float i=1; while(1+i!=1){i/=2;} i*=2;
	double j=1; while(1+j!=1){j/=2;} j*=2;
	long double k=1; while(1+k!=1){k/=2;} k*=2;
	printf("My while vs. .h; float, double, LD\n %g %g\n %g %g\n %Lg %Lg\n",i,FLT_EPSILON,j,DBL_EPSILON,k,LDBL_EPSILON);
	
	float l=1; do l/=2; while(l+1!=1); l*=2;
	double m=1; do m/=2; while(m+1!=1); m*=2;
	long double n=1; do n/=2; while(n+1!=1); n*=2;
	printf("My do vs. .h; float, double, LD\n %g %g\n %g %g\n %Lg %Lg\n",l,FLT_EPSILON,m,DBL_EPSILON,n,LDBL_EPSILON);
	
	float x; for(x=1; 1+x!=1; x/=2){} x*=2;
	double y; for(y=1; 1+y!=1; y/=2){} y*=2;
	long double z; for(z=1; 1+z!=1; z/=2){} z*=2;
	printf("My for vs. .h; float, double, LD\n %g %g\n %g %g\n %Lg %Lg\n",x,FLT_EPSILON,y,DBL_EPSILON,z,LDBL_EPSILON);

	return 0;
}
