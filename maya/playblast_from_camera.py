import maya.cmds as mc


class PlayblastFromCamera(object):
    def __init__(self):



        self.get_camera()
        self.playblast()

    def get_camera(self):
        camera_animation = mc.listCameras()[0]
        mc.lookThru (camera_animation)

    def playblast(self):
        mc.playblast(filename=object, format="image", viewer=True, showOrnaments=False, framePadding=4)