# K-ty Co do Wielkości Element - Wyjaśnienie

## Opis
Algorytm znajduje k-ty co do wielkości element w tablicy, gdzie k=1 to najmniejszy, k=n to największy. Wykorzystuje sortowanie bąbelkowe, a potem zwraca element na k-tej pozycji.

## Dane Wejściowe
- **n**: liczba elementów tablicy (n > 0)
- **A[1..n]**: tablica n liczb
- **k**: pozycja szukanego elementu (1 ≤ k ≤ n)

## Wynik
**A[k]**: k-ty co do wielkości element (po sortowaniu rosnącym)

## Strategia Rozwiązania

### Kroki Algorytmu
1. Wczytaj n, k i elementy tablicy
2. Posortuj tablicę rosnąco (bąbelkowe)
3. Zwróć element na pozycji k

## Przykład

### Dane Wejściowe
```
n = 6
k = 3
A = [15, 3, 25, 7, 30, 8]
```

### Przebieg Algorytmu
- Sortowanie: [3, 7, 8, 15, 25, 30]
- k-ty (3-cim) element to: 8

### Wynik
```
K-ty element (k=3): 8
```

## Zastosowania
- Statystyka (percentyle, mediana)
- Szukanie środkowego elementu (mediana)
- Analiza danych
- Szukanie outliers (1-ty i n-ty element)

## Uwagi
- **Mediana**: dla n parzystego średnia A[n/2] i A[n/2+1], dla nieparzystego A[(n+1)/2]
- **Optymalizacja**: QuickSelect - O(n) średnio zamiast O(n log n)
- **k=1**: najmniejszy element
- **k=n**: największy element
- **Duplikaty**: funkcja zwraca dowolny z równych elementów na k-tej pozycji
