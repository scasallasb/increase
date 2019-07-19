ARCH=colcom

${ARCH}.pdf: ${ARCH}.tex bibliografia.bib
	pdflatex ${ARCH}.tex
	bibtex   ${ARCH}.aux
	pdflatex ${ARCH}.tex

ver:
	evince ${ARCH}.pdf

clean:
	rm -f *.aux *.log ${ARCH}.pdf *.bbl *.blg 

