class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        nchar = len(p)
        target = sorted(p)
        result = []
        for i in range(0, len(s)-nchar+1):
            if sorted(s[i:i+nchar]) == target:
                result.append(i)
        return result
        
