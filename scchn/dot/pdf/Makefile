all: pdf/oral_cavity.pdf pdf/larynx.pdf pdf/oropharynx.pdf pdf/hypopharynx.pdf pdf/recurrent_metastatic.pdf
pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf

