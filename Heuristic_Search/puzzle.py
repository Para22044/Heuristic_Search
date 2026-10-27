# Puzzle und Lösbarkeit

# Aufgaben: - "Goal State" definieren"
#           - "Random State" erzeugen
#           - "Solvability" ist das Puzzle lösbar
#           - "Conditions & Neighbors" alle möglichen nächsten Zustände durch Verschieben eines Steines erzeugen

import array as arr
import random

class Puzzle:
    """Data class to create and fill playing field.

    ==================  ==================================================
    Function            Description
    ==================  ==================================================
    fill_field          Creates a random state by calling "random.shuffle" on array variable "self.field".
    """

    def __init__(self):
        """Initializes array variable "self.field".
        
        :parameter self:
        """
        
        self.field = arr.array('i', [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def fill_field(self):
        """Creates a random state by calling "random.shuffle" on array variable "self.field".

        :parameter self:
        """
        
        random.shuffle(self.field)
        