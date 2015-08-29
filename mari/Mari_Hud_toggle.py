import mari


def hud_toggle():
    canvas = mari.canvases.current()
    hud_enabled = canvas.getDisplayProperty("HUD/RenderHud")
    toggle_palette = mari.actions.find('/Mari/Actions/Toggle Palettes Visibility')



    if hud_enabled == 1:
        canvas.repaint()
        canvas.setDisplayProperty("HUD/RenderHud", False)
        toggle_palette.trigger()
    if hud_enabled == 0:
        canvas.repaint()
        canvas.setDisplayProperty("HUD/RenderHud", True)
        toggle_palette.trigger()


hud_toggle()