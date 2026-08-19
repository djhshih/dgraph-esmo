indir = ../dot

all: diagnosis.dg adjuvant_stage_iii.dg adjuvant_stage_ii.dg follow_up.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
