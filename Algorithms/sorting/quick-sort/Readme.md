# 一文讲明白 Quicksort

quicksort 是最快的 in-place 排序算法。所以 C 的库里吗 qsort 用的就是 quicksort。quicksort 本质上就是利用 divide and conquer 的原理。我们的 base case 是一个空的 array 和一个长度为 1 的 array。这时候，我们不用排序。

而当我们有一个长度为 2 的 array，我们排序很简单。  
当我们有一个长度为 3 的 array，我们选一个 pivot 然后确保左右 2 个 subarray 都是有序的，那就排序了。所以我们可以分而治之。

把 array 每次都 parition 为 A + pivot + B，然后递归调用 quicksort(A)和 quicksort(B)

partition 就是 divide  
quicksort 就是 conquer  
partition 的目的是为了让 1 个问题分解为 2 个子问题
