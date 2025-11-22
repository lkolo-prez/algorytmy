# Wyszukiwanie Binarne

```pseudocode
algorithm WyszukiwanieBinarne(A, n, szukana) {
  // Wczytanie danych
  read(n)
  for i ← 1 to n do {
    read(A[i])
  }
  read(szukana)
  
  // Algorytm wyszukiwania binarnego
  left ← 1
  right ← n
  znaleziono ← -1
  
  while left ≤ right do {
    mid ← (left + right) div 2
    
    if A[mid] = szukana then {
      znaleziono ← mid
      left ← right + 1  // Przerwij pętlę
    } else if A[mid] < szukana then {
      left ← mid + 1
    } else {
      right ← mid - 1
    }
  }
  
  // Wynik
  if znaleziono ≠ -1 then {
    write("Znaleziono na pozycji: ", znaleziono)
  } else {
    write("Nie znaleziono")
  }
  
  return znaleziono
}
```

**Złożoność:** O(log n)

**Opis:** Wyszukiwanie binarne w posortowanej tablicy. Wymaga, aby tablica była posortowana rosnąco.

**Zasada działania:**
1. Sprawdź środkowy element
2. Jeśli to szukana wartość - koniec
3. Jeśli szukana wartość jest mniejsza - szukaj w lewej połowie
4. Jeśli szukana wartość jest większa - szukaj w prawej połowie
5. Powtarzaj aż znajdziesz lub zakres będzie pusty
