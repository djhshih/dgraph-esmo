SCRIPT = ../../download_image.py

all: diagnostic_workup.jpg treatment_lung.jpg treatment_breast.jpg treatment_melanoma.jpg

diagnostic_workup.jpg:
	python $(SCRIPT) https://www.annalsofoncology.org/cms/10.1016/j.annonc.2021.07.016/asset/928c3298-f170-405d-a7a0-fd80544cd1f3/main.assets/gr1_lrg.jpg $@

treatment_lung.jpg:
	python $(SCRIPT) https://www.annalsofoncology.org/cms/10.1016/j.annonc.2021.07.016/asset/6b419e7d-a4ec-4120-9583-3bb9e77ae7d7/main.assets/gr2a_lrg.jpg $@

treatment_breast.jpg:
	python $(SCRIPT) https://www.annalsofoncology.org/cms/10.1016/j.annonc.2021.07.016/asset/8c886d48-f1e7-4f16-8918-4805ca8d6ba7/main.assets/gr2b_lrg.jpg $@

treatment_melanoma.jpg:
	python $(SCRIPT) https://www.annalsofoncology.org/cms/10.1016/j.annonc.2021.07.016/asset/238f77f7-c111-4482-9a33-856bf3a4c139/main.assets/gr2c_lrg.jpg $@
