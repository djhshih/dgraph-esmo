all: pdf/cup_vs__ve_nsclc.pdf pdf/cup_vs_+ve_nsclc.pdf pdf/cup_vs_cca.pdf pdf/cup_vs_ovarian.pdf pdf/cup_vs_rcc.pdf pdf/cup_vs_sgc.pdf pdf/cup_vs_breast.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
