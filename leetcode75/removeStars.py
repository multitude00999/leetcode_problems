class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        for i in s:
            if i == '*':
                res.pop(-1)
            else:
                res.append(i)
        return "".join(res)