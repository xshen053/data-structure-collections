# 一篇文章讲明白动态规划

所有 dp 问题的特点是，都有最优子结构。

当我们发现一个问题有 1 最优子结构之后，一棵树就在我们脑海中显现出来了。而我们可以先忽略记忆化，尝试用 recursion 来解决它。写出 recursion 的前提，我们只需要考虑

- optimal substructure
- boundary
- general recurrence

思考完了之后，这个问题已经可以解出来了

> 而对于问题的难点，一般就是卡在 1 最优子结构上，这个需要大量练习，总结题型

dp 问题解题 5 步法

- 什么是 optimal substructure？
- recurrence 是什么？
- boundary 是什么？
- 如何 memo？
- 如何转换为 iteration

还有一个分类：

- dp 弄出来之后，有些题目返回的并不是一个状态的值，而是所有状态中的 max 或者 min
- 所以你就需要遍历所有 dp，比如 longest palindrome subsequence
- 还有 124 binary tree maximum path sum
- 还有 53. Maximum Subarray

还有个分类：

- dp 只是其中的一部分，而不是我们要求的
- 42. Trapping Rain Water， `max_left[i] = min(max_left[i - 1], height[i - 1])`
- 我们要求的 `res += max(min(max_right[i], max_left[i]) - height[i], 0)`

## 固定最优子结构的定义（从 coding 角度简化）

> 定义永远 dp(i)为 i...n 而不是 0...i

这样对应所有的 call 就都是 dp(0)

有一类题是反过来的

- amount coin change (其实正的也可以)，就是我现在手上的钱是 amount
- maximum subarray （因为直觉上 dp(i)和 dp(i + 1) 压根没关系），除非你定义为从右往左的 subarray
- 看你怎么定义了

> 如果求 max, e.g. max(dp(i + 2), dp(i + 1)), 无效边界为-INF  
> 如果求 min, e.g. min(dp(i + 2), dp(i + 1)), 无效边界为 INF
> 如果要无影响的，边界设为 0

```
其实顺序反过来的
我们直观思考就是，如果我今天买，我下一天卖会怎么样，再下一天卖会怎么样
就类似链表反过来print一样，recursion就可以反过来，所以我们先考虑的是第n-1天卖买，然后返回给第n-2天

第n-2天卖买，返回给第n-3天

一般的结论就是，这种顺序为----->的，其实都可以用recursion反过来
```

# 解法分析维度 1

## 经典题型 1: array 每一个元素选或不选

[121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)  
[322. coin change](https://leetcode.com/problems/coin-change/description/) (这里会超时)  
[416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/description/)

# 另一个维度分析

## 题型 1: 问 max/min

这类题一般会状态转移除了 dp(i+1)...之外，可能会+1，或者+arr[i]

- 72. Edit Distance
- 64. Minimum Path Sum
- 120. Triangle
- 1186. Maximum Subarray Sum with One Deletion
- 32. Longest Valid Parentheses

## 题型 2，问总共有几种方式

这种一般状态转移不存在+1，一般就是 dp(i) = dp(i + 1) + dp(xxx)...

- 62. Unique Paths
- 63. Unique Paths II
- 91. Decode Ways
- 140. Word Break II
