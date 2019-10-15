# colocar el prefijo de los nombres
doc=estadoArte

## --bibliography=bibliografia.bib 

OPT= --variable=papersize:letter --variable=geometry:"margin=3cm " --variable=fontsize:12pt --variable=fontfamily=utopia --variable=documentclass=article  --number-sections --toc --top-level-division=[part]

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



clean:
	rm ${doc}.pdf ${doc}.doc
