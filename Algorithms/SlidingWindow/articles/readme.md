# 一文讲解 sliding window

sliding window 是基于 brute force 的优化。原因就是，窗口中的状态可以维护，这样整个 array 中的每个元素最多只会访问 2 次，right pointer 一次，left pointer 一次，所以整体复杂度 O(N)

移动 left，其实就是过滤所有 arr[old_l..., right]... arr[old_l..., right + 1...]

因为 right 再往右移动，arr[old_l, right + 1...] 全都是无效的

# post-iteration check

这种 for 循环的题很容易碰到 post-iteration check

两种解决方案

1. 之后再检查一次最后的情况
2. for 循环用 len(s) + 1，这样直接在 for 里面解决

其实都可以在 for 里面做的，可以针对性的练习，之前也碰到过很多这样的题

```Python

# max window
for r in range(n):
  # 窗口不满足条件
  while()

  # 这里满足条件（或若有其他附加条件if在这里check）
  # 满足的话获得max length

# min window
for r in range(n):
  # 窗口满足条件
  while:
    # 这里满足条件
    # 获得min length

  # 这里不满足

```

## 常见题型

> 以 amazon 题单为例

### maximum window 长度

- 3 Longest Substring Without Repeating Characters（unique 元素）

- 1695 Maximum Erasure Value (unique 元素)

- 1658 Minimum Operations to Reduce X to Zero（需转换为这种类型，其实就是求 maximum length）

- 1838 Frequency of the Most Frequent Element （需转换，frequency 就是 window length)

> 合法的 window 是在 while 之后的，while 说明窗口不合法
> 所以计算长度是在 while 之后

### minimum window 长度

- 76. Minimum Window Substring

- 209. Minimum Size Subarray Sum（最小长度）

> 合法窗口在 while 中
> while 是满足条件的

### window size 为 k，求的不是 window 的 length，而是 window 中其他的属性

- 239 Sliding Window Maximum（求 k window 中的 max 元素值）
- 1423 Maximum Points You Can Obtain from Cards（求某个 window 的 minimum sum window length: n - k，但转换和上面 1658 一样）
- 2461 Maximum Sum of Distinct Subarrays With Length K（求 k window 的 max sum）
- 30 Substring with Concatenation of All Words
- 1456 Maximum Number of Vowels in a Substring of Given Length

> 逻辑也是完全一样的

### 替换

- 424. Longest Repeating Character Replacement（替换上限为 k）
- 1004. Max Consecutive Ones III（替换上限为 k）

> 条件是：当前可替换的已经超过 k
> 这 2 题基本完全一样

### 移动 meeting

- 3439. Reschedule Meetings for Maximum Free Time I

维护 size 为 k 的窗口

### at most （求 subarray 的数量满足某个条件）

- 992 Subarrays with K Different Integers（subarray 有 k 个不同 integers）
- 930 Binary Subarrays With Sum（subarray 的和为 k）
  > 此类题目通常无法直接用 window 满足条件，而是用 at_most(n) - at_most(n - 1)

因为 window 我们知道某个 window 的 size 为 n 之后，我们能推断出，这个 window 限制的所有 subarray 都为 at most n，
但不能推断是否为 exactly n。而且我们是找所有 subarray，而不是一个，一个 window 通常只能代表一个 subarray。
我们不能通过 sliding window 去除[old_l...r + 1], ... [old_l...n - 1]

### 用 count 状态维护窗口

- 76 Minimum Window Substring
- 395 Longest Substring with At Least K Repeating Characters

这 2 题都需要一些状态变量来确保 O(1)时间获得某些状态

一个窗口本身需要一些变量来维护状态，比如一个 hashmap。但是还有些变量用来节省时间，我们不需要遍历 hashmap 就可以获得结果。

### 26 个滑窗

每一个你想检查的“条件”，都需要一个变量来维护

## 总结

- 基础滑窗
- 定长滑窗，入，进，出
- word滑窗：30
- at most 滑窗
- 字符频率滑窗： 76，209
- 区间滑窗3439




