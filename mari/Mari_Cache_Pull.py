import os
import shutil
import os.path



class Cache_Pull():
    def __init__(self):
        self.path_to_cache_local = "H:\\Cache_3"
        self.path_to_cache_server = "Z:\\Groupes-cours\\NAND999-A15-N01\\Nature\\tex"
        # self.real_name_and_long_name = {}     Avoir un dict pour selectionner l'objet voulu [Cube : 74aed3[...] ]




    def pull_folder(self):
        destPath = self.path_to_cache_local + "\\" + self.real_name_and_long_name[1]

        for root, dirs, files in os.walk(self.path_to_cache_server):

            # destination PATH
            dest = destPath + root.replace(self.path_to_cache_server, '')

            # creer des directory si existe pas
            if not os.path.isdir(dest):
                os.mkdir(dest)
                print 'Folder created at: ' + dest

            # Boucler a travers les files
            for f in files:

                oldLoc = root + '\\' + f
                newLoc = dest + '\\' + f

                if not os.path.isfile(newLoc):
                    try:
                        shutil.copy2(oldLoc, newLoc)
                        print 'File ' + f + ' copied.'
                    except IOError:
                        print 'File "' + f + '" already exists'
                else:
                    os.remove(newLoc)
                    print "Removing " + f
                    try:
                        shutil.copy2(oldLoc, newLoc)
                        print 'File ' + f + ' copied.'
                    except IOError:
                        print 'File "' + f + '" already exists'
