# Graph

看这个就够了
https://guides.codepath.org/compsci/Graphs#introduction

这里面要注意的是 run time analysis

我们做 dfs，但是不同的 graph 表示，时间不同

```
        | Representation       | Getting all adjacent edges for a vertex | Traversing entire graph | hasEdge(u, v)                     | Space         |
        |----------------------|-----------------------------------------|--------------------------|-----------------------------------|---------------|
        | Adjacency Matrix     | O(V)                                   | O(V²)                    | O(1)                              | O(V²)         |
        | Edge Set             | O(E)                                   | O(E)                     | O(E)                              | O(E)          |
        | Adjacency List       | O(1)                                   | O(V + E)                 | O(max number of edges a vertex has) | O(E + V)    |
```

adj_list 的优势是 traversing entire graph 时间短，所以如果是 bfs，dfs 的话，时间短，因为其实 bfs，dfs 就是暴力搜索整个 graph / tree  
adj_mat 优势是查询 edge 是 O(1)

For interviews, it is vital to know

- how to implement a graph
- basic graph traversals (BFS, DFS)
- how to sort topologically the graph.

# dfs visited 情况

- case 1，每个 dfs 的 visited 是 local 的
  - word break
- case 2，一个 graph 的 dfs 共享
  - number of islands

# graph 题型

- Dijkstra
- bellman-ford
- MST: Kruskal 算法
- spanning tree，union find

## shortest path

dfs 也可以解决 shortest path 问题，但它的问题是，它是暴力的解法，这并不是高效的。对于任何一个 node，我们都会探索它的 neighbour。

而 Dijkstra 通过贪心的方法，确保 efficiency

## BFS vs DFS

- 什么情况适合 BFS
- 什么情况适合 DFS

##

Dijkstra 就是一种加权的 bfs
