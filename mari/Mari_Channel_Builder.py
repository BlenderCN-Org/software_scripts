#coding=utf-8

import mari, os, hashlib
import PythonQt.QtGui as gui
import PythonQt.QtCore as core
import sys


class MariExporter(gui.QDialog):
	def __init__(self):
		super(MariExporter, self).__init__()


		self.setWindowTitle("Channel Builder")
		main_layout = gui.QHBoxLayout(self)

		# Map Checkbox Layout
		left_group = gui.QGroupBox(self)
		self.channel_layout = gui.QGridLayout()
		left_group.setLayout(self.channel_layout)
		self.lbl = gui.QLabel("<b>Channels To Build</b>")
		self.channel_layout.addWidget(self.lbl)
		self.channel_layout.setColumnMinimumWidth(1, 5)

		# Middle Layout
		self.mid_group = gui.QGroupBox(self)
		self.mid_group_layout = gui.QVBoxLayout(self)
		self.mid_group.setLayout(self.mid_group_layout)

		# Close Layout
		self.right_group = gui.QGroupBox(self)
		self.right_group_layout = gui.QVBoxLayout(self)
		self.right_group.setLayout(self.right_group_layout)

		# Add Layout to main
		main_layout.addWidget(left_group)
		main_layout.addWidget(self.mid_group)
		main_layout.addWidget(self.right_group)

		self.channel_builder()
		self.bouton_ui()


	def channel_builder(self):


		#-----------------------------Boring stuff (AKA VARIABLES ET FONCTIONS)-----------------

		self.geo_list = mari.geo.list()
		self.sel_obj = mari.geo.current()
		self.chk_dict = {}
		self.chk_liste = []
		diff_chk = gui.QCheckBox("Diffuse", self)
		bump_chk = gui.QCheckBox("Bump", self)
		disp_chk = gui.QCheckBox("Displacement", self)
		spec_chk = gui.QCheckBox("Specular", self)
		norm_chk = gui.QCheckBox("Normal", self)
		roug_chk = gui.QCheckBox("Roughness", self)
		refl_chk = gui.QCheckBox("Reflection", self)
		refr_chk = gui.QCheckBox("Refraction", self)
		fres_chk = gui.QCheckBox("Fresnel", self)
		mask_chk = gui.QCheckBox("Mask", self)
		self.chk_liste = [diff_chk, bump_chk, disp_chk, spec_chk, norm_chk, roug_chk, refl_chk, refr_chk, fres_chk, mask_chk]
		self.chk_liste_name = ["diff_chk", "bump_chk", "disp_chk", "spec_chk", "norm_chk", "roug_chk", "refl_chk", "refr_chk", "fres_chk", "mask_chk"]

	def bouton_ui(self):
		# Add Checkbox pour Map et Set to layout
		self.add_chk()

		# Select All & Select None
		sel_all = gui.QPushButton("Select All")
		sel_none = gui.QPushButton("Select None")
		self.channel_layout.addWidget(sel_all)
		self.channel_layout.addWidget(sel_none)

		sel_all.connect("clicked()", self.select_all)
		sel_none.connect("clicked()", self.select_none)

		# Close button
		close_btn = gui.QPushButton("Close")
		self.right_group_layout.addWidget(close_btn)
		close_btn.connect("clicked()", self.reject)
		print self.chk_dict

		#Build All
		build_all = gui.QPushButton("Build All")	#Bouton Build All
		self.build_all_same_size_chkbox = gui.QCheckBox("Use same size for all maps?")
		self.build_all_size_combobox = gui.QComboBox()
		self.build_all_groupbox = gui.QGroupBox(self)	#Création du cadre
		self.build_all_layout = gui.QGridLayout(self)	#Layout du cadre
		self.build_all_groupbox.setLayout(self.build_all_layout)	#Attribuer le layout au cadre

		self.build_all_layout.addWidget(build_all)	#Ajouter le bouton au layout

		self.build_all_layout.addWidget(self.build_all_same_size_chkbox)	#Ajouter le checkbox au layout

		self.build_all_layout.addWidget(self.build_all_size_combobox)	#Ajouter la combobox au layout
		self.build_all_size_combobox.insertItem(0, "1024", )	#Ajouter resolution 1024
		self.build_all_size_combobox.insertItem(1, "2048", )	#Ajouter resolution 2048
		self.build_all_size_combobox.insertItem(2, "4096", )	#Ajouter resolution 4096
		self.build_all_size_combobox.insertItem(3, "8192", )	#Ajouter resolution 8192

		self.mid_group_layout.addWidget(self.build_all_groupbox)	#Ajouter le cadre au Layout du milieu

		if self.build_all_same_size_chkbox.isChecked() == 1:
			self.build_all_size_combobox.setEnabled(0)
		else:
			self.build_all_size_combobox.setEnabled(1)

		# build_all.connect("clicked()", self.)

		#Build Selected
		build_selected = gui.QPushButton("Build Selected")
		self.mid_group_layout.addWidget(build_selected)

	def add_chk(self):
		'''Fonction pour créer les checkbox et les assigner'''
		temp = 0
		for checkbox in self.chk_liste:
			self.size_for_map = gui.QComboBox()
			self.size_for_map.insertItem(0, "1024", )
			self.size_for_map.insertItem(1, "2048", )
			self.size_for_map.insertItem(2, "4096", )
			self.size_for_map.insertItem(3, "8192", )
			# self.size_for_map.insertItem(4, "16384", )    #PEUT-ETRE DISPONIBLE UN JOUR QUI SAIT ;_;
			self.channel_layout.addWidget(self.chk_liste[temp])
			self.channel_layout.addWidget(self.size_for_map)
			temp_name = self.chk_liste_name[temp]
			temp = temp + 1
			self.chk_dict[temp_name] = self.size_for_map

	def select_all(self):
		'''Fonction pour selectionner tout'''
		for checkbox in self.chk_liste:
			checkbox.setChecked(1)

	def select_none(self):
		'''Fonction pour déselectionner tout'''
		for checkbox in self.chk_liste:
			checkbox.setChecked(0)

	def check_state(self):
		'''Fonction pour barrer les maps combobox'''

	# def build_all_fc(self):
	# 	self.sel_obj.createChannel()






MainWindow = MariExporter()
MainWindow.show()




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
