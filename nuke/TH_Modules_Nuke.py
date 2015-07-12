import nuke


def scale_nodes( scale ):
    nodes = nuke.selectedNodes()    # GET SELECTED NODES
    amount = len( nodes )    # GET NUMBER OF SELECTED NODES
    if amount == 0:    return # DO NOTHING IF NO NODES WERE SELECTED

    allX = sum( [ n.xpos()+n.screenWidth()/2 for n in nodes ] )  # SUM OF ALL X VALUES
    allY = sum( [ n.ypos()+n.screenHeight()/2 for n in nodes ] ) # SUM OF ALL Y VALUES

    # CENTER OF SELECTED NODES
    centreX = allX / amount
    centreY = allY / amount

    # REASSIGN NODE POSITIONS AS A FACTOR OF THEIR DISTANCE TO THE SELECTION CENTER
    for n in nodes:
        n.setXpos( centreX + ( n.xpos() - centreX ) * scale )
        n.setYpos( centreY + ( n.ypos() - centreY ) * scale )

def remove_mb_channels():
    for s in nuke.allNodes("ScanlineRender"):
        s.knob("MB_channel").setValue("none")
        s['output_motion_vectors_type'].setValue(0)

def set_merge_bbox_B():
    for s in nuke.allNodes("Merge2"):
        s['bbox'].setValue(3)

def precomp_write():

	first_node = nuke.selectedNode()

	read_node = nuke.selectedNode().dependencies()
	nodes_list = []

	while read_node:
	    read_node = read_node[0].dependencies()
	    nodes_list.append(read_node)

	read_node = nodes_list[-2][0]
	read_path = read_node.knob("file").value()
	file_name = read_path.split("/")[-1].split(".")[0]

	file_path = read_path.split("/")[:-1]
	file_path = "/".join(file_path)
	write_path = "{0}/precomp/{1}_precomp.%04d.jpg".format(file_path, file_name)

	write_node = nuke.nodes.Write()
	write_node.setInput(0, first_node)
	write_node.setSelected(True)
	write_node.knob("file").setValue(write_path)
	write_node.knob("file_type").setValue("jpeg")
	#write_node.knob("channels").setValue("rgba")
	write_node.knob("_jpeg_quality").setValue(100)
	write_node.knob("beforeRender").setValue("import os\nif not os.path.isdir(os.path.dirname(nuke.thisNode()[\'file\'].evaluate())):\n\tos.makedirs(os.path.dirname(nuke.thisNode()[\'file\'].evaluate()))")

	nuke.connectViewer(0,write_node)


def change_framerange_from_read():

	cur_node = nuke.selectedNode()
	first_frame = cur_node["first"].value()
	last_frame = cur_node["last"].value()
	nuke.Root()['first_frame'].setValue(first_frame)
	nuke.Root()['last_frame'].setValue(last_frame)

	nuke.frame(cur_node["first"].value())


def create_read_from_file_path():

	file_list = []

	for (dir, _, files) in os.walk(file_path):
	    for f in files:
	        if f.endswith("png") or f.endswith("PNG") or f.endswith("jpg"):
	            file_list.append(f)

	file_list_frames = [i.split(".")[-2] for i in file_list]
	read_file_path = file_path + "/" + file_list[0].split(".")[0] + ".%04d." + file_list[0].split(".")[-1]
	read_file_path = read_file_path.replace("\\", "/")



	cur_read_node = nuke.nodes.Read()
	cur_read_node["file"].setValue(read_file_path)

	cur_read_node["first"].setValue(int(file_list_frames[0]))
	cur_read_node["last"].setValue(int(file_list_frames[-1]))

	







