CFLAGS = -I/usr/include
LDLIBS = -L/usr/lib/x86_64-linux-gnu -lgsl -lgslcblas -lm

all: pathplot.svg

pathplot.svg: out.txt plotit.gpi
	gnuplot plotit.gpi

out.txt: main
	./$< > $@
main: main.c
