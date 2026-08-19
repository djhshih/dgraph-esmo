indir = ../dot

all: upper_third_ct1_ct3.dg upper_third_ct4.dg middle_lower_surgery.dg middle_lower_organ_preservation.dg dmmr_msih.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
