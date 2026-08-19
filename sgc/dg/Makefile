indir = ../dot

all: sgc.dg parotid.dg sublingual.dg submandibular.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
