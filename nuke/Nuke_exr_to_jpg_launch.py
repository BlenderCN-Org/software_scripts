import subprocess

path_nuke = 'C:\PROGRA~1\Nuke8.0v5\NUKE80~1.EXE'
path_script = 'H:\\Projet_Synthese\\software_scripts\\nuke\\Nuke_exr_to_jpg.py'

subprocess.call([path_nuke, '-t', path_script])