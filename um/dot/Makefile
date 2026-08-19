all: pdf/staging_risk.pdf pdf/primary.pdf pdf/metastatic.pdf pdf/surveillance.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
