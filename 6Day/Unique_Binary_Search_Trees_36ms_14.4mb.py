# Another Solution : Catalan Number[2! / n! * (n + 1)!]
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1:
            return 1
        arr = [0] * (n + 1)
        arr[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                arr[i] += arr[j] * arr[i - 1 - j]
        return arr[-1]

if __name__ == '__main__':
    inst = Solution()
    n = 3
    print(inst.numTrees(n))