# Zamiana Min i Max w Wierszach

```pseudocode
algorithm ZamanaMinMaxWiersze(A, n, m) {
  read(n, m)
  
  for i ← 1 to n do {
    for j ← 1 to m do {
      read(A[i, j])
    }
  }
  
  for i ← 1 to n do {
    min ← A[i, 1]
    max ← A[i, 1]
    min_idx ← 1
    max_idx ← 1
    
    for j ← 2 to m do {
      if A[i, j] < min then {
        min ← A[i, j]
        min_idx ← j
      }
      
      if A[i, j] > max then {
        max ← A[i, j]
        max_idx ← j
      }
    }
    
    temp ← A[i, min_idx]
    A[i, min_idx] ← A[i, max_idx]
    A[i, max_idx] ← temp
  }
  
  for i ← 1 to n do {
    for j ← 1 to m do {
      write(A[i, j], " ")
    }
    write("\n")
  }
}
```

Złożoność: O(n·m) czasowa, O(n·m) pamięciowa
