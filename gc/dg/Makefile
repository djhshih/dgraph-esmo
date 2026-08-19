indir = ../dot

all: gc.dg gc_first_line.dg gc_maintenance.dg gc_second_line.dg gc_third_line.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
