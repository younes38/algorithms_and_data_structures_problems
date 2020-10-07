def twoSum(self, arr, target):
        n = len(arr)
        d = {}
        for i in range(n):
            v = arr[i]
            x = target - v
            if d.has_key(x):
                return d[x], i
            d[v] = i
        
        return -1, -1
