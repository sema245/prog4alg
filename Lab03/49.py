import collections

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            # Сортируем строку для создания универсального ключа
            ans[tuple(sorted(s))].append(s)
        return list(ans.values())
