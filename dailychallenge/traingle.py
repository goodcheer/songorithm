class Solution:
    def minimumTotal(self, T: List[List[int]]) -> int:
        for i in range(len(T)-2,-1,-1):
            # print("i=",i)
            for j in range(len(T[i])-1,-1,-1):
                # print("\tj=",j)
                T[i][j] += min(T[i+1][j], T[i+1][j+1])
                # print(T,)
        return T[0][0]
