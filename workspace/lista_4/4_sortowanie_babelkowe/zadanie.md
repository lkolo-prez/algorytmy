````markdown
# Sortowanie Bąbelkowe

```pseudocode
algorithm SortowanieBabelkowe(A, n) {
  read(n)
  
  for i ← 1 to n do {
    read(A[i])
  }
  
  for i ← 1 to n - 1 do {
    for j ← 1 to n - i do {
      if A[j] > A[j + 1] then {
        temp ← A[j]
        A[j] ← A[j + 1]
        A[j + 1] ← temp
      }
    }
  }
  
  write("Posortowana tablica:")
  for i ← 1 to n do {
    write(A[i], " ")
  }
}
```

Złożoność: O(n²) czasowa (pesymistyczna), O(n) (optymistyczna), O(1) pamięciowa

````
