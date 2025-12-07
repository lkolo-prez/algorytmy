````markdown
# Sortowanie przez Proste Wybieranie

```pseudocode
algorithm SortowaniePrzezWybieranie(A, n) {
  read(n)
  
  for i ← 1 to n do {
    read(A[i])
  }
  
  for i ← 1 to n - 1 do {
    min_idx ← i
    
    for j ← i + 1 to n do {
      if A[j] < A[min_idx] then {
        min_idx ← j
      }
    }
    
    if min_idx != i then {
      temp ← A[i]
      A[i] ← A[min_idx]
      A[min_idx] ← temp
    }
  }
  
  write("Posortowana tablica:")
  for i ← 1 to n do {
    write(A[i], " ")
  }
}
```

Złożoność: O(n²) czasowa (zawsze), O(1) pamięciowa

````
