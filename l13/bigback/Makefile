FLAGS = -I/usr/include
LDLIBS = -L/usr/lib/x86_64-linux-gnu -lgsl -lgslcblas -lm

all: report.pdf

report.pdf: report.bbl report.tex fig.pdf fig2.pdf
	pdflatex report.tex
	pdflatex report.tex

report.bbl: report
	biber report

report: bibl.bib
	pdflatex report.tex 


fig.pdf: out.txt plotit.gpi
	gnuplot plotit.gpi
fig2.pdf: out.txt plotit2.gpi
	gnuplot plotit2.gpi

out.txt: main plotdat
	./plotdat > $@
	
plotdat: plotdat.c bessel.c
main: main.c

clean: ;$(RM) report.aux report.bbl report.bcf report.blg report.log report.out report.run.xml out.txt main plotdat
