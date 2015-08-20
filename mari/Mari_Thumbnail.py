import mari
import time
def open_project():
    mari.projects.open('Cube')





def get_thumbnail():
    canvas = mari.canvases.current()
    camera_front = mari.actions.find('/Mari/Canvas/Camera/Camera Front')
    camera_side = mari.actions.find('/Mari/Canvas/Camera/Camera Left')
    camera_top = mari.actions.find('/Mari/Canvas/Camera/Camera Top')
    camera_list = [ camera_front, camera_side, camera_top ]



    for cameras in camera_list:

        #Se promener a travers les cameras
        cameras.trigger()

        #Refresh le canvas
        canvas.repaint()

        #Frame All
        frame_all = mari.actions.find('/Mari/Canvas/Camera/View All')
        frame_all.trigger()

        #Disable le HUD
        """Ne semble pas fonctionner avec le captureImage"""
        hud_enabled = canvas.getDisplayProperty("HUD/RenderHud")
        if hud_enabled == 1:
            canvas.setDisplayProperty("HUD/RenderHud", False)

        #Prendre Screenshot
        snapAction = mari.actions.find('/Mari/Canvas/Take Screenshot')
        snapAction.trigger()


        #Reenable le HUD
        canvas.setDisplayProperty("HUD/RenderHud", True)


open_project()
time.sleep(3)
get_thumbnail()