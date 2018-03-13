CFLAGS = -I/usr/include
LDLIBS = -L/usr/lib/x86_64-linux-gnu -lgsl -lgslcblas -lm
all: plot
plot: out.txt
		gnuplot plotorb.gpi
out.txt: main
		./main > $@
main1: main.c
	
