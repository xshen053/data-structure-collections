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

## 题型分析

### 根据字符频率，O(1)获取最大频率的letter

767. Reorganize String

### topk

347. Top K Frequent Elements  
23. Merge k Sorted Lists  
215. Kth Largest Element in an Array  
658. Find K Closest Elements

### O(1)获取global最小end

253. Meeting Rooms II

### 两个heap结合

295. Find Median from Data Stream

### Pq + Greedy

1353. Maximum Number of Events That Can Be Attended

### Sliding window sortedDict和heap两种方法

1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit  

### Subarray + pq

2163. Minimum Difference in Sums After Removal of Elements
