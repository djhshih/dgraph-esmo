
indir = ../dot

all: extensive_stage.dg limited_stage.dg recurrent.dg
	
%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg

 