"""
Another Solution : Regex Expression

while '[' in s:
        s = re.sub(r'(\d+)\[([a-z]*)\]', lambda m: int(m.group(1)) * m.group(2), s)
    return s
"""

class Solution:
    def decodeString(self, s: str) -> str:
        words = []
        nums = []
        n = 0
        cur_s = ''
        for word in s:
            if word == '[':
                words.append(cur_s)
                nums.append(n)
                cur_s = ''
                n = 0
            elif word == ']':
                n = nums.pop()
                prev_s = words.pop()
                cur_s = prev_s + n * cur_s
                n = 0
            elif word.isdigit():
                n = n * 10 + int(word)
            else:
                cur_s += word
        return cur_s

if __name__ == '__main__':
    inst = Solution()
    s = "3[a]2[bc]"
    print(inst.decodeString(s))