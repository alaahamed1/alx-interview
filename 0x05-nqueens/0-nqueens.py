#!/usr/bin/python3
"""The N queens puzzle
"""

import sys


def check_feasible(Psol, place, N):
    """Checks if place is feasible in the solution Psol
    """
    for queen in Psol:
        if queen[1] == place[1]:
            return False
        Rdiag_queen = queen[0] + queen[1]
        Rduag_place = place[0] + place[1]
        if Rdiag_queen == Rduag_place:
            return False
        Ldiag_queen = queen[0] - queen[1] + N - 1
        Ldiag_place = place[0] - place[1] + N - 1
        if Ldiag_queen == Ldiag_place:
            return False
    return True


def Nqueen_Solving(Psol, N):
    """Get the complete solution of Psol
    or None to backtrack
    """
    if len(Psol) == N:
        print(Psol)
        return
    col = len(Psol)
    for i in range(N):
        place = [col, i]
        if check_feasible(Psol, place, N):
            Psol.append(place)
            Nqueen_Solving(Psol, N)
            Psol.pop()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    N = sys.argv[1]
    if not N.isnumeric():
        print("N must be a number")
        exit(1)
    N = int(N)
    if N < 4:
        print("N must be at least 4")
        exit(1)
    Nqueen_Solving([], N)
