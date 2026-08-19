indir = ../dot

all: oral_cavity.dg larynx.dg oropharynx.dg hypopharynx.dg recurrent_metastatic.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
