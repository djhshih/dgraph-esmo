indir = ../dot

all: first_line_eligible.dg first_line_ineligible.dg relapsed_refractory.dg apl_first_line.dg apl_relapsed_refractory.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
