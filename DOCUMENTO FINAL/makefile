# colocar el prefijo de los nombres
doc=estadoArte



## --bibliography=bibliografia.bib 

OPT= --variable=papersize:letter --variable=geometry:"margin={4cm,3cm,2cm,3cm} " --variable=fontsize:12pt --variable=fontfamily=mathptmx --variable=documentclass=article --number-sections --toc 

BIB = --filter pandoc-citeproc --bibliography=refer.bib 

#--variabla=lof --variable=lot 



${doc}.pdf: ${doc}.md refer.bib dependencias.pdf UMTS.pdf
	@echo "Haciendo documento $@"
	#@gpp -T $< | pandoc ${OPT} -f markdown -t latex  -o $@
	pandoc ${OPT}  ${BIB} -f markdown -t latex $< -o $@



dependencias.pdf: dependencias.svg
	inkscape -D -A dependencias.pdf dependencias.svg
	
	
UMTS.pdf: UMTS.svg
	inkscape -D -A UMTS.pdf UMTS.svg

metodología.pdf: metodologia.svg
	inkscape -D -A metodologia.pdf dependencias.svg


clean:
	rm ${doc}.pdf ${doc}.doc
