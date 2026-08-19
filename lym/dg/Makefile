indir = ../dot

all: dlbcl_stage_i_ii.dg dlbcl_stage_iii_iv.dg dlbcl_rr.dg pcnsl.dg fl_first_line.dg fl_rr.dg mcl_first_line.dg mcl_rr.dg emzl_stage_i_iie.dg smzl_nmzl.dg mzl_stage_iv.dg chl_stage_i_ii.dg chl_advanced.dg chl_rr.dg ptcl.dg ptcl_rr.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
