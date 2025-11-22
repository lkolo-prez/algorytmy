# Zamiana Dwóch Wierszy - Wyjaśnienie

## Opis
Algorytm zamienia całkowicie zawartość dwóch wybranych wierszy macierzy. Wiersze są zamienianie element po elemencie z indeksami i1 i i2.

## Dane Wejściowe
- **n**: liczba wierszy
- **m**: liczba kolumn
- **A[1..n][1..m]**: macierz n×m liczb
- **i1, i2**: indeksy wierszy do zamiany (1 ≤ i1, i2 ≤ n)

## Wynik
**A[1..n][1..m]**: macierz gdzie wiersze i1 i i2 zostały zamienione

## Strategia Rozwiązania

### Kroki Algorytmu
1. Wczytaj n, m, i1, i2 i macierz A
2. Sprawdź czy i1 i i2 są w prawidłowym zakresie
3. Dla każdej kolumny j od 1 do m: zamień A[i1,j] z A[i2,j]
4. Wypisz macierz

## Przykład

### Dane Wejściowe
```
n = 4, m = 3, i1 = 1, i2 = 3
A = [
  [1, 2, 3],      ← wiersz 1
  [4, 5, 6],
  [7, 8, 9],      ← wiersz 3
  [10, 11, 12]
]
```

### Przebieg Algorytmu
```
Kolumna 1: A[1,1] ↔ A[3,1] → 1 ↔ 7
Kolumna 2: A[1,2] ↔ A[3,2] → 2 ↔ 8
Kolumna 3: A[1,3] ↔ A[3,3] → 3 ↔ 9

Wynik:
[7,  8,  9]       ← były wiersz 3
[4,  5,  6]
[1,  2,  3]       ← były wiersz 1
[10, 11, 12]
```

## Zastosowania
- Sortowanie wierszy (przy sortowaniu bąbelkowym macierzy)
- Permutacje wierszy
- Operacje na macierzach
- Algorytmy eliminacji Gaussa (pivot)
- Podstawowy krok algorytmów transformacyjnych

## Uwagi
- **Bezpieczeństwo**: sprawdzenie granic indeksów
- **Niezależność**: zamienianie całego wiersza na raz
- **Czasy**: O(m) na operację zamiany dwóch wierszy
- **Złożoność całkowita**: O(n·m) jeśli liczba zamian = O(n)
- **Edge case**: i1 = i2 (żadna zmiana)
- **Operacja odwracalna**: drugą zaminą przywracamy stan pierwotny
