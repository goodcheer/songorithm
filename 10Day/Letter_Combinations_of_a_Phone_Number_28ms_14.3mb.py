from collections import deque
from typing import List
class Solution:
    def __init__(self):
        self.phone = {'2':['a', 'b', 'c'],
                      '3':['d', 'e', 'f'],
                      '4':['g', 'h', 'i'],
                      '5':['j', 'k', 'l'],
                      '6':['m', 'n', 'o'],
                      '7':['p', 'q', 'r', 's'],
                      '8':['t', 'u', 'v'],
                      '9':['w', 'x', 'y', 'z']}

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digits = deque(list(digits))
        
        stack = ['']
        while digits:
            tmp = []
            cur_digit = digits.popleft()
            cur_words = self.phone[cur_digit]
            for prev_word in stack:
                for cur_word in cur_words:
                    tmp.append(prev_word + cur_word)
            stack = tmp[:]
        return stack

if __name__ == '__main__':
    inst = Solution()
    digits = "23"
    print(inst.letterCombinations(digits))