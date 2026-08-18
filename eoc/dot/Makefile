all: pdf/eoc_early.pdf pdf/eoc_advanced.pdf pdf/eoc_recurrent.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
