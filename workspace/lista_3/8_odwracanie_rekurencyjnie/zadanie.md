# Odwracanie Tablicy - Rekurencyjnie

```pseudocode
algorithm OdwracanieTablicyRek(A, n) {
  read(n)
  
  for i ← 1 to n do {
    read(A[i])
  }
  
  OdwracanieRek(A, 1, n)
  
  for i ← 1 to n do {
    write(A[i], " ")
  }
}

algorithm OdwracanieRek(A, lewo, prawo) {
  if lewo < prawo then {
    temp ← A[lewo]
    A[lewo] ← A[prawo]
    A[prawo] ← temp
    OdwracanieRek(A, lewo + 1, prawo - 1)
  }
}
```

Złożoność: O(n) czasowa, O(n) pamięciowa (stos rekursji)
