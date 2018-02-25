#include<stdio.h>
static int x = 0;

void func1(int x) {
	x++;
	printf("x=%i\n",x);
}

void func2(int x) {
	x--;
	printf("x2=%i\n",x);
}

int main() {
	func1(x);
	func1(x);
	func1(x);
	func2(x);
	func2(x);
	func2(x);
	return 0;
}
