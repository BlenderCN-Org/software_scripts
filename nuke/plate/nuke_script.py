import nuke
import os
import re
import shutil
import time, datetime
import modules.mail_notification as mail



def render_plates(folder_list, cur_folder):
	
	for folder in folder_list:

		#Go to next line in txt file if line contains a # (comment).
		if "#" in folder:
			continue
		
		custom_text = ""
		if "*" in folder:
			custom_text = folder.split("*")[1]
			folder = folder.split("*")[0]

		#Return all folder files.
		files_list = [f for f in os.listdir(folder) if f.endswith('.jpg') or f.endswith('.png') or f.endswith('.exr') or f.endswith('.tga') or f.endswith('.tif')]

		#Retrieve the number of frames.
		nbr_frame = len(os.listdir(folder))

		#Get the name of the first and last frame (in order to retrieve frame range).
		file_name_first = files_list[0]
		file_name_last = files_list[-1]

		a = re.compile("([a-z]*_)*[0-9]{6}_[a-z]{2}\.")

		if a.match(file_name_first):

			file_description = re.search('([a-zA-Z]*_)*', file_name_first).group(0)
			file_description = file_description[:-1]
			file_date = re.search('_[0-9]{6}_', file_name_first).group(0).replace("_", "")
			file_creator = re.search('_[a-z]{2}\.', file_name_first).group(0).replace("_", "").replace(".", "")

			if file_creator == "th":
				file_creator = "Thibault Houdon"
			elif file_creator == "mr":
				file_creator = "Maxime Roz"
			elif file_creator == "cg":
				file_creator = "Christopher Gonnord"

			file_date = time.strptime(file_date, "%y%m%d")
			file_date = time.strftime('%B %d, %Y', file_date)

			#Get the padding of the first frame.
			padding = re.search("\.[0-9]{4}\.", file_name_first)
			padding = padding.group(0).replace(".", "")

			#Get the padding of the last frame.
			padding_last = re.search("\.[0-9]{4}\.", file_name_last)
			padding_last = padding_last.group(0).replace(".", "")
		
			#Convert the file_name from #### padding to %04d padding.
			file_name_first = file_name_first.replace(padding, "%0" + str(len(padding)) + "d")
			file_extension = os.path.splitext(file_name_first)[1]
			file_name_write = file_name_first.replace(file_extension, ".jpg")

			folder = folder.replace("\\", "/")

			########## NUKE #########

			nuke_script = [f for f in os.listdir(cur_folder) if f.endswith('.nk')][0]

			nuke.scriptOpen(cur_folder + "\\plate.nk")

			#Retrieve Read and Write nodes.
			read_node = nuke.toNode("Read")
			write_node = nuke.toNode("Write")
			burntext_node = nuke.toNode("BurnText")

			#Change frame range.
			read_node.knob("first").setValue(int(padding))
			read_node.knob("last").setValue(int(padding_last))


			#Replace the read and write nodes paths.
			read_node.knob("file").setValue(folder + "/" + file_name_first)
			write_node.knob("file").setValue(folder + "/plate/" + file_name_write)

			#Change text on the plate.
			if len(custom_text) > 0:
				burntext_node.knob("Topright").setValue(custom_text)
			else:
				burntext_node.knob("Topright").setValue("")

			burntext_node.knob("Bottomcenter").setValue("Walden")
			burntext_node.knob("Bottomleft").setValue(file_creator)
			burntext_node.knob("Bottomright").setValue(file_date)

			#Creates a plate folder to write files to.
			os.makedirs(folder + "\\plate")

			nuke.scriptSave(cur_folder + "\\" + file_description + ".nk")

			nuke.scriptExit()

			nuke.scriptOpen(cur_folder + "\\" + file_description + ".nk")

			#Render all frames.
			nuke.execute("Write",int(padding),int(padding_last),1)

			#Exit Nuke.
			nuke.scriptExit()

			os.remove(cur_folder + "\\" + file_description + ".nk")

			mail.send_email(subject="Plates finished", message=folder, to_addr_list="t")

cur_folder = os.path.dirname(os.path.abspath(__file__))

with open(cur_folder + "\\plate_list.txt") as f:
    folder_list = f.read().splitlines()

render_plates(folder_list,cur_folder)