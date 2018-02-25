CFLAGS = -std=gnu99 -Wall -0

.PHONY:default
default: out.txt
	cat out.txt

out.txt: math1 math2
	./math1 > out.txt
	./math2 >> out.txt

math1: math1.c
	cc math1.c -o math1 -lm

math2: math2.c
	cc math2.c -o math2 -lm

.PHONY:clean
clean:
	rm -f out.txt math1 math2
