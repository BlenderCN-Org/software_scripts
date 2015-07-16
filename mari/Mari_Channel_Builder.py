import mari, os, hashlib
import PythonQt.QtGui as gui
import PythonQt.QtCore as core



def channel_builder():


	#-----------------------------Boring stuff (AKA VARIABLES ET FONCTIONS)-----------------
	dlg = gui.QDialog()
	geo_list = mari.geo.list()
	sel_obj = mari.geo.current()
	chk_header = gui.QLabel("<strong>Channels To Build</strong>")
	diff_chk = gui.QCheckBox("Diffuse")
	bump_chk = gui.QCheckBox("Bump")
	disp_chk = gui.QCheckBox("Displacement")
	spec_chk = gui.QCheckBox("Specular")
	norm_chk = gui.QCheckBox("Normal")
	rough_chk = gui.QCheckBox("Roughness")
	refl_chk = gui.QCheckBox("Reflection")
	refr_chk = gui.QCheckBox("Refraction")
	fres_chk = gui.QCheckBox("Fresnel")
	mask_chk = gui.QCheckBox("Mask")	
	# size = 
	# depth = 
	
	#Fonction pour créer les checkbox et les assigner
	def add_chk():
		left_group_layout.addWidget(chk_header)	
		left_group_layout.addWidget(diff_chk)
		left_group_layout.addWidget(bump_chk)
		left_group_layout.addWidget(disp_chk)
		left_group_layout.addWidget(spec_chk)
		left_group_layout.addWidget(norm_chk)
		left_group_layout.addWidget(rough_chk)
		left_group_layout.addWidget(refl_chk)
		left_group_layout.addWidget(refr_chk)
		left_group_layout.addWidget(fres_chk)
		left_group_layout.addWidget(mask_chk)	

	def select_all():
		diff_chk.setChecked(1)
		bump_chk.setChecked(1)
		disp_chk.setChecked(1)
		spec_chk.setChecked(1)
		norm_chk.setChecked(1)
		rough_chk.setChecked(1)
		refl_chk.setChecked(1)
		refr_chk.setChecked(1)
		fres_chk.setChecked(1)
		mask_chk.setChecked(1)

	def select_none():
		diff_chk.setChecked(0)
		bump_chk.setChecked(0)
		disp_chk.setChecked(0)
		spec_chk.setChecked(0)
		norm_chk.setChecked(0)
		rough_chk.setChecked(0)
		refl_chk.setChecked(0)
		refr_chk.setChecked(0)
		fres_chk.setChecked(0)
		mask_chk.setChecked(0)





	main_layout = gui.QHBoxLayout()

	#Map Checkbox Layout
	left_group = gui.QGroupBox()
	left_group_layout = gui.QVBoxLayout()	
	left_group.setLayout(left_group_layout)

	#Middle Layout
	mid_group = gui.QGroupBox()
	mid_group_layout = gui.QVBoxLayout()	
	mid_group.setLayout(mid_group_layout)

	#Close Layout
	right_group = gui.QGroupBox()
	right_group_layout = gui.QVBoxLayout()	
	right_group.setLayout(right_group_layout)

	#Add Layout to main
	main_layout.addWidget(left_group)
	main_layout.addWidget(mid_group)
	main_layout.addWidget(right_group)





	#Add Checkbox pour Map et Set to layout	
	add_chk()

	#Select All & Select None
	sel_all = gui.QPushButton("Select All")
	sel_none = gui.QPushButton("Select None")
	left_group_layout.addWidget(sel_all)
	left_group_layout.addWidget(sel_none)

	sel_all.connect("clicked()", select_all)
	sel_none.connect("clicked()", select_none)	



	#Close button
	close_btn = gui.QPushButton("Close")
	right_group_layout.addWidget(close_btn)
	close_btn.connect("clicked()", dlg.reject)







	dlg.setLayout(main_layout)
	dlg.setWindowTitle("Channel Builder")


	dlg.exec_()

channel_builder()

# colr	Diffuse color
# bump	Bump
# disp	Displacement
# spec	Specular
# norm	Normal
# roug	Roughness
# refl	Reflection
# refr	Refraction
# frnl	Fresnel
# mask	Alpha
