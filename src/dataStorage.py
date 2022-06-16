import shutil
import os
import tomita.legacy.pysynth as ps
from pathlib import Path
import pickle as pk
import simpleaudio as sa
import sys

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
        with HiddenPrints():
            ps.make_wav (
                song,
                bpm = 130,
                transpose = 1,
                pause = 0.1,
                boost = 1.15,
                repeat = 1,
                fn = fileName,
            )

    def playWAV(self, fileName):
        sa.WaveObject.from_wave_file(fileName).play().wait_done()

# Hide the prints when WAV file is being made
class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout