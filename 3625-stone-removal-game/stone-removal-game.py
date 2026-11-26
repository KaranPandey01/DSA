class Solution:
    def canAliceWin(self, n: int) -> bool:
        remove = 10
        moves = 0

        while n >= remove:
            n -= remove
            remove -= 1
            moves += 1

        return moves % 2 == 1
