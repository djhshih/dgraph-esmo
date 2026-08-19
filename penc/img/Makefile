SCRIPT = ../../download_image.py

all: diagnosis.jpg primary_tumour.jpg inguinal_ln.jpg

diagnosis.jpg:
	python $(SCRIPT) https://www.esmoopen.com/cms/10.1016/j.esmoop.2024.103481/asset/7a2f333e-be7f-4bbd-97bd-68dc927f0a4b/main.assets/gr1_lrg.jpg $@

primary_tumour.jpg:
	python $(SCRIPT) https://www.esmoopen.com/cms/10.1016/j.esmoop.2024.103481/asset/97e5cf7a-0233-4ae4-8108-c33fb3515d60/main.assets/gr2_lrg.jpg $@

inguinal_ln.jpg:
	python $(SCRIPT) https://www.esmoopen.com/cms/10.1016/j.esmoop.2024.103481/asset/f3532c4e-a139-4a04-826b-2fd9b4eff3d7/main.assets/gr3_lrg.jpg $@
