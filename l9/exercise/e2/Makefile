CFLAGS = -I/usr/include
LDLIBS = -L/usr/lib/x86_64-linux-gnu -lgsl -lgslcblas -lm
all: energyplot.svg
energyplot.svg: energyplot.gpi
	gnuplot energyplot.gpi
energyplot.gpi: out.txt
out.txt: main
	./$< > $@
main: main.c
