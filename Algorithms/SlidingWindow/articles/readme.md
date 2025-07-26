# 一文讲解 sliding window

sliding window 是基于 brute force 的优化。原因就是，窗口中的状态可以维护，这样整个 array 中的每个元素最多只会访问 2 次，right pointer 一次，left pointer 一次，所以整体复杂度 O(N)

移动 left，其实就是过滤所有 arr[old_l..., right]... arr[new_l..., right]

因为 right 再往右移动，arr[old_l, right + 1...] 全都是无效的

# post-iteration check

这种 for 循环的题很容易碰到 post-iteration check

两种解决方案

1. 之后再检查一次最后的情况
2. for 循环用 len(s) + 1，这样直接在 for 里面解决

其实都可以在 for 里面做的，可以针对性的练习，之前也碰到过很多这样的题
