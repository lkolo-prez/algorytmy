# Średnia Arytmetyczna

```pseudocode
algorithm SredniaArytmetyczna(A, n) {
  read(n)
  
  for i ← 1 to n do {
    read(A[i])
  }
  
  suma ← 0
  
  for i ← 1 to n do {
    suma ← suma + A[i]
  }
  
  srednia ← suma / n
  
  write("Średnia = ", srednia)
}
```

Złożoność: O(n) czasowa, O(n) pamięciowa
