class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        max_diff = arr[1] - arr[0]
        sign = 1
        if max_diff < 0:
            sign = -1
            max_diff *= sign
            
        for i in range(0, len(arr)-1):
            diff = (arr[i+1] - arr[i]) * sign
            # print(i, diff)
            if diff > max_diff:
                return (arr[i] + arr[i+1]) // 2
            elif diff < max_diff:
                return (arr[i-1] + arr[i]) // 2
        return arr[0]
