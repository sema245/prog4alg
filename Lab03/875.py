import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right

        while left <= right:
            k = (left + right) // 2
            # Считаем суммарное время при текущей скорости k
            hours = sum(math.ceil(p / k) for p in piles)

            if hours <= h:
                res = k
                right = k - 1
            else:
                left = k + 1

        return res
