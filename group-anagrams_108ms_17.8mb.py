from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        gbl = defaultdict(list)
        
        for word in strs:
            # l = len(word)
            s = "".join(sorted(word))
            gbl[s].append(word)

        return gbl.values()
