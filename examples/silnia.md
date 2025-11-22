# Silnia (Rekurencyjnie)

```pseudocode
algorithm Silnia(n) {
  // Wczytanie liczby
  read(n)
  
  // Obliczenie silni
  wynik ← ObliczSilnie(n)
  
  // Wypisanie wyniku
  write("Silnia z ", n, " = ", wynik)
  
  return wynik
}

algorithm ObliczSilnie(n) {
  // Warunek bazowy
  if n = 0 then {
    return 1
  }
  
  if n = 1 then {
    return 1
  }
  
  // Wywołanie rekurencyjne
  return n * ObliczSilnie(n - 1)
}
```

**Złożoność:** O(n)

**Opis:** Oblicza silnię liczby n! = n × (n-1) × (n-2) × ... × 2 × 1 używając rekurencji.

**Zasada działania:**
1. Warunek bazowy: 0! = 1, 1! = 1
2. Wywołanie rekurencyjne: n! = n × (n-1)!
3. Każde wywołanie zmniejsza n o 1
4. Rekurencja kończy się gdy n = 0 lub n = 1
