# Przykładowy Algorytm - Suma Elementów

```pseudocode
algorithm SumaElementow(A, n) {
  // Wczytanie tablicy
  read(n)
  for i ← 1 to n do {
    read(A[i])
  }
  
  // Obliczenie sumy
  suma ← 0
  for i ← 1 to n do {
    suma ← suma + A[i]
  }
  
  // Wypisanie wyniku
  write("Suma = ", suma)
  return suma
}
```

**Złożoność:** O(n)

**Opis:** Algorytm wczytuje n liczb do tablicy, a następnie oblicza ich sumę.
