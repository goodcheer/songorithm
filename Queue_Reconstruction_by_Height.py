"""
######Another Solution#######

class Solution(object):
    def reconstructQueue(self, people):
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res
"""

from collections import deque
class Solution:
    def reconstructQueue(self, people: list) -> list:
        people.sort(key=lambda x : x[0])
        answer = [[h, f] for h, f in people if not f]
        people = deque(sorted(people, key=lambda x : (x[1], -x[0])))
        
        while people:
            cur_height, cur_front = people.popleft()
            if not cur_front:
                continue
            cnt = 0
            for idx, val in enumerate(answer):
                height = val[0]
                if cur_height <= height:
                    cnt += 1
                if cnt == cur_front:
                    answer.insert(idx + 1, [cur_height, cur_front])
            print(answer)
        return answer
if __name__ == '__main__':
    inst = Solution()
    exam1 = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    exam2 = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
    print(inst.reconstructQueue(exam1))
    print(inst.reconstructQueue(exam2))