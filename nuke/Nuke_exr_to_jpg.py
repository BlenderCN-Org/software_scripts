import nuke

def exr_split():

    node = nuke.selectedNode()
    channels = node.channels()
    layers = []
    path_for_jpg = "H:/Image Test/Nuke Test"
    first_frame = node.knob("first").value()
    last_frame = node.knob("last").value()
    write_number = 1

    print first_frame
    print last_frame


    for c in channels:      #Pour tout les channel dans le node
        layers.append(c.split('.')[0])  #Separer les channels  I.E.: RGBA.Red devient [RGBA,Red] et on prend RGBA
    layers = list(set(layers))      #Eliminer les doubles dans la liste






    for lay in layers:
        if lay == "rgba" or lay == "depth":     #Pour layers qui ne sont pas les layers de base RGBA et Depth
            pass
        else:

            shuffle_node = nuke.nodes.Shuffle( label= str(lay), inputs= [node])
            write_node = nuke.nodes.Write(inputs= [shuffle_node])
            shuffle_node['in'].setValue( lay )
            write_node.knob("file").setValue(path_for_jpg + "/" + lay + ".jpg")
            nuke.execute("Write" + str(write_number), first_frame, last_frame)
            write_number = write_number + 1

exr_split()