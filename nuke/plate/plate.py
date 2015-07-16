import os
import subprocess

if __name__ == "__main__":

	cur_folder = os.path.dirname(os.path.abspath(__file__))

	os.system("COLOR CF")

	subprocess.call(['C:\Program Files\Nuke8.0v5\Nuke8.0.exe', '-t', cur_folder + '\\nuke_script.py'])

	print "##### SUCCESS #####"

	os.system("COLOR 2F")

	raw_input("Press enter to continue")



