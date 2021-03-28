class Solution:
    def __init__(self):
        self.dic = {1 : 1, 2 : 2}
        
    def numTrees(self, n: int) -> int:
        if not n:
            return 1
        if n in self.dic:
            return self.dic[n]
        tmp = 0
        for i in range(1, n + 1):
            tmp += self.numTrees(i - 1) * self.numTrees(n - i)
        self.dic[n] = tmp
        return tmp

if __name__ == '__main__':
    inst = Solution()
    n = 3
    print(inst.numTrees(n))