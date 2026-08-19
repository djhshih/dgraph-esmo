all: pdf/pan_net_surgical.pdf pdf/si_net_surgical.pdf pdf/carcinoid_syndrome.pdf pdf/systemic_therapy.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
