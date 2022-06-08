import shutil
import os
import tomita.legacy.pysynth as ps
from pathlib import Path
import pickle as pk

class DataStorage:
    def __init__(self):
        self.databasePath = Path(os.getcwd()).joinpath("database") # Path to the database directory

    def createDatabaseDirectory(self): 
        os.mkdir('database',0o777) 
    
    def checkIfDatabaseDirectoryExist(self):
        return os.path.exists(self.databasePath) if True else False

    def removeDatabaseDirectory(self):
        shutil.rmtree(self.databasePath) 

    def getPickleFileData(self, fileName):
        file = open(fileName, "rb")
        data = pk.load(file)
        file.close()
        return data

    def createPickleFile(self, fileName, data):
        file = open(fileName, "wb")
        pk.dump(data,file)
        file.close()
    

    def createWAVfile(self,fileName, song):
        ps.make_wav (
            song,
            bpm = 130,
            transpose = 1,
            pause = 0.1,
            boost = 1.15,
            repeat = 1,
            fn = fileName,
        )