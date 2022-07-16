import sys
import os

class AdjustFileNames:
    def __init__(self, diractory_path = os.path.abspath(os.getcwd())):
        self.toremove = ['.adjustfilenames.py.swp', 'adjustfilenames.py']
        self.diractory_path = diractory_path
        self.checkDiractory()

    def __del__(self):
        pass

    def checkDiractory(self):
        if os.path.isdir(self.diractory_path) == False:
            print('The specified diractory does not exist.')
            exit()

    def adjust(self):
        names = os.listdir(self.diractory_path)

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
            os.rename(self.diractory_path + '/' + name, self.diractory_path + '/' + newname)


if __name__ == '__main__':
    
    path = ''
    if len(sys.argv) == 1:
        path = os.path.abspath(os.getcwd())
    else:
        path = sys.argv[1]


    afn = AdjustFileNames(diractory_path = path)
    afn.adjust()
