from buildingBlock import BuildingBlock

# A song is a group of building blocks
class Song:
    def __init__(self):
        self.buildingBlocks = []

    # Create random building blocks
    def createRandomBuildingBlock(self,buildingBlockAmount):
        for i in range(buildingBlockAmount):
            self.buildingBlocks.append(BuildingBlock())

    # Combine all the buildingblocks together to get 1 song
    def createSong(self): 
        combinedBuildingBlocks = []

        for buildingBlock in self.buildingBlocks: 
            combinedBuildingBlocks += buildingBlock.notes

        return combinedBuildingBlocks















