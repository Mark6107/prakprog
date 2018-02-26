CFLAGS = -I/usr/include
LDLIBS = -L/usr/lib/x86_64-linux-gnu -lgsl -lgslcblas -lm
all: dat.txt
dat.txt: airy_dat
		./airy_dat > dat.txt
airy_dat: airy_dat.c
