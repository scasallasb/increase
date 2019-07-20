# colocar el prefijo de los nombres
doc=estadoArte

.PHONY: clean gnuplot 


todo: ${doc}.pdf ${doc}.doc 

#  fontfamily: utopia, lmodern, times, bookman
OPT= --variable=papersize:letter \
     --variable=geometry:"margin=2cm" \
     --variable=fontsize:12pt\
     --variable=fontfamily:utopia\
     --variable=documentclass:article\
     --number-sections
#     --filter pandoc-eqnos\
#     --filter pandoc-citeproc 
#     --bibliography=bibliografia.bib\
#--filter pandoc-include-code


${doc}.pdf: ${doc}.md bibliografia.bib ${gnuplots}
	@echo "Haciendo documento $@" 
	pandoc ${OPT} -f markdown -t latex  -o $@ $<


${doc}.doc: ${doc}.md
	@echo "Haciendo word $@"
	pandoc ${OPT} -f markdown  -o $@ $<

clean:
	rm ${doc}.pdf ${doc}.doc
