indir = ../dot

all: mcrc.dg mcrc_first_line.dg mcrc_maintenance.dg mcrc_second_line.dg mcrc_third_line.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
