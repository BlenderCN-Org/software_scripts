from PIL import Image
import os

class Moodboard_Creator():
    def __init__(self):

        # --------------------------------------------------------------------------

        self.dir = "H:\\Image Test\\"       #Path to directory
        self.image_folder = os.listdir( self.dir )
        self.max_image_per_row = 5
        self.vertical_spacing = 50
        self.horizontal_spacing = 50
        self.width_resize = 1500  # Resize horizontal voulu
        self.image_list = []        #Liste pour l'entierete des images
        self.biggest_image_list = []        #Liste pour les images les plus grandes
        for file in self.image_folder:      #Pour chaque image dans le folder a image
            self.image_list.append(Image.open(self.dir + file))     #Rajouter dans la liste
        self.max_row = len(self.image_list)     # Le maximum de row est egal a la totalite des item dans la liste
        self.image_canevas = Image.new("RGB", ( 15000, 15000))  # Creation du canevas (Mode de couleur et grandeur)
        self.second_row = (self.width_resize + 200)

        # --------------------------------------------------------------------------


        self.resize_and_drop()

    def resize_and_drop(self):
        self.list_image_numero = 0

        for row in range(self.max_row):     #Pour chaque row dans le maximum donne
            try:                    #
                y_top = y_bottom + self.vertical_spacing
            except NameError:
                y_top = self.vertical_spacing

            try:
                y_bottom = y_top + max(self.max_height_list)
            except AttributeError:
                y_bottom = self.second_row
            except ValueError:
                pass

            try:
                self.biggest_image_list.append(max(self.max_height_list))
            except AttributeError:
                pass
            except ValueError:
                pass

            self.max_height_list = []       #Liste des images les plus grandes sur la ligne


            for image in range(self.max_image_per_row):     #Pour chaque image par row dans le maximum donne
                try:
                    if image == 0:      #si c'est l'image 0 sur la ligne, on retourne a la marge gauche
                        x_left = self.horizontal_spacing
                    else:
                        x_left = x_right + self.horizontal_spacing

                    x_right = x_left + self.width_resize

                    self.image = self.image_list[self.list_image_numero]       #Prendre image selon list_image si existe dans
                    self.list_image_numero = self.list_image_numero + 1         #+1 Pour pouvoir passer a travers les images

                    wpercent = (self.width_resize / float(self.image.size[0]))
                    hsize = int((float(self.image.size[1]) * float(wpercent)))
                    self.resized_image = self.image.resize((self.width_resize, hsize),Image.ANTIALIAS)  # Resize image a resized_image

                    self.max_height_list.append(self.resized_image.size[1])     #Append la hauteur de chaque image a la liste


                    self.image_canevas.paste(self.resized_image, (x_left, y_top))       #Paste image a canevas




                except IndexError:          #Si liste_image_numero depasse items dans liste_image
                    pass

        self.canevas_resize_horizontal = ( ( (self.horizontal_spacing * self.max_image_per_row) + self.horizontal_spacing ) + self.max_image_per_row * self.width_resize )
        self.canevas_resize_vertical = ( (self.vertical_spacing * 5) + sum(self.biggest_image_list) + 200 )
        self.cropped_canvas = self.image_canevas.crop((0, 0, self.canevas_resize_horizontal, self.canevas_resize_vertical))     #Canevas Cropped

        self.cropped_canvas.save(self.dir + "Moodboard.jpg")

Moodboard_Creator()







