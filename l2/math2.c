#include<stdio.h>
int main(){

float n1 = 0.1111111111111111111111111111;
double n2 = 0.1111111111111111111111111111;
long double n3 = 0.1111111111111111111111111111L;

printf("Float: %.25g\nDouble: %.25lg\nLong: %.25\n",n1,n2,n3);

return 0;

}
