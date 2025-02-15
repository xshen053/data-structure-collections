# 一文讲解 priority queue

从题目 [621. Task Scheduler](https://leetcode.com/problems/task-scheduler/description/) 和 [767. Reorganize String](https://leetcode.com/problems/reorganize-string/description/)可以分析出 heap 的本质

767 我最早的思路就是按照每个 index 为一个 iteration，即单层 loop。但做了 621 之后，621 有 1 个限制，interval.其实要满足这个条件，我们知道我们需要把不同的元素进行 pop，而 heap 自动就满足这个条件了。

其实 heap 特点，不光可以以 O(1)时刻找到最大值，还可以结合间隔一起使用

我之前的盲区就是我在想，如果每个 iteration 都要 push，pop 所有的元素，那复杂度就上去了。但其实每一次可以 pop 对应的 iteration 就顺带往后延了一个。

为什么 767 也能使用 cycle，因为它其实就等于题目加了个条件，interval 为 1，让你 organize string，所以和 621 是完全一样的题目

## python 操作

```Python
pq = []
heapq.heappush(pq, value)
heapq.heappop(pq)

```
