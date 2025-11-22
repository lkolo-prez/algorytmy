# Minimum i Maksimum - Wyjaśnienie

## Opis
Algorytm znajduje minimalny i maksymalny element w tablicy. Oba elementy są wyszukiwane w jednym przejściu tablicy.

## Dane Wejściowe
- **n**: liczba elementów tablicy (n ≥ 1)
- **A[1..n]**: tablica n liczb

## Wynik
- **min**: najmniejszy element w tablicy
- **max**: największy element w tablicy

## Strategia Rozwiązania

### Kroki Algorytmu
1. Wczytaj liczbę elementów n
2. Wczytaj n elementów do tablicy A
3. Zainicjalizuj `min ← A[1]` i `max ← A[1]` (pierwszy element)
4. Przeglądaj tablicę od 2 elementu do n
5. Dla każdego elementu:
   - Jeśli jest mniejszy od min, zaktualizuj min
   - Jeśli jest większy od max, zaktualizuj max
6. Wypisz wyniki

## Przykład

### Dane Wejściowe
```
n = 6
A = [15, 3, 25, 7, 30, 8]
```

### Przebieg Algorytmu
| i | A[i] | min | max |
|---|------|-----|-----|
| Start | - | 15 | 15 |
| 2 | 3 | 3 | 15 |
| 3 | 25 | 3 | 25 |
| 4 | 7 | 3 | 25 |
| 5 | 30 | 3 | **30** |
| 6 | 8 | 3 | 30 |

### Wynik
```
Minimum = 3, Maksimum = 30
```

## Zastosowania
- Normalizacja danych
- Statystyka opisowa
- Walidacja danych
- Algorytmy sortujące
- Analiza zakresu wartości

## Uwagi
- **Efektywność**: oba elementy znalezione w jednym przejściu O(n)
- **Alternatywa**: można użyć dwóch osobnych pętli (ale mniej efektywnie)
- **Edge case**: tablica jednoelementowa → min = max
- **Optymalizacja**: dla par elementów można zredukować do 1.5n porównań zamiast 2n
