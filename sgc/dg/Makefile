
indir = ../dot

all: parotid.dg sgc.dg sublingual.dg submandibular.dg
	

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg

