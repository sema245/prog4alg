import collections

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = collections.Counter(nums)
        # Возвращаем только сами элементы, игнорируя их частоту
        return [item[0] for item in count.most_common(k)]
