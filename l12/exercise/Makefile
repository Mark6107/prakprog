FLAGS = -I/usr/include
LDLIBS = -L/usr/lib/x86_64-linux-gnu -lgsl -lgslcblas -lm

all: report.pdf

report.pdf: report.bbl report.tex ferr.pdf
	pdflatex report.tex
	pdflatex report.tex

report.bbl: report
	biber report

report: bibl.bib
	pdflatex report.tex 


ferr.pdf: out.txt plotit.gpi
	gnuplot plotit.gpi

plotit.gpi:

out.txt: main
	./$< -3 3 0.01 > $@

main: main.c

