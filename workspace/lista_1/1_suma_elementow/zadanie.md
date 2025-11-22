# Suma Elementów Tablicy

```pseudocode
algorithm SumaTablicy(A, n) {
  read(n)
  
  for i ← 1 to n do {
    read(A[i])
  }
  
  suma ← 0
  
  for i ← 1 to n do {
    suma ← suma + A[i]
  }
  
  write("Suma = ", suma)
}
```

Złożoność: O(n) czasowa, O(n) pamięciowa
