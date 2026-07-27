
indir = ../dot

# excluded treatment-intent.dg because the decisions associated with branching are not clear
all: staging.dg inoperable.dg multimodality.dg 
	

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg

 