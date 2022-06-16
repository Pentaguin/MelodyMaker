import random as rd

# Building block is a group of notes
class BuildingBlock:
    def __init__(self): 
        availableNotes = [[('c', 8), ('d', 8), ('e', 8), ('f', 8), ('g', 8), ('a', 8), ('b', 8), ('c', 8)], # Ionisch
                          [('d', 8), ('e', 8), ('f', 8), ('g', 8), ('a', 8), ('b', 8), ('c', 8), ('d', 8)], # Dorisch
                          [('e', 8), ('f', 8), ('g', 8), ('a', 8), ('b', 8), ('c', 8), ('d', 8), ('e', 8)], # Frygisch
                          [('f', 8), ('g', 8), ('a', 8), ('b', 8), ('c', 8), ('d', 8), ('e', 8), ('f', 8)], # Lydisch
                          [('g', 8), ('a', 8), ('b', 8), ('c', 8), ('d', 8), ('e', 8), ('f', 8), ('g', 8)], # Mixolydisch
                          [('a', 8), ('b', 8), ('c', 8), ('d', 8), ('e', 8), ('f', 8), ('g', 8), ('a', 8)], # Aeolisch
                          [('b', 8), ('c', 8), ('d', 8), ('e', 8), ('f', 8), ('g', 8), ('a', 8), ('b', 8)], # Locrisch
                          [('a', 8), ('c#', 8), ('e', 8)], # A major
                          [('a', 8), ('c', 8), ('e', 8)],  # A minor
                          [('c', 8), ('e', 8), ('g', 8)],  # C major
                          [('c', 8), ('eb', 8), ('g', 8)], # C minor
                          [('d', 8), ('f#', 8), ('a', 8)], # D major
                          [('d', 8), ('f', 8), ('a', 8)],  # D minor
                          [('e', 8), ('g#', 8), ('b', 8)], # E major
                          [('e', 8), ('g', 8), ('b', 8)],  # E minor
                          [('f', 8), ('a', 8), ('c', 8)],  # F major
                          [('f', 8), ('ab', 8), ('c', 8)], # F minor
                          [('g', 8), ('b', 8), ('d', 8)],  # G major
                          [('g', 8), ('bb', 8), ('d', 8)]] # G minor

        self.notes = availableNotes[(rd.randint(0,len(availableNotes) - 1))] # Randomly initialize some notes

