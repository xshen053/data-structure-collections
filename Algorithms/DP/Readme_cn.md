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
