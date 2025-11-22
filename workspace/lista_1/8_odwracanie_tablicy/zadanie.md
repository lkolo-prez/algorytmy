# Odwracanie Tablicy

```pseudocode
algorithm OdwracanieTableoy(A, n) {
  read(n)
  
  for i ← 1 to n do {
    read(A[i])
  }
  
  for i ← 1 to n div 2 do {
    temp ← A[i]
    A[i] ← A[n - i + 1]
    A[n - i + 1] ← temp
  }
  
  for i ← 1 to n do {
    write(A[i], " ")
  }
}
```

Złożoność: O(n) czasowa, O(n) pamięciowa
