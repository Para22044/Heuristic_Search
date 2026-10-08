# Tests und Auswertung

# Aufgaben: - Testet beide Heuristiken mit denselben (100) zufälligen Startzuständen.
#           - "Execution Time" Misst die Laufzeit.
#           - "Memory Effort" Misst die Anzahl expandierter Knoten
#           - "Mean & Standard Deviation" Berechnet Mittelwert und Standardabweichung.
#           - Vergleichen der Ergebnisse beider Heuristiken.

# temp class for development
class Hamming:
    def solve(self):
        return 42

# temp class for development
class Manhatten:
    def solve(self):
        return 100

from puzzle import Puzzle

class Benchmark:

    def __init__(self):
        self.hamming = Hamming()
        self.manhatten = Manhatten()
        self.puzzle = Puzzle()

        self.start_test()

    def start_test(self):
        self.measure(self.hamming)
        self.measure(self.manhatten)

    def measure(self, heuristic):
        for i in range(100):
            self.puzzle.fill_field()
            result = heuristic.solve()
            print(result)

Benchmark()