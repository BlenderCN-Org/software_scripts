import mari


def get_thumbnail():
    canvas = mari.canvases.current()
    max_image_size = 512
    canvas_size = canvas.size()
    thumb_width = canvas_size.width()
    thumb_height = canvas_size.height()
    max_thumbnail_size = max(thumb_width, thumb_height)

    thumb_name = str(mari.projects.current().name())
    thumb_path = "H:\\Image Test\\Mari Screenshots\\" + thumb_name + ".jpg"

    #Si le screenshot du canevas depasse le maximum de pixel donnee pour le thumbnail
    if max_thumbnail_size > max_image_size:
        scale = min(float(max_image_size) / float(max_thumbnail_size), 1.0)
        thumb_width = max(min(int(thumb_width * scale), thumb_width), 1)
        thumb_height = max(min(int(thumb_height * scale), thumb_height), 1)

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

get_thumbnail()















"""Fonction Thumbnail implementee dans Mari, probleme avec HUD, ne peut pas framer et prendre plusieurs camera"""
"""_________________________________________________________________________________________________________"""
# #Get Thumbnail
# thumb = None
# thumb = canvas.captureImage( thumb_width, thumb_height )
#
# #Save le thumbnail
# thumb.save(thumb_path)
"""_________________________________________________________________________________________________________"""
