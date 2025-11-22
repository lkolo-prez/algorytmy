# Tablica Spiralna

```pseudocode
algorithm TablicaSpiralna(A, n) {
  read(n)
  
  liczba ← 1
  gora ← 1
  dol ← n
  lewa ← 1
  prawa ← n
  
  while gora ≤ dol and lewa ≤ prawa do {
    for i ← gora to dol do {
      A[i, prawa] ← liczba
      liczba ← liczba + 1
    }
    prawa ← prawa - 1
    
    for j ← prawa to lewa step -1 do {
      A[dol, j] ← liczba
      liczba ← liczba + 1
    }
    dol ← dol - 1
    
    for i ← dol to gora step -1 do {
      A[i, lewa] ← liczba
      liczba ← liczba + 1
    }
    lewa ← lewa + 1
    
    for j ← lewa to prawa do {
      A[gora, j] ← liczba
      liczba ← liczba + 1
    }
    gora ← gora + 1
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
