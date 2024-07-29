def sortArray(self, nums: list[int]) -> list[int]:
    # merge sort
    def merge(arr1, arr2):
        i = 0
        j = 0
        m = len(arr1)
        n = len(arr2)
        res = []
        while i < m and j < n:
            if arr1[i] < arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1
        if i < m:
            res.extend(arr1[i:])
        if j < n:
            res.extend(arr2[j:])
        return res

    def mergeSort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = mergeSort(arr[:mid])
        right = mergeSort(arr[mid:])
        return merge(left, right)

    return mergeSort(nums)
