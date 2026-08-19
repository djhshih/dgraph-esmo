indir = ../dot

all: thyroid_dtc.dg thyroid_tt.dg thyroid_postop.dg thyroid_advanced.dg thyroid_atc.dg thyroid_mtc.dg thyroid_mtc_postop.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
