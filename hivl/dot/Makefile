all: pdf/hiv_dlbcl.pdf pdf/hiv_bl_first_line.pdf pdf/hiv_pbl_first_line.pdf pdf/hiv_pbl_rr.pdf pdf/hiv_pel_first_line.pdf pdf/hiv_pel_rr.pdf pdf/hiv_pcnsl_first_line.pdf pdf/hiv_hl.pdf pdf/hhv8_mcd_first_line.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
