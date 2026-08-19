indir = ../dot

all: hiv_dlbcl.dg hiv_bl_first_line.dg hiv_pbl_first_line.dg hiv_pbl_rr.dg hiv_pel_first_line.dg hiv_pel_rr.dg hiv_pcnsl_first_line.dg hiv_hl.dg hhv8_mcd_first_line.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
