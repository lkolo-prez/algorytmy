# Maximum - Dziel i Zwyciężaj

```pseudocode
algorithm MaximumDzielZwyciez(A, n) {
  read(n)
  
  for i ← 1 to n do {
    read(A[i])
  }
  
  wynik ← MaxRek(A, 1, n)
  write("Maksimum = ", wynik)
}

algorithm MaxRek(A, lewo, prawo) {
  if lewo = prawo then {
    return A[lewo]
  }
  
  srodek ← (lewo + prawo) div 2
  max_lewo ← MaxRek(A, lewo, srodek)
  max_prawo ← MaxRek(A, srodek + 1, prawo)
  
  if max_lewo > max_prawo then {
    return max_lewo
  } else {
    return max_prawo
  }
}
```

Złożoność: O(n) czasowa, O(log n) pamięciowa (stos rekursji)
