import mari


path = "H:\\Cube.obj"
EmptyChannels = []
mari.projects.create("cube4", path, EmptyChannels, EmptyChannels)

diffuse = mari.geo.current().currentChannel()

mari.geo.current().removeChannel(diffuse)

mari.projects.current().save()
mari.projects.current().close()

mari.app.exit()

# C:\PROGRA~1\Mari2.6v2\Bundle\bin\MARI26~1.EXE
# H:\Projet_Synthese\software_scripts\mari\Mari_delete_diffuse.py