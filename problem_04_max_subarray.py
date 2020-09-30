def maxSubArray(self, arr):
        max_sum = arr[0]
        n = len(arr)
        s = 0
        
        for i in range(n):
            s += arr[i]
            max_sum = max(max_sum, s)
            if s < 0: s = 0
        
        return max_sum
