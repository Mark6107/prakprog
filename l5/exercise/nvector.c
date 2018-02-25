#include<stdio.h>
#include<stdlib.h>
#include"nvector.h"

nvector* nvector_alloc(int n){
	nvector* v = malloc(sizeof(nvector));
	(*v).size = n;
	(*v).data = malloc(n*sizeof(double));
	if( v==NULL) fprintf(stderr, "Error in nvector_alloc\n");
	return v;}

void nvector_free(nvector* v){free(v->data); free(v);}

void nvector_set(nvector* v, int i, double value){ (*v).data[i]=value;}

double nvector_get(nvector* v, int i){return (*v).data[i];}

nvector* vector_dot_product(nvector* u, nvector* v){
	if((*u).size != (*v).size){
		fprintf(stderr, "Error in nvector_dot_product, not same size\n");
		nvector* w = NULL;
		return w;}
	else{
		nvector* w = nvector_alloc((*u).size);
		int i=0;
		for(i=0;i<(*u).size;i++)nvector_set(w, i, (*u).data[i]*(*v).data[i]);
		return w;}
}
