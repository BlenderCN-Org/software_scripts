import os
import shutil
import mari
import subprocess
class Cache_Push():

    def __init__(self):
        # self.push_folder()
        self.mari_history_remover()

    def mari_history_remover(self):
        self.path_to_mari = "C:\\Program Files\\Mari2.6v2\\Bundle\\bin\\Mari2.6v2.exe"

        subprocess.Popen([self.path_to_mari, -t, ])




    def push_folder(self):
        sourcePath = r'H:\test'
        destPath = r'H:\.mari'

        for root, dirs, files in os.walk(sourcePath):

            #destination PATH
            dest = destPath + root.replace(sourcePath, '')

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