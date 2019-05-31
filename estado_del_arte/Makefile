comparacion.pdf: comparacion.md dependencias.pdf
	pandoc -f markdown comparacion.md -o comparacion.pdf

dependencias.pdf: dependencias.svg
	inkscape -D -A dependencias.pdf dependencias.svg

estadoArte.pdf: estadoArte.md dependencias.pdf
	pandoc -f markdown estadoArte.md -o estadoArte.pdf
