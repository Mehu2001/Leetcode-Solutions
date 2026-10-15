class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = []
        for i in range(rowIndex + 1):
            r = [1] * (i + 1)
            for j in range(1, i):
                r[j] = result[i - 1][j - 1] + result[i - 1][j]
            result.append(r)
        return result[rowIndex]
