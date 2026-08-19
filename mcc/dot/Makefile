all: pdf/mcc_locoregional.pdf pdf/mcc_advanced.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
