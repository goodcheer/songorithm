# 파이썬 알고리즘 인터뷰 p.387 <이진트리의 최대 깊이 (bfs 풀이) 참고함.

from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        q = deque([root])
        vals = []
        
        while q:
            level = []
            
            # 큐 연산 추출 노드의 자식 노드 삽입
            for _ in range(len(q)):  # 부모 노드의 길이 만큼만 반복
                root = q.popleft()
                
                if root.left is not None:
                    q.append(root.left)
                if root.right is not None:
                    q.append(root.right)
                
                level.append(root.val)
            vals.append(level)
            
        return vals
