all: pdf/lung_adjuvant.pdf pdf/thymic_adjuvant.pdf pdf/functioning_syndrome.pdf pdf/advanced.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
