from PIL import Image
import os
from PyQt4 import QtCore, QtGui
import webbrowser

class Moodboard_Creator():
    def __init__(self, image_list):

        
        self.max_images_per_row = 4 # Maximum number of images per row
        self.spacing = 24 # Space between each image
        self.maximum_width = 1500  # Maximum image width
        self.image_list = []
        self.original_image_list = image_list
        for image in self.original_image_list: # Create PIL images list from images
            self.image_list.append(Image.open(image))

        # Resize all images to maximum width
        self.resize_images()

        # Get height and width of moodboard image based on new images sizes
        self.get_canvas_size()

        # Create moodboard image from resized images
        self.create_moodboard()

    def get_canvas_size(self):

        # Split main list into sublists of x images (x being equal to the maximum number of images per row)
        rows = [self.image_list[i:i+self.max_images_per_row] for i in range(0, len(self.image_list), self.max_images_per_row)]
        
        # Set default width and height values
        width = 0
        height = 0

        for images in rows:
            width_list = []
            height_list = []

            # Get the sum of all width of current row images and if it is higher than previous row, set new width
            for image in images:
                width_list.append(image.size[0])
                height_list.append(image.size[1])

            if sum(width_list) > width:
                width = sum(width_list)
            if sum(height_list) > height:
                height = sum(height_list)

        # Create final moodboard image with correct dimension
        self.final_image = Image.new("RGB", ( width, height + self.spacing), (12,12,12))

    def resize_images(self):

        # Resize all images to maximum width
        self.resized_images_list = []
        for i, each_image in enumerate(self.image_list):
            if each_image.size[0] > 1500: # Resize image if it is larger than 1500 pixels
                wpercent = (self.maximum_width / float(each_image.size[0]))
                height = int((float(each_image.size[1]) * float(wpercent)))
                each_image = each_image.resize((self.maximum_width, height), Image.ANTIALIAS)

            self.resized_images_list.append(each_image)

        # Split resized list into sublists of x images (x being equal to the maximum number of images per row)
        self.resized_images_list = [self.resized_images_list[i:i+self.max_images_per_row] for i in range(0, len(self.resized_images_list), self.max_images_per_row)]

    def create_moodboard(self):
        pos_y = self.spacing
        # Go through each row
        for i, each_row in enumerate(self.resized_images_list):
            maximum_row_height = []
            pos_x = self.spacing

            # Go through each image in current row
            for i2, image in enumerate(each_row):
                # Get current image height
                height = image.size[1]
                maximum_row_height.append(height)

                if i2 != 0: # Loop is at image 2 or higher in current row
                    pos_x += each_row[i2-1].size[0] + self.spacing

                if i == 0: # Loop is in first row
                    self.final_image.paste(image, (pos_x, self.spacing))
                else: # Loop is in row 2 or higher
                    self.final_image.paste(image, (pos_x, pos_y + self.spacing))

            # Set new pos_y        
            pos_y += max(maximum_row_height) + self.spacing


        self.final_image.show()





Moodboard_Creator(["C:\\Users\\Thibault\\Desktop\\test\\nat_xxx_xxxx_ref_SculptureZambi_01_backup.jpg",
"C:\\Users\\Thibault\\Desktop\\test\\nat_xxx_xxxx_ref_serpentsBocaux_01_backup.jpg",
"C:\\Users\\Thibault\\Desktop\\test\\nat_xxx_xxxx_ref_serpentsBocaux_02_backup.jpg",
"C:\\Users\\Thibault\\Desktop\\test\\nat_xxx_xxxx_ref_serpentsBocaux_03_backup.jpg",
"C:\\Users\\Thibault\\Desktop\\test\\nat_xxx_xxxx_ref_squelettesDeCerfs_01_backup.jpg",
"C:\\Users\\Thibault\\Desktop\\test\\nat_xxx_xxxx_ref_statue_01_backup.jpg",
"C:\\Users\\Thibault\\Desktop\\test\\nat_xxx_xxxx_ref_statueMexicaine_01_backup.jpg",
"C:\\Users\\Thibault\\Desktop\\test\\nat_xxx_xxxx_ref_tempeteDeSable_01_backup.jpg",
"C:\\Users\\Thibault\\Desktop\\test\\nat_xxx_xxxx_ref_tempeteDeSable_02_backup.jpg",
"C:\\Users\\Thibault\\Desktop\\test\\nat_xxx_xxxx_ref_tempeteDeSable_03_backup.jpg",
"C:\\Users\\Thibault\\Desktop\\test\\nat_xxx_xxxx_ref_templeOfDedur_01_backup.jpg",
"C:\\Users\\Thibault\\Desktop\\test\\nat_xxx_xxxx_ref_texture_01_backup.jpg",
"C:\\Users\\Thibault\\Desktop\\test\\nat_xxx_xxxx_ref_texture_02_backup.jpg",
"C:\\Users\\Thibault\\Desktop\\test\\nat_xxx_xxxx_ref_textureAgabat_01_backup.jpg",
"C:\\Users\\Thibault\\Desktop\\test\\nat_xxx_xxxx_ref_textureEau_01_backup.jpg",
"C:\\Users\\Thibault\\Desktop\\test\\nat_xxx_xxxx_ref_texturePaysage_01_backup.jpg",
"C:\\Users\\Thibault\\Desktop\\test\\nat_xxx_xxxx_ref_textureVolcanVuDeLespace_01_backup.jpg",
"C:\\Users\\Thibault\\Desktop\\test\\nat_xxx_xxxx_ref_TheDecorativeArtsMuseumInParis_01_backup.jpg"])


