import nuke

def exr_split():

    #Path for source and where to
    path_for_jpg = "H://Image Test//Nuke Test"
    path_sequence_to_read = "H://Image Test//testEtienne.exr"

    layers = []
    write_number = 1


    #Creation du read node et attribution du path
    read_node = nuke.createNode('Read')
    read_node.knob("file").setValue(path_sequence_to_read)

    #Query pour le first et last frame
    first_frame = read_node.knob("first").value()
    last_frame = read_node.knob("last").value()


    channels = read_node.channels()

    for c in channels:      #Pour tout les channel dans le node
        layers.append(c.split('.')[0])  #Separer les channels  I.E.: RGBA.Red devient [RGBA,Red] et on prend RGBA
    layers = list(set(layers))      #Eliminer les doubles dans la liste


    for lay in layers:
        if lay == "rgba" or lay == "depth":     #Pour layers qui ne sont pas les layers de base RGBA et Depth
            pass
        else:
            #Creer le shuffle et le write
            shuffle_node = nuke.nodes.Shuffle( label= str(lay), inputs= [read_node])
            write_node = nuke.nodes.Write(inputs= [shuffle_node])

            #Linker le shuffle au channel
            shuffle_node['in'].setValue( lay )

            #Changer le filepath du write et executer le rendu
            write_node.knob("file").setValue(path_for_jpg + "/" + lay + ".jpg")
            nuke.execute("Write" + str(write_number), first_frame, last_frame)

            #Iterer le numero du node write
            write_number = write_number + 1

exr_split()


"""
import sys

sys.path.append(r"H:\Projet_Synthese\software_scripts\nuke")

import Nuke_exr_to_jpg as nkj
reload(nkj)

nkj.exr_split()
"""