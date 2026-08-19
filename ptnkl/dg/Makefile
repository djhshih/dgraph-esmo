indir = ../dot

all: nodal_first_line.dg extranodal_first_line.dg leukaemic_first_line.dg nodal_rr.dg extranodal_rr.dg leukaemic_rr.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
