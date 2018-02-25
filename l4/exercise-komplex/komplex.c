#include<stdio.h>
#include<math.h>
#include"komplex.h"
#define TINY 1e-6

void komplex_print(char *s, komplex a){
	printf("%s (%g,%g)\n",s, a.re, a.im);
}

komplex komplex_new(double x, double y){
	komplex z = {x, y};
	return z;
}

void komplex_set(komplex* z, double x, double y){
	(*z).re = x;
	(*z).im = y;
}

komplex komplex_add(komplex a, komplex b){
	komplex result = {a.re + b.re, a.im + b.im};
	return result;
}

komplex komplex_sub(komplex a, komplex b){
	komplex result = {a.re - b.re, a.im - b.im};
	return result;
}

int komplex_equal(komplex a, komplex b){
	if(a.re-b.re<TINY && a.im-b.im<TINY)
		return 1;
	return 0;
}

komplex komplex_mul(komplex a, komplex b){
	komplex result = {a.re*b.re - a.im*b.im, a.im*b.re + a.re*b.im};
	return result;
}

komplex komplex_div(komplex a, komplex b){
	if(b.re==0 && b.im==0){
		komplex result = {0,0};
		return result;}
	komplex result = {(a.re*b.re+a.im*b.im)/(pow(b.re,2)+pow(b.im,2)),
					(a.im*b.re-a.re*b.im)/(pow(b.re,2)+pow(b.im,2))};
	return result;
}

komplex komplex_conju(komplex z){
	komplex result = {z.re, -z.im};
	return result;
}

komplex komplex_abs(komplex z){
	komplex result = {pow((pow(z.re,2)+pow(z.im,2)),0.5),0};
	return result;
}

komplex komplex_exp(komplex z){
	komplex result = {exp(z.re)*cos(z.im),exp(z.re)*sin(z.im)};
	return result;
}

komplex komplex_sin(komplex z){
	komplex result = {sin(z.re)*cosh(z.im),cos(z.re)*sinh(z.im)};
	return result;
}

komplex komplex_cos(komplex z){
	komplex result = {cos(z.re)*cosh(z.im), -sin(z.re)*sinh(z.im)};
	return result;
}

komplex komplex_sqrt(komplex z){
	komplex result = {
		pow(0.5*(z.re+pow((pow(z.re,2)+pow(z.im,2)),0.5)),0.5),
		pow(0.5*(pow((pow(z.re,2)+pow(z.im,2)),0.5)-z.re),0.5)*z.im/fabs(z.im)};
		return result;		
}
