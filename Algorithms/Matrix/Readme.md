# 2D Matrix 题型分类
> 以amazon题单为例


## matrix特性

```
y = len(matrix) row
x = len(matrix[0]) col

总元素 x * y

2d => 1d

(r, c) => r * x + c
```

## dfs, bfs

200. Number of Islands  
79. Word Search  
417. Pacific Atlantic Water Flow（不过需要转换下思维，从哪里开始遍历更好）

> 这类题就是基本的bfs，dfs，考察搜索，只不过是在matrix上

## matrix模拟

54. Spiral Matrix  

> 主要考察matrix边界问题

## 多源bfs

994. Rotting Oranges  
542. 01 Matrix  

> 新的思路，bfs的开始可以是多源的

## 2d Backtracking

36. Valid Sudoku （不需要backtracking，但思路和下面一样）  
37. Sudoku Solver  

> 在matrix上做backtracking

## matrix旋转

48. Rotate Image  











