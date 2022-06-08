import shutil
import os
import tomita.legacy.pysynth as ps
from pathlib import Path
import pickle as pk

class DataStorage:
    def createDatabaseDirectory(self): 
        if os.path.exists(Path(os.getcwd()).joinpath("database")): 
            shutil.rmtree(Path(os.getcwd()).joinpath("database")) # Remove the whole tree when the directory already exist
        
        os.mkdir('database',0o777) # Create a new directory called database in current path
    
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