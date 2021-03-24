class Solution:
    def __init__(self):
        self.answer = 0
        
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        for i in range(n):
            for j in range(i + 1, n + 1):
                cur_s = s[i:j]
                if cur_s == cur_s[::-1]:
                    self.answer += 1
        return self.answer

if __name__ == '__main__':
    inst = Solution()
    s = 'abc'
    print(inst.countSubstrings(s))