# Stack题型

> 以amazon题单为例


## 利用stack特性，撤销
20. Valid Parentheses  
71. Simplify Path  
394. Decode String  

> 了解stack特性

## 单调栈
84. Largest Rectangle in Histogram  
85. Maximal Rectangle  

496. Next Greater Element I  
503. Next Greater Element II  

1081. Smallest Subsequence of Distinct Characters （比大小的是字母）

## 用stack模拟recursion遍历tree
173. Binary Search Tree Iterator  
1008. Construct Binary Search Tree from Preorder Traversal  

## 一些stack的问题可以不用stack解决

844. Backspace String Compare
```Python
# 这个结构非常巧妙
# 就是我们持续抵消#和对应的letter，直到我们的p1变成一个有效的letter
            while p1 >= 0:
                if s[p1] == "#":
                    skipS += 1
                    p1 -= 1
                elif skipS > 0:
                    skipS -= 1
                    p1 -= 1
                else:
                    break
```

