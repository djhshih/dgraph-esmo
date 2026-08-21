indir = ../dot

all: mnsclc_mol_pos.dg mnsclc_egfr.dg mnsclc_alk.dg mnsclc_ros1.dg mnsclc_braf.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
