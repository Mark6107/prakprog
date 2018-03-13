CFLAGS = -I/usr/include
LDLIBS = -L/usr/lib/x86_64-linux-gnu -lgsl -lgslcblas -lm
default: h_plot.svg
h_plot.svg: out.txt hydrogenplot.gpi
	gnuplot hydrogenplot.gpi
hydrogenplot.gpi:
out.txt: main
	./$< > $@
main: main.c fe.c
