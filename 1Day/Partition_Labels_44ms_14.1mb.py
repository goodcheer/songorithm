class Solution:
    def partitionLabels(self, S: str) -> list:
        #Save Last Index
        last_idx = {}
        for idx, val in enumerate(S):
            last_idx[val] = idx
        
        answer = []
        cnt = 0
        max_idx = 0 #Current Max Index
        
        for idx, val in enumerate(S):
            max_idx = max(max_idx, last_idx[val])
            cnt += 1
            if max_idx == idx:
                answer.append(cnt)
                cnt = 0
        return answer

if __name__ == '__main__':
    inst = Solution()
    s = "ababcbacadefegdehijhklij"
    print(inst.partitionLabels(s))