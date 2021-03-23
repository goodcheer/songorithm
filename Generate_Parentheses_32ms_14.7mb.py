class Solution:
    def __init__(self):
        self.answer = set()
        
    def generateParenthesis(self, n: int) -> List[str]:

        def dfs(cur_word, op, cl):
            if not cl:
                self.answer.add(cur_word)
            if op:
                dfs(cur_word + '(', op - 1, cl)
            if op < cl:
                dfs(cur_word + ')', op, cl - 1)
                
        dfs('', n, n)
        
        return list(self.answer)

if __name__ == '__main__':
    inst = Solution()
    exam1 = 3
    exam2 = 4
    print(inst.generateParenthesis(exam1))
    print(inst.generateParenthesis(exam2))