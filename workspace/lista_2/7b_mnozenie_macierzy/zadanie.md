# Mnożenie Macierzy

```pseudocode
algorithm MnozenieMacierzy(A, B, C, n, m, k) {
  read(n, m, k)
  
  for i ← 1 to n do {
    for j ← 1 to m do {
      read(A[i, j])
    }
  }
  
  for i ← 1 to m do {
    for j ← 1 to k do {
      read(B[i, j])
    }
  }
  
  for i ← 1 to n do {
    for j ← 1 to k do {
      C[i, j] ← 0
      
      for l ← 1 to m do {
        C[i, j] ← C[i, j] + A[i, l] · B[l, j]
      }
    }
  }
  
  for i ← 1 to n do {
    for j ← 1 to k do {
      write(C[i, j], " ")
    }
    write("\n")
  }
}
```

Złożoność: O(n·m·k) czasowa, O(n·m+m·k+n·k) pamięciowa
