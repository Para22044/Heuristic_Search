
# A*-Suchalgorithmus

# Aufgaben: - Implementierung des A*-Suchalgorithmus.
#           - Verwendung der Heuristiken, um den besten Weg zum Ziel zu finden.
#           - Berechnung der Anzahl der benötigten Schritte.
#           - "Expanded Nodes" zählt die expandierten Knoten.

import heapq


class Hamming:
    """Class containing functions for the Hamming heuristic.

    ==================  ==================================================
    Function            Description
    ==================  ==================================================
    solve               Solves the 8-puzzle using A* and Hamming.
    """

    def __init__(self):
        self.goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

    def hamming_distance(self, field):
        """Counts the tiles that are not in their goal positions."""
        return sum(
            tile != 0 and tile != goal
            for tile, goal in zip(field, self.goal)
        )

    def solve(self, field):
        """Solves the 8-puzzle using A* and Hamming.

        :parameter self:
        :parameter field: Initial puzzle state (array)
        :return: Number of moves and expanded nodes (int)
        """

        start = tuple(field)

        if len(start) != 9 or set(start) != set(self.goal):
            raise ValueError("Invalid puzzle")

        frontier = [(self.hamming_distance(start), 0, start)]
        best_moves = {start: 0}
        expanded_nodes = 0

        while frontier:
            _, moves, current = heapq.heappop(frontier)

            if moves != best_moves[current]:
                continue

            if current == self.goal:
                return moves, expanded_nodes

            expanded_nodes += 1

            blank = current.index(0)
            row, col = divmod(blank, 3)

            neighbors = []
            if row > 0:
                neighbors.append(blank - 3)
            if row < 2:
                neighbors.append(blank + 3)
            if col > 0:
                neighbors.append(blank - 1)
            if col < 2:
                neighbors.append(blank + 1)

            for neighbor in neighbors:
                new = list(current)
                new[blank], new[neighbor] = new[neighbor], new[blank]
                new = tuple(new)

                new_moves = moves + 1

                if new_moves < best_moves.get(new, float("inf")):
                    best_moves[new] = new_moves
                    priority = new_moves + self.hamming_distance(new)
                    heapq.heappush(frontier, (priority, new_moves, new))

        return None, expanded_nodes
