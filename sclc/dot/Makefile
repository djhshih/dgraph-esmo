

all: pdf/extensive_stage.pdf pdf/limited_stage.pdf pdf/recurrent.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf

