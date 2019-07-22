# colocar el prefijo de los nombres
doc=estadoArte


## --bibliography=bibliografia.bib 

OPT= --variable=papersize:letter --variable=geometry:"margin=2cm" --variable=fontsize:12pt --variable=fontfamily=utopia --variable=documentclass=article  --number-sections --toc

BIB = --filter pandoc-citeproc --bibliography=refer.bib -S

#--variabla=lof --variable=lot 

${doc}.pdf: ${doc}.md refer.bib 
	@echo "Haciendo documento $@"
	#@gpp -T $< | pandoc ${OPT} -f markdown -t latex  -o $@
	pandoc ${OPT}  ${BIB} -f markdown -t latex $< -o $@

${doc}.doc: ${doc}.md
	@echo "Haciendo word $@"
	@gpp -T $< | pandoc ${OPT} -f markdown  -o $@
	#pandoc ${OPT} -f markdown $< -o $@

clean:
	rm ${doc}.pdf ${doc}.doc
