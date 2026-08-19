indir = ../dot

all: front_line.dg second_line.dg third_line.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
