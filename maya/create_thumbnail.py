import os
import maya.cmds as mc
from thibh import screenshot

def create():

	file_name = mc.file(query=True, sn=True, shn=True)
	if file_name:
		file_name = os.path.splitext(file_name)[0]
		screenshot.take(name=file_name)
	else:
		mc.confirmDialog(button="Ok", message="Can't find the file name (did you save your scene ?)", title="Error")

	
create()