# Manhatten Distanz und A* Algorithmus implementiert
# Heuristik berechnet die geschätze Entfernung eines Puzzle-Zustands zum Zielzustand
# A* Algorithmus verwendet die Heuristik, um den kürzesten Lösungsweg zu finden.
# Expandierte Knoten werden gezählt, um den Suchaufwand zu bestimmen.

import heapq

class Manhattan:
    def __init__(self):
        self.goal = (1, 2, 3, 4, 5, 6, 7, 8, 0) # Goal state of the 8-puzzle

    # Input: Current puzzle state (array)
    # Output: Manhatten distance (int)
    # Function: Estimates the distance to the goal state
    def manhattan_distance(self, field):
        distance = 0
        
        for index, tile in enumerate(field):
            if tile != 0:   # Ignores the empty field
                continue
            
            current_row = index // 3
            current_col = index % 3

            goal_row = (tile - 1) // 3
            goal_col = (tile - 1) % 3

            distance += abs(current_row - goal_row)
            distance += abs(current_col - goal_col)

        return distance
    
    # Input: Initial puzzle state (array)
    # Output: Number of moves and expanded nodes (int)
    # Function: Solves the 8-puzzle using A* and Manhatten
    def solve(self, field):
        start = tuple(field)

        # Priority queue: (f, g, state)
        queue = [(self.manhattan_distance(start), 0, start)]
        visited = {start: 0}    # Best known cost for each state

        expanded_nodes = 0

        while queue:
            f, g, current = heapq.heappop(queue)

            if current == self.goal:
                return g
            
            # Skips outdated entries
            if g > visited[current]:
                continue
            
            # Checks if goal state is reached
            if current == self.goal:
                return g, expanded_nodes
            
            # Counts expanded nodes
            expanded_nodes += 1

            # Finds postion of empty field
            zero = current.index(0)
            row, col = divmod(zero, 3)

            neighbors = []

            # Possible movements
            if row > 0:
                neighbors.append(zero - 3)
            if row < 2:
                neighbors.append(zero + 3)
            if col > 0:
                neighbors.append(zero - 1)
            if col < 2:
                neighbors.append(zero + 1)

            # Generates neighboring states
            for neighbor in neighbors:
                new_field = list(current)

                new_field[zero], new_field[neighbor] = (
                    new_field[neighbor],
                    new_field[zero],
                )

                new_state = tuple(new_field)
                new_g = g + 1

                # Only updates if a better path is found
                if new_g < visited.get(new_state, float("inf")):
                    visited[new_state] = new_g

                    # Calculates the heuristic
                    h = self.manhattan_distance(new_state)

                    # A*: f(n) = g(n) + h(n)
                    new_f = new_g + h

                    heapq.heappush(
                        queue,
                        (new_g + h, new_g, new_state)
                    )

        return None, expanded_nodes