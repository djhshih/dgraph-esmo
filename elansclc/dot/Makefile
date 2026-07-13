all: pdf/locoregional_staging.pdf pdf/resectable.pdf pdf/systemic_treatment.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf

