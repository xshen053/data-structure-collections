- cycle sort
- selection sort: Find the smallest item and put it at the front.
- heap sort
- merge sort: Merge two sorted halves into one sorted whole.
- insertion sort: Figure out where to insert the current item.
- quick sort: Partition items around a pivot.

## Cycle Sort

Just constantly swap 2 numbers until all elements are sorted

## Selection Sort

Selection sorting N items: 
- Find the smallest item in the unsorted portion of the array.
- Move it to the end of the sorted portion of the array.
- Selection sort the remaining unsorted items.

## Heap Sort



## Merge Sort

Top-Down merge sorting N items: 
- Split items into 2 roughly even pieces.
- Mergesort each half (steps not shown, this is a recursive algorithm!)
- Merge the two sorted halves to form the final result.


## Insertion Sort

General strategy: 
- Starting with an empty output sequence.
- Add each item from input, inserting into output at right point.


For naive approach, if output sequence contains k items, worst cost to insert a single item is k.
- Might need to move everything over.


More efficient method:
- Do everything in place using swapping.


## QuickSort

Similar to dutch national flag problem

```Python
        def partition(arr, low, high):
            # Find a pivot
            pivot = arr[low]
            # n = nums.length
            # invariant: 
            #   - [i, high] >= pivot
            #   - [low + 1, i - 1] < pivot
            
            i = high + 1
            for j in range(high, low, -1):
                if arr[j] >= pivot:
                    i -= 1
                    arr[i], arr[j] = arr[j], arr[i]

            # now: 
            # [i, high] >= pivot
            # [low + 1, i - 1] < pivot
            arr[low], arr[i - 1] = arr[i - 1], arr[low]
            # now:
            # [i - 1, high] >= pivot
            # [low, i - 2] < pivot

            # return the index of pivot
            return i - 1
                
        def quickSort(arr, low, high):
            if low < high:
                pi = partition(arr, low, high)
                quickSort(arr, low, pi - 1)
                quickSort(arr, pi + 1, high)
```


