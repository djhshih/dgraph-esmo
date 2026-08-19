indir = ../dot

all: limited_stage.dg extensive_stage.dg recurrent.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
