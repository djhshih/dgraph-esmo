

all: pdf/mnsclc-egfr.pdf pdf/mnsclc-alk.pdf pdf/mnsclc-ros1.pdf pdf/mnsclc-braf.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf

