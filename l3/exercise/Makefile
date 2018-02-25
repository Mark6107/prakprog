CFLAGS = -std=gnu99 -Wall -0

.PHONY:default
default: out.txt
	cat out.txt

out.txt: e3
	./e3.o > out.txt

e3: e3.c
	gcc e3.c -o e3.o

.PHONY:clean
clean:
	rm -f out.txt e3.o
