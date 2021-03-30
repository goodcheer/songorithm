from collections import Counter, deque
from typing import List
class Solution:
    def __init__(self):
        self.answer = 0
        
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not n:
            return len(tasks)
        cnt = deque(Counter(tasks).most_common())
        while cnt:
            scheduler = []
            for _ in range(n + 1):
                if not cnt or (scheduler and cnt[0][0] == scheduler[0]):
                    break
                cur_task, cur_n = cnt.popleft()
                scheduler.append(cur_task)
                if cur_n - 1:
                    cnt.append((cur_task, cur_n - 1))

            if cnt:
                self.answer += n + 1
            else:
                self.answer += len(scheduler)
            cnt = deque(sorted(list(cnt), key = lambda x: x[1], reverse = True))
        return self.answer

if __name__ == '__main__':
    inst = Solution()
    tasks = ["A","A","A","B","B","B"]
    n = 2
    print(inst.leastInterval(tasks, n))