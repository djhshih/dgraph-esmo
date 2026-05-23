

all: pdf/ebc-dx.pdf pdf/ebc.pdf pdf/ebc-aln.pdf pdf/ebc-her2-pos.pdf pdf/ebc-hr-pos.pdf pdf/ebc-tnbc.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf

