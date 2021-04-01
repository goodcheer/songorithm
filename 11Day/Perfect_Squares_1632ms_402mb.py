class Solution:
    def __init__(self):
        self.nums = []
        self.cnt = 1
        
    def numSquares(self, n: int) -> int:
        for i in range(1, int(n ** 0.5) + 1):
            self.nums.append(i ** 2)
        if n in self.nums:
            return 1
        stack = self.nums[:]
        while True:
            tmp = []
            for prev in stack:
                for cur in self.nums:
                    if prev + cur == n:
                        return self.cnt + 1
                    tmp.append(prev + cur)
            self.cnt += 1
            stack = tmp[:]

if __name__ == '__main__':
    inst = Solution()
    n = 12
    print(inst.numSquares(n))