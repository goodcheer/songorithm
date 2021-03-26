from collections import deque
class Solution:
    def __init__(self):
        self.result = []
        
    def combinationSum(self, candidates: list, target: int) -> list:
        answer = set()
        stack = deque([])
        for cand in candidates:
            if cand == target:
                self.result.append([cand])
            else:
                stack.append([cand])
        while stack:
            cur_n = stack.popleft()
            for n in candidates:
                if sum(cur_n) + n == target:
                    answer.add(tuple(sorted(cur_n + [n])))
                elif sum(cur_n) + n < target:
                    stack.append(cur_n + [n])
        return list(map(list ,answer)) + self.result

if __name__ == '__main__':
    inst = Solution()
    candidates = [2,3,6,7]
    target = 7
    print(inst.combinationSum(candidates, target))