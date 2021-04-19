class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    """solution from https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/ """
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        current = root 
        stack = [] # initialize stack
        values = []

        while True:

            # Reach the left most Node of the current Node
            if current is not None:

                # Place pointer to a tree node on the stack 
                # before traversing the node's left subtree
                stack.append(current)

                current = current.left 


            # BackTrack from the empty subtree and visit the Node
            # at the top of the stack; however, if the stack is 
            # empty you are done
            elif(stack):
                current = stack.pop()
                values.append(current.val)

                # We have visited the node and its left 
                # subtree. Now, it's right subtree's turn
                current = current.right 

            else:
                break
            

        return values
        
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    
    ans = Solution.inorderTraversal(root)
    assert ans == [4, 2, 5, 1, 3]