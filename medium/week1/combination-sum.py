# 파이썬 알고리즘 인터뷰  p.351 답안 내용.

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def dfs(csum, index, path, depth):
            # 종료조건
            if csum < 0: #목표 초과
                print(depth, "Goal over path: ", path, csum)
                return
            elif csum == 0: # 목표 달성
                result.append(path)
                print(depth, "Goal met path: ", path, csum)
                return
            else:
                print(depth, "Contiune path: ", path, csum)
            
            # 자신부터 하위 원소까지의 나열 재귀호출
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]], depth+"\t")
            
        dfs(target, 0, [], "")
        return result
