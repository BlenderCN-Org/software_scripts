#  ___    ___    ___  ___ ___  ____    __ __  ___  __   __
# (   )  (   )  / _ \(_  v  _)(   _)  (_ v _)/ _ \(  | |  )
#  | |    | |__( (_) ) \   /   | E_     \ / ( (_) )| |_| |
# (___)  (_____)\___/   \_/   (____)   (___) \___/ (_____)

						# THIBAULT
 
 

#SCRIPT BY THE ONE AND ONLY RODRIGUOOOOOOOOOOOOOOOOOOOOOOOO





import mari, os, hashlib
import PythonQt.QtGui as gui
import PythonQt.QtCore as core


def export_manager():

	#-----------------------------FONCTIONS NECESSAIRES----------------------------

	#Fonction pour bouton Select all --- All Checkbox == 1
	def select_all():
		for key, value in checkbox_dict.items():
			key.setChecked(1) #1 = Checked


	#Fonction pour bouton Select none --- All Checkbox == 0
	def select_none():
		for key, value in checkbox_dict.items():
			key.setChecked(0) #0 = Not Checked

	#Export All maps peu importe les Checkbox
	def export_all_fc(): 
		print "EXPORTING THESE MAPS(ALL)"
		for obj in geo_list:
			mari.geo.setCurrent(obj)
			channelList = obj.channelList()
			for chan in channelList:
				print chan
				chan.exportImagesFlattened(path_export + nomenclature)

	#Export SELECTED maps selon les Checkbox
	def export_selected_fc():
		print "EXPORTING THESE MAPS(SELECTED)"
		for key in checkbox_dict.keys():
			if key.checkState() == 2:
				chan =  checkbox_dict[key]
				print chan
				chan.exportImagesFlattened(path_export + nomenclature)
				# object = "Cube"
				# channel = "Diffuse"
				# geo_dict = {"Cube":objet cube}




	#-----------------------------UI & SHITS---------------------------------------			

	#Variables necessaires
	dlg = gui.QDialog()
	geo_list = mari.geo.list()
	path_export = "H:\\tmp\\"
	nomenclature = "nat_feu_0010_$CHANNEL_$ENTITY_$UDIM.png"

	#Construire la fenetre et le layout de base
	main_layout = gui.QHBoxLayout()
	close_layout = gui.QVBoxLayout()


	#Layout pour section du top
	top_group = gui.QGroupBox()
	top_group_layout = gui.QVBoxLayout()
	top_group.setLayout(top_group_layout)

	#Layout pour section du bot
	bottom_group = gui.QGroupBox()
	bottom_group_layout = gui.QVBoxLayout()	
	bottom_group.setLayout(bottom_group_layout)


	#Ajouter Group Widget au main Layout
	main_layout.addWidget(top_group)
	main_layout.addWidget(bottom_group)



	#Channel Header, Label et Widgets
	channel_label = gui.QLabel("<strong>Channels To Export</strong>")
	channel_layout = gui.QVBoxLayout()
	channel_header_layout = gui.QHBoxLayout()
	
	#Layout Channel
	channel_header_layout.addWidget(channel_label)
	channel_header_layout.addStretch()
	channel_layout.addLayout(channel_header_layout)

	top_group_layout.addLayout(channel_layout)

	#-----------------------------BUTTON & WIDGETS---------------------------------

	#Repopulate the earth
	chan_dict = {}
	checkbox_dict = {}
	checkbox_liste = []

	checkbox_group = gui.QGroupBox()
	checkbox_group_layout = gui.QVBoxLayout()
	checkbox_group.setLayout(checkbox_group_layout)
	top_group_layout.addWidget(checkbox_group)

	#Label & Checkbox builder
	geo_dict = {}
	for geo in geo_list: # Iterating over each object (geo = Cube, Sphere, Torus)

		obj_label = gui.QLabel(str(geo.name()))
		checkbox_group_layout.addWidget(obj_label)

		for channel in geo.channelList(): # Iterating over each channel (channel = Diffuse, Spec, Bump...)
			checkbox = gui.QCheckBox(str(channel.name()))
			checkbox_group_layout.addWidget(checkbox)
			checkbox_dict[checkbox] = channel


	#Path Layout
	path_layout = gui.QHBoxLayout()

    #Ajouter un label, bouton et text field pour le path
	path_label = gui.QLabel('Path:')	#Label avant le lineEdit
    path_line_edit = gui.QLineEdit(path_export)	#Texte sur la ligne
	path_line_edit.setReadOnly(1)	#Read Only mode, can select can't change
    path_pixmap = gui.QPixmap(mari.resources.path(mari.resources.ICONS) + '/ExportImages.png')
    icon = gui.QIcon(path_pixmap)
    path_button = gui.QPushButton(icon, "")


    path_layout.addWidget(path_label)
    path_layout.addWidget(path_line_edit)
    path_layout.addWidget(path_button)


    bottom_group_layout.addLayout(path_layout)



    #Select All & Select None Button
	sel_all = gui.QPushButton("Select All")
	sel_none = gui.QPushButton("Select None")
	top_group_layout.addWidget(sel_all)
	top_group_layout.addWidget(sel_none)

	sel_all.connect("clicked()", select_all)	#Connect button to fonction
	sel_none.connect("clicked()", select_none)	#Connect button to fonction


    #Export All & Export Button
    export_all = gui.QPushButton("Export All")
    export_selected = gui.QPushButton("Export Selected")
    bottom_group_layout.addWidget(export_all)
    bottom_group_layout.addWidget(export_selected)
	
	export_all.connect("clicked()", export_all_fc)	#Connect button to fonction
	export_selected.connect("clicked()", export_selected_fc)	#Connect button to fonction

    #Close button
    close_btn = gui.QPushButton("Close")
    close_layout.addWidget(close_btn)
    main_layout.addLayout(close_layout, stretch = 1)

    close_btn.connect("clicked()", dlg.reject)	#Connect button to fonction

	dlg.setLayout(main_layout)
	dlg.setWindowTitle("Export Manager")





	dlg.exec_()







export_manager()

