SCRIPT = ../../download_image.py

all: locoregional-staging.jpg resectable.jpg systemic-treatment.jpg

locoregional-staging.jpg:
	python $(SCRIPT) https://www.annalsofoncology.org/cms/10.1016/j.annonc.2025.08.003/asset/df103be2-956c-44df-bc05-9283b033b1f3/main.assets/gr1_lrg.jpg $@

resectable.jpg:
	python $(SCRIPT) https://www.annalsofoncology.org/cms/10.1016/j.annonc.2025.08.003/asset/9b1241bd-214a-424e-aaed-a0718981b88c/main.assets/gr2_lrg.jpg $@

systemic-treatment.jpg:
	python $(SCRIPT) https://www.annalsofoncology.org/cms/10.1016/j.annonc.2025.08.003/asset/936a4344-b6b8-45d2-9b17-91af934c6eaf/main.assets/gr3_lrg.jpg $@
