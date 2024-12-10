import random

# 这个是更简单直观的方法
class Solution:
    def sortArray(self, nums):
        def quick_sort(nums):
            if len(nums) < 2:
                return nums
            pivot = random.choice(nums)
            left, mid, right = [], [], []
            # partition
            for num in nums:
                if num < pivot:
                    left.append(num)
                elif num > pivot:
                    right.append(num)
                else:
                    mid.append(num)    
            return quick_sort(left) + mid + quick_sort(right)
        return quick_sort(nums)


# 这个方法partition太容易错了
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
        
        i = high + 1
        for j in range(high, low, -1):
            if arr[j] >= pivot:
                i -= 1
                arr[i], arr[j] = arr[j], arr[i]
        # 结束之后，因为知道[i, high] >= pivot，所以把pivot插到i-1的位置
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
