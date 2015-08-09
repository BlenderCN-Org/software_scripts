import maya.cmds as mc
import maya.mel as mm

class PlayblastFromCamera(object):
    def __init__(self):
        self.get_camera()
        self.default_render_format()
        self.playblast()

    def get_camera(self):
        camera_animation = mc.listCameras()[0]
        mc.lookThru (camera_animation)
        print camera_animation

    def playblast(self):
        path = "H:\\Image Test\\"
        output_name = "shit"
        mc.playblast(filename= path + output_name, format="image", viewer=False, showOrnaments=False, framePadding=4, )

    def default_render_format(self):
        mm.eval("setAttr defaultRenderGlobals.imageFormat 8;")
