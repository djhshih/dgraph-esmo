all: pdf/mf_ss.pdf pdf/cd30_lpd.pdf pdf/pcmzl_pcfcl.pdf pdf/pclbcl_lt.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
