import nuke



def replaceReads():

	readnds = nuke.allNodes("Read")
	for x in readnds:
		pth = x.knob("file").value()
		npth = pth.replace("Z:/Partage temporaire/Frenchies", "H:/NAD/Session 2/Projet_final_3D/COMPOSITING")
		x.knob("file").setValue(npth)
