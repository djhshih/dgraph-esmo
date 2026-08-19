all: pdf/mbc.pdf pdf/mbc_er_pos_her2_neg.pdf pdf/mbc_her2_pos_1st_2nd_line.pdf pdf/mbc_her2_pos_3rd_line.pdf pdf/mtnbc.pdf pdf/mbc_omd.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
