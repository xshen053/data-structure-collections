# 一文讲明白 backtracking

## dfs vs backtrakcing

backtracking 其实和 dfs 是一类问题。

它们之间的区别是微妙的

- dfs 会一直搜索，直到尽头
- backtracking 如果不符合条件，就理解返回

- DFS 就像沿着迷宫的一条路一直走到底，走到尽头才换下一条路。如果目标是遍历整个迷宫，DFS 就能完成任务。
  - 核心是搜索到尽头
- Backtracking 就像走迷宫时，每走一步都要判断是否走到了死路，如果是就立刻回头换路。
  - 核心是探索所有可能的解法

所以可以看成 backtracking 是特殊的 dfs，即提前到了尽头，那就立即返回

backtracking 伴随撤销状态的过程，dfs 不一定需要

## backtracking 问题分类

### 按 input 分类

- array
- string（就是一个 array）
- 2d matrix

### 按顺序分类

- 必须无序，拿球问题（set）
  - 46. permutations
  -
- 有序，（array）
- 顺序无所谓（set，原 input）比如 word search

## 去重

dfs 有一些防止重复遍历的方式

- 2d array 防止重复访问来的路线
  - grid[i][j] = 其它的值
  - 全局 visited
- 1d array 防止重复访问来的路线
  - 全局 visited
- 1d array 防止同一层选相同的数字
  - 每一层 visited
  - arr[i] != arr[i - 1]

## 解题方式

- 先判断这个问题是有序还是无序问题
- 然后判断是否需要去重

## 结论

其实我发现本质上都是图，不管是 array，string 还是 2d matrix

因为我们从一个 index 到另一个 index 就是因为有一条边我们才可以跳过去。

然后我们根据题目给定我们的要求，决定

- 是否可以再次 visit 同一个值
- 是否可以再次 visit 不同 index 但是相同的值
