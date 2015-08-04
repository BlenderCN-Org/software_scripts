import os
import shutil
import subprocess
import os.path




class Cache_Push():
    def __init__(self):
        self.path_to_cache = "H:\\Cache_2\\"        #Path to Source (Mari cache)
        self.check_last_used()
        self.push_folder()

    def check_last_used(self):
        self.last_used_directory = max([os.path.join(self.path_to_cache, d) for d in os.listdir(self.path_to_cache)], key=os.path.getmtime)
        self.last_used_directory_name = self.last_used_directory.split("\\")[-1]        #Get Cache folder name (longue string)

    def push_folder(self):
        destination_folder = "Z:\\Groupes-cours\\NAND999-A15-N01\\Nature\\tex"
        destPath = destination_folder + "\\"+ self.last_used_directory_name

        for root, dirs, files in os.walk(self.last_used_directory):

            #destination PATH
            dest = destPath + root.replace(self.last_used_directory, '')

            #creer des directory si existe pas
            if not os.path.isdir(dest):
                os.mkdir(dest)
                print 'Folder created at: ' + dest

            #Boucler a travers les files
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








Cache_Push()