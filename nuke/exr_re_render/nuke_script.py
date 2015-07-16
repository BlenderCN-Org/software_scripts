import nuke
import os
import re
import shutil
import time
import modules.mail_notification as mail

def re_render_exr(folder_list, cur_folder):
	
	for folder in folder_list:

		#Go to next line in txt file if line contains a # (comment).
		if "#" in folder:
			continue
		
		#Return all folder files.
		files_list = os.listdir(folder)

		#Retrieve the number of frames.
		nbr_frame = len(os.listdir(folder))

		#Get the name of the first and last frame (in order to retrieve frame range).
		file_name_first = os.listdir(folder)[0]
		file_name_last = os.listdir(folder)[-1]

		#Get the padding of the first frame.
		padding = re.search("[0-9]{4}", file_name_first)
		padding = padding.group(0)

		#Get the padding of the last frame.
		padding_last = re.search("[0-9]{4}", file_name_last)
		padding_last = padding_last.group(0)
	
		#Convert the file_name from #### padding to %04d padding.
		file_name_first = file_name_first.replace(padding, "%0" + str(len(padding)) + "d")


		folder = folder.replace("\\", "/")

		nuke.scriptOpen(cur_folder + "\\exr_re_render.nk")

		#Retrieve Read and Write nodes.
		read_node = nuke.toNode("Read")
		write_node = nuke.toNode("Write")		

		#Change frame range.
		read_node.knob("first").setValue(int(padding))
		read_node.knob("last").setValue(int(padding_last))

		#Replace the read and write nodes paths.
		read_node.knob("file").setValue(folder + "/" + file_name_first)
		write_node.knob("file").setValue(folder + "/tmp/" + file_name_first)

		#Creates a tmp folder to write files to.
		os.makedirs(folder + "\\tmp")

		#Render all frames.
		nuke.execute ("Write",0,nbr_frame,1)

		#Exit Nuke.
		nuke.scriptExit()

		#Move all files from tmp to original folder.
		for i in files_list:
			os.remove(folder + "/" + i)

		for i in os.listdir(folder + "/tmp"):
			shutil.move(folder + "/tmp/" + i, folder)

		#Remove tmp folder.
		shutil.rmtree(folder + "/tmp", ignore_errors=True)

		mail.send_email(to_addr_list='t', message=folder)
		

cur_folder = os.path.dirname(os.path.abspath(__file__))

with open(cur_folder + "\\exr_re_render_list.txt") as f:
	folder_list = f.read().splitlines()

re_render_exr(folder_list,cur_folder)