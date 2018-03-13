CFLAGS = -I/usr/include
LDLIBS = -L/usr/lib/x86_64-linux-gnu -lgsl -lgslcblas -lm
all: out.txt
out.txt: main
		./main > $@
main: main.c
