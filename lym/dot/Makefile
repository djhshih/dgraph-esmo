all: pdf/dlbcl_stage_i_ii.pdf pdf/dlbcl_stage_iii_iv.pdf pdf/dlbcl_rr.pdf pdf/pcnsl.pdf pdf/fl_first_line.pdf pdf/fl_rr.pdf pdf/mcl_first_line.pdf pdf/mcl_rr.pdf pdf/emzl_stage_i_iie.pdf pdf/smzl_nmzl.pdf pdf/mzl_stage_iv.pdf pdf/chl_stage_i_ii.pdf pdf/chl_advanced.pdf pdf/chl_rr.pdf pdf/ptcl.pdf pdf/ptcl_rr.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
