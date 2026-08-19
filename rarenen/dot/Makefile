all: pdf/ukp_locoregional.pdf pdf/gugy_locoregional.pdf pdf/hn_locoregional.pdf pdf/metastatic.pdf pdf/functioning_syndrome.pdf pdf/parathyroid_carcinoma.pdf pdf/intrathyroid_thymic.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
