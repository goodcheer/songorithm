class Solution:
    def countBits(self, num: int) -> list:
        answer = []
        for n in range(num + 1):
            if not n:
                answer.append(0)
                continue
            bit = bin(n)[2:]
            answer.append(bit.count('1'))
        return answer

if __name__ == '__main__':
    inst = Solution()
    num = 5
    print(inst.countBits(num))