````markdown
# Sortowanie Szybkie (Quick Sort)

```pseudocode
algorithm Podzial(A, low, high) {
  pivot ← A[high]
  i ← low - 1
  
  for j ← low to high - 1 do {
    if A[j] < pivot then {
      i ← i + 1
      temp ← A[i]
      A[i] ← A[j]
      A[j] ← temp
    }
  }
  
  temp ← A[i + 1]
  A[i + 1] ← A[high]
  A[high] ← temp
  
  return i + 1
}

algorithm SortowanieSzybkie(A, low, high) {
  if low < high then {
    pi ← Podzial(A, low, high)
    SortowanieSzybkie(A, low, pi - 1)
    SortowanieSzybkie(A, pi + 1, high)
  }
}

algorithm QuickSort(A, n) {
  read(n)
  
  for i ← 1 to n do {
    read(A[i])
  }
  
  SortowanieSzybkie(A, 1, n)
  
  write("Posortowana tablica:")
  for i ← 1 to n do {
    write(A[i], " ")
  }
}
```

Złożoność: O(n log n) czasowa średnia, O(n²) pesymistyczna, O(log n) pamięciowa

````
