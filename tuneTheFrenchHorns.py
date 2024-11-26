# Create a function named tune_french_horns that receives notes as its parameter.

# This function aims to simulate the tuning of a section of French horns in a concert hall. 
# Each French horn plays a single note represented by a string in the notes array. 
# Due to the unique acoustics of the concert hall, every other note starting from the first note needs 
# to be shifted up an octave, which is represented by capitalizing the note.

# To tune the French horns:

# Iterate through the notes array.
# For each note at an even index (0, 2, 4, ...), capitalize the note to shift it up an octave.
# Leave the notes at odd indices (1, 3, 5, ...) unchanged.
# Return the modified notes array with the French horns tuned according to the concert hall's acoustics.

# Parameter:

# notes (list): An array of strings, where each string represents a musical note played by a French horn. 
# Each note string consists of lowercase English letters (a-g).
# The function returns a list of strings representing the tuned notes, where every other note starting from the first note is capitalized.

def tuneFrenchHorns(notes):
    incre = 0
    res = []
    for i in notes:
        if incre % 2 == 0:
            res.append(i.upper())
        else:
            res.append(i)
        incre += 1
    return res

print(tuneFrenchHorns(['a', 'b', 'c', 'd', 'e']))