all: pdf/resectable.pdf pdf/unresectable.pdf pdf/metastatic.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
