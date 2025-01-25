# 一文讲解 sliding window

sliding window 是基于 brute force 的优化。原因就是，窗口中的状态可以维护，这样整个 array 中的每个元素最多只会访问 2 次，right pointer 一次，left pointer 一次，所以整体复杂度 O(N)
