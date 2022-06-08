# requirements, design, test
'''

Design:
    Each song has atleast 2 building blocks (bb) and each bb has notes.
    Create the bb first. Then create the song by combining the bb.

    Combine already existing bb into a new song:
    Randomly select bb WAV files. 
    Then let the user choose them. After that the user can swap the building block orders.
    When swapping is done. Pick the selected bb WAV files and copy them into a new WAV file, but with another name. 
    Also Create the new song by combining the bb WAV files
'''


from dataStorage import DataStorage
from song import Song
import playsound # Version 1.2.2 is used here. playsound version 1.3 gives error.
import os
from pathlib import Path
import glob as gl
import random as rd
import itertools

class MelodyMaker:
    def getUserPreference(self):
        self.songAmount = self.askValue("How many songs? Atleast 1. ", int)
        self.buildingBlockAmount = self.askValue("How many building blocks per song? Atleast 2. ", int)
        
    def askValue(self,message, desired_type):
        while True:
            try:
                return desired_type(input(message))
            except ValueError:
                print("cannot convert input to", str(desired_type))

    def start(self):
        if(self.songAmount < 1 or self.buildingBlockAmount < 2): # Atleast 1 song and 2 building block
            return
        
        self.db = DataStorage()

        # if restart add these 3 functions
        self.db.createDatabaseDirectory()
        self.db.createPickleFile(str(Path(os.getcwd()).joinpath("database")) + "\SongData", (self.songAmount,self.buildingBlockAmount)) # Write the data from the songs to a pickle file
        self.generateSongs()

        # only this if not restart
        self.selectRandomWAVFiles()
        
    def generateSongs(self):
        print("\n---Generate songs---\n")
        databasePath = str(Path(os.getcwd()).joinpath("database")) # music\database.
        
        for songIndex in range(self.songAmount):
            # Create the building blocks and the song
            song = Song()
            song.createRandomBuildingBlock(self.buildingBlockAmount) 
            combinedSong = song.createSong() 

            self.db.createWAVfile(databasePath + f"\Song{songIndex}.wav", combinedSong) # Write the song to a WAV file

            print(f"\nNow playing song {songIndex}")
            playsound.playsound(databasePath + f"\Song{songIndex}.wav") # Play the wav file from the song

            # Write the building blocks to WAV and pickle files and play the WAV file
            print(f"\nNow playing buildingblocks from song {songIndex}")
            for buildingBlockIndex in range(len(song.buildingBlocks)):
                self.db.createWAVfile(databasePath + f"\Song{songIndex}bb{buildingBlockIndex}.wav", song.buildingBlocks[buildingBlockIndex].notes)
                self.db.createPickleFile(databasePath + f"\Song{songIndex}bb{buildingBlockIndex}", song.buildingBlocks[buildingBlockIndex].notes)
                playsound.playsound(databasePath + f"\Song{songIndex}bb{buildingBlockIndex}.wav")

    # Choose random WAV files from building blocks
    def selectRandomWAVFiles(self): 

        # GROTE WHILE LOOP WITH MUTATE CHANCE

        print("\n---Combining---\n")
        databasePath = str(Path(os.getcwd()).joinpath("database")) # music\database.
        songAmount, buildingBlockAmount = self.db.getPickleFileData(databasePath + "\SongData")
        
        #  Buildingblock amount x 2 will be given as options
        givenSize = 2 * buildingBlockAmount
        buildingBlockWAVFileOptions = []

        for i in range(givenSize): # Randomly select the WAV files with bb (BuildingBlock) in its name.
            buildingBlockWAVFileOptions.append(rd.choice(gl.glob(str(Path(os.getcwd()).joinpath("database")) + '\*bb*.wav')))

        print(f"Random building blocks are given. Choose the {buildingBlockAmount} building blocks from the {givenSize} given options to combine into a new song.")

        # Listening to the WAV files from the building blocks
        while (True):
            print("Enter the number from the building block you want to listen to.")
            print(f"Given building blocks are number 1 to {givenSize}.")
            chosenNumber = self.askValue("If you want to stop listening and want to start selecting. Enter 0. ", int)

            if (chosenNumber == 0): # Quit loop and continue selecting
                break

            if (chosenNumber < 0 or chosenNumber > givenSize):
                print("Number does not exist")
            else: 
                print(f"Now listening to building block number {chosenNumber}\n")
                playsound.playsound(buildingBlockWAVFileOptions[chosenNumber - 1]) # List start with 0

        selectedNumbers = self.getSelectedBuildingBlockIndex(buildingBlockAmount, givenSize) 
        selectedOrder = self.getSortedBuildingBlockIndex(selectedNumbers)
        self.combineBuildingBlockIntoSong(selectedOrder, buildingBlockWAVFileOptions, databasePath)

    # Select the building block index
    def getSelectedBuildingBlockIndex(self, buildingBlockAmount, givenSize):
        selectedIndexes = [] 
        amountOfFilesChosen = 0
        currentIndex = 1

        while (True):
            chosenNumber = self.askValue(f"\nDo you want to select building block number {currentIndex}. [Enter 1 for Yes. Enter 0 for No] ", int)
                
            if (chosenNumber == 1): # Building block selected
                print(f"Building block number {currentIndex} selected.")
                amountOfFilesChosen += 1
                selectedIndexes.append(currentIndex)

                if (amountOfFilesChosen == buildingBlockAmount): # File selection is done
                    print("\n---Building block selection is finished---\n")
                    break
                elif (amountOfFilesChosen < buildingBlockAmount and currentIndex == givenSize): 
                    print(f"But already reached the end of the list, but only {amountOfFilesChosen} out of the {buildingBlockAmount} has been selected. Start over again")
                    currentIndex = 1
                    amountOfFilesChosen = 0
                    selectedIndexes[:] = []
                else: 
                    currentIndex += 1

            elif(chosenNumber == 0): # Building block not selected
                if(amountOfFilesChosen != buildingBlockAmount and currentIndex == givenSize): # List is at the end
                    print(f"\nAlready reached the end of the list, but only {amountOfFilesChosen} out of the {buildingBlockAmount} has been selected. Start over again")
                    currentIndex = 1
                    amountOfFilesChosen = 0
                    selectedIndexes[:] = []
                else: 
                    currentIndex += 1
        
        return selectedIndexes

    # Swap the building block from a song in the order you want
    def getSortedBuildingBlockIndex(self, selectedIndexes): 
        orderList =  list(itertools.permutations(selectedIndexes))
        selectedOrder = []

        for index, order in enumerate(orderList):
            print(index + 1, order)

        while (True):
            chosenNumber = self.askValue("Enter the number from the order you want. ", int)
            if (chosenNumber > -1 and chosenNumber < len(orderList) + 1): # Number is between the given options.
                selectedOrder = orderList[chosenNumber - 1]
                break

        return selectedOrder
        
    def combineBuildingBlockIntoSong(self, selectedOrder, buildingBlockWAVFileOptions, databasePath):
        temporaryList = [x-1 for x in selectedOrder] # Every number - 1 to make the index start at 0 again.
        selectedWAVFiles = []
        newSong = []
        # Add the selected WAV files from all the options to the selectedWAVFiles list.
        for i in range(len(temporaryList)):
            selectedWAVFiles.append(buildingBlockWAVFileOptions[temporaryList[i]])
            newSong += self.db.getPickleFileData(selectedWAVFiles[i][:-4]) # Remove the last 4 chars, which is .wav to get the pickle file and add it to newSong
        
        # make wav from song
        # make from from bb
    
# TO DO

# increment songAmount by 1 for every new song and write it back to the pickle file
# combine
# mutate
# while loop

mm = MelodyMaker()
mm.getUserPreference()
mm.start()