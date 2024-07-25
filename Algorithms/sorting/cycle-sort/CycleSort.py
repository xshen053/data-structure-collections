def cyclesort(arr: list[int]):
  n = len(arr)
  for i in range(n):
    j = arr[i]
    while i != j:
      arr[i], arr[j] = arr[j], arr[i]
      j = arr[i]
  return arr
