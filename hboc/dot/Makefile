all: pdf/hboc_brca1.pdf pdf/hboc_brca2.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
