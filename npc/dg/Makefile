indir = ../dot

all: locoregional.dg recurrent_metastatic.dg follow_up.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
