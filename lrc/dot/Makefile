all: pdf/upper_third_ct1_ct3.pdf pdf/upper_third_ct4.pdf pdf/middle_lower_surgery.pdf pdf/middle_lower_organ_preservation.pdf pdf/dmmr_msih.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
