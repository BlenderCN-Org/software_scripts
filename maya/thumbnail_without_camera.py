import maya.cmds as mc
import maya.mel as mm
import PIL



class ThumbnailWithoutCamera():
    def __init__(self):
        self.base_parameters()
        self.get_thumbnail()

    def base_parameters(self):
        scene_path = "H:\\Image Test\\Maya test"

        mc.select(clear=True)
        mm.eval("modelEditor -e -jointXray true modelPanel4;")

    def get_thumbnail(self):
        for camera in mc.listCameras():
            if camera == "persp":
                pass
            else:
                mm.eval("viewFit -all;")
                mc.lookThru(camera)
                mc.playblast( cf= "H:\\Image Test\\" + camera + ".jpg" , fr=1, fmt="image", v=False, wh=[500, 300], orn=False,
                    compression="jpg", quality=100, percent=100 )


