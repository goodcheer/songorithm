class Solution:
    # recursive
    def preorder(self, root: 'Node') -> List[int]:
        def solve(root, ans):
            if root:                          # only continue when root is not None
                ans.append(root.val)          # Append the root
                for child in root.children:   # And recurse for its children
                    solve(child, ans)
            return ans
        return solve(root, [])
        

class Solution2(object):
    # Iterative
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        
        stack, output = [root, ], []            
        while stack:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[::-1]) # since pre-order (root-> left -> right), and pop from stack
                
        return output
