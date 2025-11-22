# Zamiana Dwóch Wierszy

```pseudocode
algorithm ZamianaDwochWierszy(A, n, m, i1, i2) {
  read(n, m, i1, i2)
  
  for i ← 1 to n do {
    for j ← 1 to m do {
      read(A[i, j])
    }
  }
  
  if i1 ≥ 1 and i1 ≤ n and i2 ≥ 1 and i2 ≤ n then {
    for j ← 1 to m do {
      temp ← A[i1, j]
      A[i1, j] ← A[i2, j]
      A[i2, j] ← temp
    }
  } else {
    write("Błąd: indeksy poza zakresem")
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
