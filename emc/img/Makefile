SCRIPT = ../../download_image.py

all: molecular_classification.jpg stage_1_surgery.jpg adjuvant_low_intermediate.jpg adjuvant_intermediate_high.jpg locoregional_recurrence.jpg metastatic.jpg

molecular_classification.jpg:
	python $(SCRIPT) https://www.annalsofoncology.org/cms/10.1016/j.annonc.2022.05.009/asset/c9f1ab0d-8be1-4c90-b30e-6dd98228b805/main.assets/gr1_lrg.jpg $@

stage_1_surgery.jpg:
	python $(SCRIPT) https://www.annalsofoncology.org/cms/10.1016/j.annonc.2022.05.009/asset/7b07a633-13dd-4e2d-9301-669c13bef3d0/main.assets/gr2_lrg.jpg $@

adjuvant_low_intermediate.jpg:
	python $(SCRIPT) https://www.annalsofoncology.org/cms/10.1016/j.annonc.2022.05.009/asset/98ead302-d665-43dd-8871-dd5f880f5dff/main.assets/gr3_lrg.jpg $@

adjuvant_intermediate_high.jpg:
	python $(SCRIPT) https://www.annalsofoncology.org/cms/10.1016/j.annonc.2022.05.009/asset/8eeee165-c01a-49e6-b936-9d6aff100878/main.assets/gr4_lrg.jpg $@

locoregional_recurrence.jpg:
	python $(SCRIPT) https://www.annalsofoncology.org/cms/10.1016/j.annonc.2022.05.009/asset/1ddba525-cffc-449e-a8bf-cf9cffa13636/main.assets/gr5_lrg.jpg $@

metastatic.jpg:
	python $(SCRIPT) https://www.annalsofoncology.org/cms/10.1016/j.annonc.2022.05.009/asset/02c197fd-ec9a-420f-bffd-5b9243bbf4cb/main.assets/gr6_lrg.jpg $@
