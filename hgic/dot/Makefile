all: pdf/lynch_syndrome.pdf pdf/gastric_cancer.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
