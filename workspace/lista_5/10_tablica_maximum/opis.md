````markdown
# Maximum w Tablicy - Dziel i Zwyciężaj - Wyjaśnienie

## Opis
Znajdowanie maksimum przy użyciu paradygmatu "dziel i zwyciężaj". Zamiast liniowego przejścia, rekurencyjnie dzielimy tablicę na połowy, znajdujemy maksimum w każdej połowie, i zwracamy większe z nich.

## Strategia (Divide and Conquer)

### 1. DZIEL (Divide)
Podziel tablicę na dwie (mniej więcej) równe części.

### 2. ZWYCIĘŻAJ (Conquer)
Rekurencyjnie znajdź maksimum w każdej połowie.

### 3. POŁĄCZ (Combine)
Zwróć większe z dwóch maksimów.

### Przypadki bazowe
- Jeden element: A[lewy] jest maksimum
- Dwa elementy: max(A[lewy], A[prawy])

## Rekurencja
```
T(n) = 2T(n/2) + O(1)
```

Przez Master Theorem:
```
T(n) = O(n)
```

## Złożoność
- **Czasowa**: O(n) - każdy element odwiedzony raz
- **Pamięciowa**: O(log n) - głębokość rekursji

## Porównanie z podejściem liniowym

| Podejście | Czas | Pamięć | Porównania |
|-----------|------|--------|------------|
| Liniowe | O(n) | O(1) | n-1 |
| Dziel i zwyciężaj | O(n) | O(log n) | n-1 |

**Wniosek**: Oba O(n), ale liniowe ma O(1) pamięć - **lepsze**!

## Dlaczego więc uczymy dziel i zwyciężaj?
1. **Edukacja**: Wprowadzenie do paradygmatu
2. **Paralelizacja**: Łatwo zrównoleglić (oba podproblemy niezależne)
3. **Fundament**: Dla bardziej złożonych problemów gdzie dziel i zwyciężaj wygrywa

## Przykład działania
```
A = [3, 7, 2, 9, 1, 5]

                [3,7,2,9,1,5]
               /              \
          [3,7,2]            [9,1,5]
          /    \             /    \
       [3,7]  [2]         [9,1]  [5]
       / \                / \
     [3] [7]            [9] [1]
      ↓   ↓              ↓   ↓
      3   7              9   1
       \  /               \  /
        7                  9
         \                /
          \              /
           \            /
            \          /
             \        /
              \      /
                 9
```

## Liczba porównań
Dla n elementów:
```
C(n) = 2C(n/2) + 1
C(1) = 0

Rozwiązanie: C(n) = n - 1
```

Tyle samo co liniowe!

## Zastosowania praktyczne dziel i zwyciężaj
- **Merge Sort**: O(n log n) vs O(n²) prostych
- **Quick Sort**: średnio O(n log n)
- **Wyszukiwanie binarne**: O(log n) vs O(n)
- **Mnożenie macierzy**: Strassen O(n^2.807) vs O(n³)
- **FFT**: O(n log n) vs O(n²)

## Wersja równoległa
```pseudocode
algorithm ParallelMax(A, lewy, prawy) {
  if lewy == prawy then return A[lewy]
  
  srodek ← (lewy + prawy) / 2
  
  // Równolegle:
  max_lewy  ← PARALLEL ParallelMax(A, lewy, srodek)
  max_prawy ← PARALLEL ParallelMax(A, srodek+1, prawy)
  
  return max(max_lewy, max_prawy)
}
```

**Złożoność równoległa**: O(log n) czas przy n procesorach!

## Ciekawostki
1. **Optimum**: Algorytm Blum-Floyd-Pratt-Rivest-Tarjan znajduje min/max z ⌈3n/2⌉ porównań (lepiej niż n-1)
2. **Tournament method**: Podobne drzewo jak dziel i zwyciężaj
3. **SIMD**: Dziel i zwyciężaj naturalnie dla instrukcji wektorowych

````
