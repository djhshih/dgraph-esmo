all: pdf/diagnosis.pdf pdf/locoregional.pdf pdf/advanced_ccrcc.pdf pdf/advanced_prcc.pdf pdf/advanced_ncc.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
