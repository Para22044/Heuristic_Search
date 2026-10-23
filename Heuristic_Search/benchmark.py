# Benchmark wurde iplementiert
# Generiert 100 zufällige lösbare Puzzle-Zustände
# Misst die Leistung der Suchalgorithmen
# Erfasst werden die Ausführungszeit und die Anzal der expandierten Knoten
# Es werden für beide Heuristiken die Mittelwerte und Standardabweichungen berechnet

import time
import statistics

from hamming import Hamming
from manhatten import Manhatten
from puzzle import Puzzle
from solvable import Solvable

class Benchmark:
    
    # Input: None
    # Output: Initailized benchmark object
    # Function: Initializes heuristic and puzzle
    def __init__(self):
        self.hamming = Hamming()
        self.manhatten = Manhatten()
        self.puzzle = Puzzle()

    # Input: None
    # Output: Benchmark results
    # Function: Generates 100 solvable puzzles and tests both heuristics
    def start_test(self):
        puzzles = []

        for i in range (100):

            self.puzzle.fill_field()

            # Generates only solvalbe puzzles
            while not Solvable.solvable(self.puzzle.field):
                self.puzzle.fill_field()

            # Saves a copy of the puzzle
            puzzles.append(tuple(self.puzzle.field))

        # Tests both heuristics with the same puzzles
        self.measure(self.hamming, puzzles)
        self.measure(self.manhatten, puzzles)

    # Input: Heuristic object and 100 puzzles states
    # Output: Mean and standard deviation
    # Function: Measure runtime and expanded nodes
    def measure(self, heuristic, puzzles):
        times = []
        expanded_nodes = []

        print(f"\nTesting {heuristic.__class__.__name__}")

        for i, field in enumerate(puzzles):

            # Starts time measurement
            start_time = time.perf_counter()

            # Solves puzzle
            moves, nodes = heuristic.sovle(field)

            # Stops the measeurement
            end_time = time.perf_counter()

            execution_time = end_time - start_time

            # Saves results
            times.append(execution_time)
            expanded_nodes.append(nodes)

            print(
                f"Test {i + 1}: "
                f"Moves: {moves}, "
                f"Nodes: {nodes}, "
                f"Time: {execution_time:.6f}s"
            )

        # Calculates statistics
        mean_time = statistics.mean(times)
        std_time = statistics.stdev(times)

        mean_nodes = statistics.mean(expanded_nodes)
        std_nodes = statistics.stdev(expanded_nodes)

        # Prints benchmark results
        print(f"\n---- Benchmark Results ----")
        print(f" Heuristic: {heuristic.__class__.__name__}")
        print(f" Mean Time: {mean_time:.6f}s")
        print(f" Standard Deviation Time: {std_time:.6f}s")
        print(f"Mean Expanded Nodes: {mean_nodes:.2f}")
        print(f"Standard Deviation Nodes: {std_nodes:.2f}")