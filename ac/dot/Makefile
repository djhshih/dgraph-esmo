all: pdf/diagnosis.pdf pdf/localised.pdf pdf/advanced.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
