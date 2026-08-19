all: pdf/front_line.pdf pdf/second_line.pdf pdf/third_line.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
