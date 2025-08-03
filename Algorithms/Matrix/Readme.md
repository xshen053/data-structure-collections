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
695. Max Area of Island

> 这类题就是基本的bfs，dfs，考察搜索，只不过是在matrix上

## 多源bfs


317. Shortest Distance from All Buildings  
542. 01 Matrix  
994. Rotting Oranges  


> 新的思路，bfs的开始可以是多源的

## 2d Backtracking

36. Valid Sudoku （不需要backtracking，但思路和下面一样）  
37. Sudoku Solver  
980. Unique Paths III  

> 在matrix上做backtracking

## 非算法题

48. Rotate Image  
54. Spiral Matrix  
73. Set Matrix Zeroes  

> 主要考察matrix边界问题

## binary search

74. Search a 2D Matrix



## max rectangle 类型题目

84. Largest Rectangle in Histogram  （这题不是matrix的，但可以作为参考）
85. Maximal Rectangle  


## union find

1970. Last Day Where You Can Still Cross

## 2D dp

64. Minimum Path Sum  
931. Minimum Falling Path Sum  
