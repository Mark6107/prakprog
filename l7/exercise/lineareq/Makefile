CFLAGS = -I/usr/include
LDLIBS = -L/usr/lib/x86_64-linux-gnu -lgsl -lgslcblas -lm
all: out.txt
		cat $<
out.txt: leq
		./leq > $@
leq: leq.c
