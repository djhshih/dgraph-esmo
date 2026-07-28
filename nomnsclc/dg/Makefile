
indir = ../dot

all: nsqnscc_ici.dg nsqnscc-no-ici.dg sqcc-ici.dg sqcc-no-ici.dg
	
%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg

 