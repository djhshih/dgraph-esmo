indir = ../dot

all: mbc.dg mbc_er_pos_her2_neg.dg mbc_her2_pos_1st_2nd_line.dg mbc_her2_pos_3rd_line.dg mtnbc.dg mbc_omd.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
