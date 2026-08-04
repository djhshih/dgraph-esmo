
indir = ../dot

all: nsqnscc_ici.dg nsqnscc_no_ici.dg sqcc_ici.dg sqcc_no_ici.dg
	
%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg

 