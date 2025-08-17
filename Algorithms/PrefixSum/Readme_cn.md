# 前缀和常见问题

> 为什么一开始要设置 prefix[0] = 1

因为为了让 edge case 不 edge，其实和 dummy node 是一样的道理

Case Without prefix[0] = 1

Suppose \text{nums} = [5, 2, -2] , k = 5 . 1. At the first element (nums[0] = 5):
• \text{cur_sum} = 5 .
• \text{cur_sum} - k = 5 - 5 = 0 .
• Without prefix[0] = 1, the algorithm fails to count the subarray [5] because prefix does not contain 0.

