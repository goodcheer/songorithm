class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                
                # count the palindrome and expand outward
                count += 1
                print(f"count: {count}, {s}[{left}] {s}[{right}]")
                left -= 1
                right += 1
            return count
        palindromes = 0
        for i in range(len(s)):
            print(i)
            # the idea is to expand around the 'center' of the string, but the center could be 1 or 2 letters
            # e.g., babab and cbbd, hence the (i, i) and (i, i + 1)
            print(f"expand({i},{i})")
            palindromes += expand(i, i)
            print(f"expand({i},{i+1})")
            palindromes += expand(i, i+ 1)
        return palindromes
    

		
        
if __name__ == "__main__":
    sol = Solution()
    
    in_put = "aaa"
    
    assert sol.countSubstrings(in_put) == 6
    print("pass")
    