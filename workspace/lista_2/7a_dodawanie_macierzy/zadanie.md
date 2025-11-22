# Dodawanie Macierzy

```pseudocode
algorithm DodawanieMacierzy(A, B, C, n, m) {
  read(n, m)
  
  for i ← 1 to n do {
    for j ← 1 to m do {
      read(A[i, j])
    }
  }
  
  for i ← 1 to n do {
    for j ← 1 to m do {
      read(B[i, j])
    }
  }
  
  for i ← 1 to n do {
    for j ← 1 to m do {
      C[i, j] ← A[i, j] + B[i, j]
    }
  }
  
  for i ← 1 to n do {
    for j ← 1 to m do {
      write(C[i, j], " ")
    }
    write("\n")
  }
}
```

Złożoność: O(n·m) czasowa, O(n·m) pamięciowa
