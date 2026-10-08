# Puzzle und Lösbarkeit

# Aufgaben: - "Goal State" definieren"
#           - "Random State" erzeugen
#           - "Solvability" ist das Puzzle lösbar
#           - "Conditions & Neighbors" alle möglichen nächsten Zustände durch Verschieben eines Steines erzeugen

import array as arr
import random

class Puzzle:
    def __init__(self):
        self.field = arr.array('i', [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def fill_field(self):
        random.shuffle(self.field)
        