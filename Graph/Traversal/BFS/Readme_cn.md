# 一篇文章讲明白BFS

BFS是一种暴力的搜索方法，我们BFS了一个graph，那必然是遍历了所有的node。BFS了一个tree，那也是一样的。

所以复杂度很好考虑，就是和V和E有关。而所有题目，都会经历几个步骤

1. 识别出题目是Graph或Tree representation（如果需要，则建图）
2. 在图上进行BFS，这里根据不同的表示方法（adj list, adj matrix, edge set)有不同的复杂度
3. bfs就是如下的模版，只是有几个地方不同题目不同，需要进行改动

## BFS 模版
以547. Number of Provinces为例

```Python
                # Place 1: bfs 这里入队
                visited.add(i)
                count += 1
                queue.append(i)
                while queue:
                    # Optional: place 4: min_dis += 1，这里根据题目，可能会求无权最短路径，
                    size = len(queue)
                    for _ in range(size):
                        cur_node = queue.popleft()
                        # Place 2: 这里下面决定遍历哪些元素，以及这些元素要不要入队的condition，不同题目不同
                        for j in range(n):
                            if isConnected[cur_node][j] == 1 and j not in visited:
                                queue.append(j)
                                # Place 3: bfs入队之后就要标记，用visited标记
                                visited.add(j)
        return count

```

## BFS类型

1. adj matrix：找邻居node的条件在Place2处
2. 2d matrix: 变成4 direction入队, Place2处变化
3. 一般的 Tree: 也是place2，变成left和right node入队，并且不需要Place3的visited，因为没有parent节点，我们是一直往下遍历