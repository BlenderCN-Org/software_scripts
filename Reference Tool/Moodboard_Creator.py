from PIL import Image
import os

class Moodboard_Creator():
    def __init__(self):
        # --------------------------------------------------------------------------
        self.image_canevas = Image.new("RGB", (2048, 1500))      #Creation du canevas (Mode de couleur et grandeur)
        self.dir = "H:\\Image Test\\"       #Path to directory
        self.image_folder = os.listdir( self.dir )
        self.canevas_size = width, height = self.image_canevas.size      #List Canevas Size
        self.max_image_per_row = 5
        self.max_row = 4
        self.width_resize = 350  # Resize horizontal voulu
        self.image_list = []
        for file in self.image_folder:
            self.image_list.append(Image.open(self.dir + file))
        # --------------------------------------------------------------------------


        self.resize_and_drop()
    def resize_and_drop(self):
        self.list_image = 0
        row = 0

        for row in range(self.max_row):     #Pour chaque row dans le maximum donne
            self.max_height_list = []

            for image in range(self.max_image_per_row):     #Pour chaque image par row dans le maximum donne
                try:
                    self.image = self.image_list[self.list_image]       #Prendre image dans liste si existe
                    self.list_image = self.list_image + 1
                    self.image_size = width, height = self.image.size

                    wpercent = (self.width_resize / float(self.image.size[0]))
                    hsize = int((float(self.image.size[1]) * float(wpercent)))
                    self.resized_image = self.image.resize((self.width_resize, hsize),Image.ANTIALIAS)  # Resize image a resized_image

                    self.max_height_list.append(self.resized_image.size[1])     #Append la hauteur de chaque image a la liste

                except IndexError:
                    pass



                # try:
                #     x_left = x_right + 30
                # except NameError:
                #     x_left = 30
                # x_right = x_left + width_resize
                # y_top = 50

        # for file in self.image_folder:      #Pour image in folder (self.dir)
        #     self.image = Image.open(self.dir + file)        #Ouvrir l'image
        #     image_size = width, height = self.image.size
        #
        #     width_resize = 350      #Resize horizontal voulu
        #     wpercent = (width_resize / float(self.image.size[0]))
        #     hsize = int((float(self.image.size[1]) * float(wpercent)))
        #     self.resized_image = self.image.resize((width_resize, hsize), Image.ANTIALIAS)      #Resize image a resized_image
        #     try:
        #         x_left = x_right + 30
        #     except NameError:
        #         x_left = 30
        #     x_right = x_left + width_resize
        #     y_top = 50
        #     y_bottom = y_top + hsize
        #
        #     self.max_height_list.append(hsize)
        #
        #
        #     self.image_canevas.paste(self.resized_image, (x_left, y_top))
        # print max(self.max_height_list)
        # self.image_canevas.show()



Moodboard_Creator()







