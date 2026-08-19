all: pdf/seminoma.pdf pdf/non_seminoma.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
