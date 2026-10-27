# A*-Suchalgorithmus

# Aufgaben: - Implementierung des A*-Suchalgorithmus.
#           - Verwendung der Heuristiken, um den besten Weg zum Ziel zu finden.
#           - Berechnung der Anzahl der benötigten Schritte.
#           - "Expanded Nodes" Zählt die expandierten Knoten.

class Hamming:
    """Class containing functions for the Hamming heuristic.

    ==================  ==================================================
    Function            Description
    ==================  ==================================================
    solve               Solves the 8-puzzle using A* and Manhatten.
    """

    def solve(self, field):
        """Solves the 8-puzzle using A* and Manhatten.
        
        :parameter self:
        :parameter field: Initial puzzle state (array)
        :return: Number of moves and expanded nodes (int)
        """

        return 0, 0