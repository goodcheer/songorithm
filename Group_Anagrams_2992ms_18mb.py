class Solution:
    def groupAnagrams(self, strs: list) -> list:
        n = len(strs)
        strs_list = []
        for idx, str_ in enumerate(strs):
            strs_list.append((sorted(list(str_)), idx))
        
        stack = []
        idx_tmp = []
        cnt = 0
        while strs_list:
            cur_str, cur_idx = strs_list.pop()
            if cur_idx in idx_tmp:
                continue
            idx_tmp.append(cur_idx)
            tmp = [strs[cur_idx]]
            for str_, idx in strs_list:
                if str_ == cur_str:
                    tmp.append(strs[idx])
                    idx_tmp.append(idx)
            stack.append(tmp)
            cnt += len(tmp)
            if cnt >= n:
                break
        return stack

if __name__ == '__main__':
    inst = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(inst.groupAnagrams(strs))