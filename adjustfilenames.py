import sys
import os

class AdjustFileNames:
    def __init__(self, directory_path = os.path.abspath(os.getcwd())):
        self.toremove = ['.adjustfilenames.py.swp', 'adjustfilenames.py']
        self.directory_path = directory_path
        self.checkDirectory()

    def __del__(self):
        pass

    def checkDirectory(self):
        if os.path.isdir(self.directory_path) == False:
            print('The specified directory does not exist.')
            exit()

    def adjust(self):
        names = os.listdir(self.directory_path)

        #remove self __file__ names from the list
        for rname in self.toremove:
            if rname in names:
                names.remove(rname)

        #adjust names
        for name in names:
            #remove whitespace
            newname = name.replace(' ','') 
            #remove whitespace
            newname = name.replace('_','') 

            #rename file
            os.rename(self.directory_path + '/' + name, self.directory_path + '/' + newname)


if __name__ == '__main__':
    
    path = ''
    if len(sys.argv) == 1:
        path = os.path.abspath(os.getcwd())
    else:
        path = sys.argv[1]


    afn = AdjustFileNames(directory_path = path)
    afn.adjust()
