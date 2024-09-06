# 一篇文章讲明白动态规划


所有dp问题的特点是，都有最优子结构。

当我们发现一个问题有1最优子结构之后，一棵树就在我们脑海中显现出来了。而我们可以先忽略记忆化，尝试用recursion来解决它。写出recursion的前提，我们只需要考虑
- optimal substructure
- boundary
- general recurrence

思考完了之后，这个问题已经可以解出来了

> 而对于问题的难点，一般就是卡在1最优子结构上，这个需要大量练习，总结题型

dp问题解题5步法
- 什么是optimal substructure？
- recurrence是什么？
- boundary是什么？
- 如何memo？
- 如何转换为iteration

还有一个分类：
- dp弄出来之后，有些题目返回的并不是一个状态的值，而是所有状态中的max或者min
- 所以你就需要遍历所有dp，比如longest palindrome subsequence




