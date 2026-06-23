SCRIPT = ../../download_image.py

all: diagnosis-staging.jpg localised-treatment.jpg very-high-risk-cn1.jpg biochemical-recurrence.jpg

diagnosis-staging.jpg:
	python $(SCRIPT) https://www.annalsofoncology.org/cms/10.1016/j.annonc.2025.12.009/asset/b5d60ebf-d6f6-4d4b-9dea-f90b9837b4a4/main.assets/gr1_lrg.jpg $@

localised-treatment.jpg:
	python $(SCRIPT) https://www.annalsofoncology.org/cms/10.1016/j.annonc.2025.12.009/asset/5e5a4170-f160-40c5-a218-20fe00bf051b/main.assets/gr2_lrg.jpg $@

very-high-risk-cn1.jpg:
	python $(SCRIPT) https://www.annalsofoncology.org/cms/10.1016/j.annonc.2025.12.009/asset/9d69588a-20ab-41ef-ab42-16266ea96e29/main.assets/gr3_lrg.jpg $@

biochemical-recurrence.jpg:
	python $(SCRIPT) https://www.annalsofoncology.org/cms/10.1016/j.annonc.2025.12.009/asset/791a5ab3-e4df-4bdc-9a48-e8c7225d28a1/main.assets/gr4_lrg.jpg $@
