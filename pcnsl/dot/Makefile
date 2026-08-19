all: pdf/diagnosis.pdf pdf/first_line.pdf pdf/pvrl.pdf pdf/rr.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
