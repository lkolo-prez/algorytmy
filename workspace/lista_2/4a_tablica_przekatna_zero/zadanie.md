# Tablica z Przekątną = 0

```pseudocode
algorithm TablicaPrzekatnaZero(A, n) {
  read(n)
  
  for i ← 1 to n do {
    for j ← 1 to n do {
      read(A[i, j])
    }
  }
  
  for i ← 1 to n do {
    A[i, i] ← 0
  }
  
  for i ← 1 to n do {
    for j ← 1 to n do {
      write(A[i, j], " ")
    }
    write("\n")
  }
}
```

Złożoność: O(n²) czasowa, O(n²) pamięciowa
