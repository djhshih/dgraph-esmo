all: pdf/thyroid_dtc.pdf pdf/thyroid_tt.pdf pdf/thyroid_postop.pdf pdf/thyroid_advanced.pdf pdf/thyroid_atc.pdf pdf/thyroid_mtc.pdf pdf/thyroid_mtc_postop.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
