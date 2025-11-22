# Zamiana Min i Max w Wierszach - Wyjaśnienie

## Opis
Algorytm dla każdego wiersza macierzy znajduje element minimalny i maksymalny, a następnie je zamienia. Operacja wykonywana jest dla każdego wiersza niezależnie.

## Dane Wejściowe
- **n**: liczba wierszy
- **m**: liczba kolumn
- **A[1..n][1..m]**: macierz n×m liczb

## Wynik
**A[1..n][1..m]**: macierz gdzie w każdym wierszu min i max zostały zamienione

## Strategia Rozwiązania

### Kroki Algorytmu
1. Wczytaj n, m i macierz A
2. Dla każdego wiersza i:
   - Znajdź element minimalny i jego pozycję
   - Znajdź element maksymalny i jego pozycję
   - Zamień te elementy
3. Wypisz zmodyfikowaną macierz

## Przykład

### Dane Wejściowe
```
n = 3, m = 4
A = [
  [1, 5, 3, 9],
  [2, 8, 4, 6],
  [7, 3, 2, 5]
]
```

### Przebieg Algorytmu
```
Wiersz 1: [1, 5, 3, 9]
  min = 1 (idx=1), max = 9 (idx=4)
  Po zamianie: [9, 5, 3, 1]

Wiersz 2: [2, 8, 4, 6]
  min = 2 (idx=1), max = 8 (idx=2)
  Po zamianie: [8, 2, 4, 6]

Wiersz 3: [7, 3, 2, 5]
  min = 2 (idx=3), max = 7 (idx=1)
  Po zamianie: [2, 3, 7, 5]

Wynik:
[9, 5, 3, 1]
[8, 2, 4, 6]
[2, 3, 7, 5]
```

## Zastosowania
- Przetwarzanie macierzy danych
- Normalizacja danych (zamiany graniczne)
- Transformacje strukturalne
- Algorytmy optymalizacyjne

## Uwagi
- **Niezależność**: każdy wiersz przetwarzany niezależnie
- **Liczba zamian**: jedna zamiana per wiersz
- **Edge case**: min = max (element się nie zmienia)
- **Złożoność**: O(n·m) - każdy element odwiedzany
- **Optymalizacja**: operacja in-place
