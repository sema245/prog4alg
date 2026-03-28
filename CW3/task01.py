
class Solution:
    @staticmethod
    def removeStars(s: str) -> str:
        zv = 0
        str = ''
        for i in range(len(s)-1, -1, -1):
            if s[i] != '*':
                if zv != 0:
                    zv -= 1
                    continue
                else:
                    str = s[i] + str
            else:
                zv += 1
        return str

print(Solution.removeStars("abc"))