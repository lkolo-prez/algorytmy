# Maximum - Dziel i Zwyciężaj - Wyjaśnienie

## Opis
Algorytm znajduje maksimum w tablicy używając strategii Dziel i Zwyciężaj. Tablica jest dzielona na połowy, maksimum znajduje się w każdej połowie rekurencyjnie, potem wyniki są porównywane.

## Dane Wejściowe
- **n**: liczba elementów
- **A[1..n]**: tablica liczb

## Wynik
**maksimum**: największy element w tablicy

## Strategi D&Z
1. Dziel: podziel tablicę na dwie połowy (srodek = (lewo + prawo) / 2)
2. Zwyciężaj: znajdź maksimum w lewej połowie rekurencyjnie
3. Zwyciężaj: znajdź maksimum w prawej połowie rekurencyjnie
4. Łącz: porównaj oba maksima i zwróć większe

## Przykład
```
A = [3, 7, 2, 9, 1, 5]

Wołanie 1: MaxRek(A, 1, 6)
  srodek = 3
  Wołanie 2: MaxRek(A, 1, 3) → max([3,7,2]) = 7
  Wołanie 3: MaxRek(A, 4, 6) → max([9,1,5]) = 9
  max(7, 9) = 9 ✓

Głębia rekursji: log2(6) ≈ 3 poziomy
```

## Zastosowania
- Edukacyjny przykład D&Z
- Warianty: FindMin, FindMaxMin (oba naraz)
- Algorytmy sortujące (MergeSort)
- Analiza algorytmów

## Uwagi
- **Złożoność**: O(n) czasowa (nie lepiej niż liniowe przeszukiwanie!)
- **Ale**: pokazuje strukturę D&Z, którą można zoptymalizować dla innych problemów
- **Pamięć**: O(log n) stos rekursji (mniej niż O(n) tablicy wyników)
- **Optimizacja**: w praktyce liniowe przeszukiwanie jest szybsze ze względu na cache
