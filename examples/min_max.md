# Minimum i Maximum

```pseudocode
algorithm MinMax(A, n) {
  // Wczytanie tablicy
  read(n)
  for i ← 1 to n do {
    read(A[i])
  }
  
  // Inicjalizacja min i max
  min ← A[1]
  max ← A[1]
  
  // Szukanie min i max
  for i ← 2 to n do {
    if A[i] < min then {
      min ← A[i]
    }
    
    if A[i] > max then {
      max ← A[i]
    }
  }
  
  // Wypisanie wyniku
  write("Minimum: ", min)
  write("Maximum: ", max)
  write("Różnica: ", max - min)
  
  return max - min
}
```

**Złożoność:** O(n)

**Opis:** Znajduje najmniejszy i największy element w tablicy w jednym przejściu.

**Zasada działania:**
1. Ustaw min i max na pierwszy element
2. Przejdź przez resztę tablicy
3. Aktualizuj min jeśli znajdziesz mniejszy element
4. Aktualizuj max jeśli znajdziesz większy element
