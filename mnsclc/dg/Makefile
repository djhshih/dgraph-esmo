
indir = ../dot

all: mnsclc_alk.dg mnsclc_braf.dg mnsclc-egfr.dg mnsclc_ros1.dg
	

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg

