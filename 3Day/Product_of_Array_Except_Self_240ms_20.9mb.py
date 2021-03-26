class Solution:
    def productExceptSelf(self, nums: list) -> list:
        n = len(nums)
        answer = [0] * n
        
        answer[0] = 1
        
        #left product
        for i in range(1, n):
            answer[i] = nums[i - 1] * answer[i - 1]
        
        tmp = 1
        #right product
        for j in reversed(range(n)):
            answer[j] *= tmp
            tmp *= nums[j]
        
        return answer

if __name__ == '__main__':
    inst = Solution()
    nums = [1, 2, 3, 4]
    print(inst.productExceptSelf(nums))