from array import array

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        count = array('i', [0 for i in range(26)])
        
        for idx, char in enumerate(S):
            key = ord(char)-97
            count[key] += 1
        
        answer = []
        left = 0 
        for right in range(1, len(S)+1):

            tot_family = 0
            shelter = S[left:right]
            n_saved = len(shelter)
            for char in set(shelter):
                key = ord(char)-97
                tot_family += count[key]
            if n_saved == tot_family:
                left = right
                answer.append(n_saved)
        return answer