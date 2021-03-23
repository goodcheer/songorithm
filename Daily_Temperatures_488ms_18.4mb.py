class Solution:
    def dailyTemperatures(self, T: list) -> list:
        n = len(T)
        days = [0] * n
        
        stack = []
        for idx, cur_temp in enumerate(T):
            while stack:
                if cur_temp <= T[stack[-1]]:
                    break
                prev_idx = stack.pop()
                days[prev_idx] = idx - prev_idx
            stack.append(idx)

        return days

if __name__ == '__main__':
    inst = Solution()
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    print(inst.dailyTemperatures(T))