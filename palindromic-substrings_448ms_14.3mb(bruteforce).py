class Solution:
    def countSubstrings(self, s: str) -> int:
        ss = s+s
        n = len(s)
        
        res = n
        window_size = 2
        while window_size < n+1:
            for i in range(0, n+1-window_size):
                substr = s[i:i+window_size]
                if substr == substr[::-1]:
                    res += 1

            window_size += 1
        return res

if __name__ == "__main__":
    sol = Solution()
    
    in_put = "aaa"
    
    assert sol.countSubstrings(in_put) == 6
    print("pass")