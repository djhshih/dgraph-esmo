

all: pdf/locoregional.pdf pdf/recurrent_metastatic.pdf pdf/follow_up.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf

