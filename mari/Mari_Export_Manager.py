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
		for i in checkbox_liste:
			i.setChecked(1)

	#Fonction pour bouton Select none --- All Checkbox == 0
	def select_none():
		for i in checkbox_liste:
			i.setChecked(0)

	#Export All maps peu importe les Checkbox
	def export_all_fc(): 
		print "EXPORTING THESE MAPS"
		for obj in geo_list:
			mari.geo.setCurrent(obj)
			channelList = obj.channelList()
			for chan in channelList:
				# chan.exportImagesFlattened("C:\\Users\\Rodrigue\\Desktop\\Script\\Mari\\Test\\nat_feu_0010_$CHANNEL_$ENTITY_$UDIM.png")
				print chan	

	#Export SELECTED maps selon les Checkbox
	def export_selected_fc():
		print checkbox_dict



	#-----------------------------UI & SHITS---------------------------------------			

	#Variables necessaires
	dlg = gui.QDialog()
	geo_list = mari.geo.list()

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

	#Query
	for geo in geo_list:
		ma_liste = []
		for channel in geo.channelList():
			ma_liste.append(channel.name())
		chan_dict[str(geo.name())] = ma_liste

	#Widget Building
	for i in geo_list:
		obj_label = gui.QLabel(str(i.name()))
		checkbox_group_layout.addWidget(obj_label)
		
		channels = chan_dict[str(i.name())]

		for chan in channels:
			checkbox_chan = gui.QCheckBox(str(chan))
			checkbox_dict[chan] = str(checkbox_chan)
			checkbox_group_layout.addWidget(checkbox_chan)
			checkbox_liste.append(checkbox_chan)
			print checkbox_dict


	
	#Path Layout
	path_layout = gui.QHBoxLayout()

    #Get mari default path and template
    path = os.path.abspath(mari.resources.path(mari.resources.DEFAULT_EXPORT))
    template = mari.resources.sequenceTemplate()
    export_path_template = os.path.join(path, template)

    #Ajouter un label, bouton et text field pour le path
    path_label = gui.QLabel('Path:')
    path_line_edit = gui.QLineEdit()
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

	sel_all.connect("clicked()", select_all)
	sel_none.connect("clicked()", select_none)


    #Export All & Export Button
    export_all = gui.QPushButton("Export All")
    export_selected = gui.QPushButton("Export Selected")
    bottom_group_layout.addWidget(export_all)
    bottom_group_layout.addWidget(export_selected)
	
	export_all.connect("clicked()", export_all_fc)
	export_selected.connect("clicked()", export_all_fc)

    #Close button
    close_btn = gui.QPushButton("Close")
    close_layout.addWidget(close_btn)
    main_layout.addLayout(close_layout, stretch = 1)
    close_btn.connect("clicked()", dlg.reject)

	dlg.setLayout(main_layout)
	dlg.setWindowTitle("Export Manager")





	dlg.exec_()







export_manager()

