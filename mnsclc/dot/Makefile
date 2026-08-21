all: pdf/mnsclc_mol_pos.pdf pdf/mnsclc_egfr.pdf pdf/mnsclc_alk.pdf pdf/mnsclc_ros1.pdf pdf/mnsclc_braf.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
