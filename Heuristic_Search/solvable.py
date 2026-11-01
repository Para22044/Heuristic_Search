from typing import Final

class Solvable:
    """Contains a function to check the solvability of 8-Puzzle states.

    ==================  ==================================================
    Function            Description
    ==================  ==================================================
    solvable            Check the solvability of an 8-Puzzle state.
    """
    @staticmethod
    def solvable(array: int):
        """Check the solvability of an 8-Puzzle state.

        :param array: Integer type array representing the initial puzzle state.
        :return: Boolean value representing if the given puzzle state is solvable.
        """

        inversion_count: int = 0
        LENGTH: Final[int] = len(array)

        for var1 in range(0, LENGTH - 1):
            for var2 in range(var1 + 1, LENGTH):

                if (
                    array[var1] != 0
                    and array[var2] != 0
                    and array[var1] > array[var2]
                ):
                    inversion_count += 1

        return inversion_count % 2 == 0