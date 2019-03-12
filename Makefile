
increasetool.pdf:

%.pdf: %.md
	pandoc -f markdown -t latex $< -o $@
