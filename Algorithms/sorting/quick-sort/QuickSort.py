def sortArray(nums: list[int]) -> list[int]:
    """
    Quick Sort:
        - Used leftmost element as pivot
        - @link https://www.geeksforgeeks.org/quick-sort-algorithm/
    """
    def partition(arr, low, high):
        pivot = arr[low]
        # n = nums.length
        # invariant: 
        #   - [i, high] >= pivot
        #   - [low + 1, i - 1] < pivot
        
        i = high + 1
        for j in range(high, low, -1):
            if arr[j] >= pivot:
                i -= 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[low], arr[i - 1] = arr[i - 1], arr[low]

        # return the index of pivot
        return i - 1
            


    def quickSort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quickSort(arr, low, pi - 1)
            quickSort(arr, pi + 1, high)

    quickSort(nums, 0, len(nums) - 1)
    return nums
