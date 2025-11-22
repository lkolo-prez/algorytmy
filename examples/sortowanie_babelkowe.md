# Sortowanie Bąbelkowe

```pseudocode
algorithm SortowanieBabelkowe(A, n) {
  // Wczytanie tablicy
  read(n)
  for i ← 1 to n do {
    read(A[i])
  }
  
  // Sortowanie bąbelkowe
  for i ← 1 to n-1 do {
    for j ← 1 to n-i do {
      if A[j] > A[j+1] then {
        // Zamiana miejscami
        temp ← A[j]
        A[j] ← A[j+1]
        A[j+1] ← temp
      }
    }
  }
  
  // Wypisanie posortowanej tablicy
  write("Posortowana tablica:")
  for i ← 1 to n do {
    write(A[i])
  }
  
  return n
}
```

**Złożoność:** O(n²)

**Opis:** Algorytm sortowania przez porównywanie i zamianę sąsiednich elementów.

**Zasada działania:**
1. Porównuj każdą parę sąsiednich elementów
2. Jeśli są w złej kolejności - zamień je
3. Po każdym przebiegu największy element "wypływa" na koniec
4. Powtarzaj dla coraz krótszej części tablicy
