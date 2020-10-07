def removeElement(self, arr, val):
        i = 0
        j = 0
        for i in range(len(arr)):
            if arr[i] == val:
                continue
            arr[j] = arr[i]
            j = j + 1
        return j
