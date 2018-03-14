CFLAGS = -I/usr/include
LDLIBS = -L/usr/lib/x86_64-linux-gnu -lgsl -lgslcblas -lm
all: dat.txt airy_plot.svg
dat.txt: airy_dat
		./airy_dat > dat.txt
airy_dat: airy_dat.c

airy_plot.svg: airy_plot.gpi
		gnuplot airy_plot.gpi
