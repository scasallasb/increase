
increasetool.pdf increasetool.html:

%.pdf: %.md
	pandoc -f markdown -t latex $< -o $@

%.html: %.md
	pandoc -f markdown -t html $< -o $@

clean:
	rm -f increasetool.pdf increasetool.html
