# Tablica: A[i,j] = j - i

```pseudocode
algorithm TablicaFormula(A, n) {
  read(n)
  
  for i ← 1 to n do {
    for j ← 1 to n do {
      A[i, j] ← j - i
    }
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
