all: pdf/nodal_first_line.pdf pdf/extranodal_first_line.pdf pdf/leukaemic_first_line.pdf pdf/nodal_rr.pdf pdf/extranodal_rr.pdf pdf/leukaemic_rr.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
