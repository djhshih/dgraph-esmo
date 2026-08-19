all: pdf/early_intermediate.pdf pdf/advanced.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
