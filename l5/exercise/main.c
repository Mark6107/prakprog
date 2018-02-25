#include"nvector.h"
#include<stdio.h>
#include<stdlib.h>
#define RND (double)rand()/RAND_MAX

int main(){
	int n = 5;
	printf("\nMain: Testing nvector_alloc ...\n");
	nvector* v = nvector_alloc(n);
	if( v == NULL) printf("Test failed...\n");
	else printf("Test passed!\n");

	printf("\nMain: Testing nvector_set and nvector_get ..\n");
	double value = RND;
	int i = n / 2;
	nvector_set(v, i, value);
	double vi = nvector_get(v, i);
	if(vi == value)printf("Test passed!\n");
	else printf("Test failed...\n");

	nvector_free(v);

	return 0;
}
