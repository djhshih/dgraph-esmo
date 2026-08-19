all: pdf/limited_stage.pdf pdf/extensive_stage.pdf pdf/recurrent.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
