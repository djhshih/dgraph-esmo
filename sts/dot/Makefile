all: pdf/sts_locoregional_resectable.pdf pdf/sts_locoregional_unresectable.pdf pdf/sts_advanced_resectable.pdf pdf/sts_advanced_unresectable.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
