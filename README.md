# Data-structure-collections

**TL,DR: 我们在思考“用什么数据结构”时，实际上是在思考“用什么 ADT”来解决问题。**

```
因为：

ADT描述了接口和行为
➡️ 你思考的是“我需要什么功能？”
➡️ 比如：“我需要一个支持 插入 O(1)，查找 O(1) 的数据结构”
➡️ 然后你想到了 HashMap 这个 ADT。

具体的数据结构只是实现方式
➡️ HashMap 可以基于哈希表（常见）
➡️ 也可以基于平衡树（红黑树，比如 C++ std::map）
➡️ 这些是实现细节，在你“用”它的时候，你更多关注的是功能接口（抽象层面）
```

## 从最底层的物理层出发

```
物理结构
├── 顺序存储（Array）
└── 链式存储（Linked List）

逻辑结构
├── 线性结构（List, Stack, Queue）
└── 非线性结构（Tree, Graph, Set）

抽象数据类型（ADT）
├── Stack / Queue / Deque / Priority Queue
├── Map / Set
└── Disjoint Set / Tree / Graph

ADT: Describes the operations and properties (e.g., each node's left subtree contains only nodes with keys less than the node's key).

具体实现
├── 数组 / 链表 / 堆 / 哈希表 / 平衡树
├── 并查集 / Trie
└── 邻接表 / 邻接矩阵
```

所以其实物理层面，只有 2 种结构，array 和 linked list

## Algorithms

- Sorting
- Greedy
- BFS
- DFS
- Dynamic Programming

## 按照数据需求分类

> input 对顺序无要求

- list
- set / map

> input 顺序无要求，但需要考虑组合排列问题

- set / map （把 set 看成袋子，里面拿球）

> 当需要维护 input 的 order，比如 increasing，decreasing

- heap (priority queue)
  - insert O(logn)
  - delete O(n)
- ordereddict / orderedset （python 特有）
  - insert O(logn)
  - delete O(logn)
- treeset / treemap
  - insert O(logn)
  - delete O(logn)
