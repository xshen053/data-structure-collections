def sortArray(nums: list[int]) -> list[int]:
    # Selection Sort: O(n^2)
    # n = nums.length
    # invariant:
    #   - [0, i] sorted
    #   - [i + 1, n - 1] unsorted
    i = -1
    while i < len(nums) - 1:
        smallest = float("inf")
        smallest_index = -1
        for j in range(i + 1, len(nums)):
            if nums[j] < smallest:
                smallest = nums[j]
                smallest_index = j
        i += 1
        nums[i], nums[smallest_index] = nums[smallest_index], nums[i]

    return nums
