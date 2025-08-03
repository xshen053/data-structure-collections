
# Binary Search

> 以 amazon 题单为例总结

## 中位数median array类题目

查看灵神题单有更详细总结

https://leetcode.cn/discuss/post/3579164/ti-dan-er-fen-suan-fa-er-fen-da-an-zui-x-3rqn/

4. Median of Two Sorted Arrays
5. Find the Median of the Uniqueness Array

## 找 peak

162. Find Peak Element
163. Peak Index in a Mountain Array

> 主要注意的是 while 里面的 condition 不是`<=` 而是`<`了。因为我们最后剩下的那个元素就是 peak

## merge sort 题

493. Reverse Pairs

> 这题用 merge sort 做，但题目也说了一种用 binary search tree 的做法，不过似乎并不是典型的二分

## 找第一个符合条件的和最后一个符合条件

1011. Capacity To Ship Packages Within D Days
1012. Koko Eating Bananas
2517. Maximum Tastiness of Candy Basket  
1482. Minimum Number of Days to Make m Bouquets  
34. Find First and Last Position of Element in Sorted Array (last，<= 往右； first, >= 往左)
35. Search Insert Position (找最后一个 < target的数，所以应该也是往右移动)

> 这类题都是贪心

找 minimum，某个 size x 就够了， 找 max，最多可以做 x。

如果找 minimum，那就是往左移，找 max 就是一直往右。while 条件没变化，都是`<=`


找first就是找minimum，找last就是找maximum

## LIS二分

354. Russian Doll Envelopes  
300. Longest Increasing Subsequence

> 用二分找到LIS中first index比现在大，替换

## 中规中矩的二分，只是判断条件要改下

540. Single Element in a Sorted Array

## DP二分

1751. Maximum Number of Events That Can Be Attended II  

