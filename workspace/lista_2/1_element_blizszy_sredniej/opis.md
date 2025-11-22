# Element Najbliższy Średniej - Wyjaśnienie

## Opis
Algorytm znajduje element tablicy, który ma najmniejszą różnicę (w wartości bezwzględnej) od średniej arytmetycznej wszystkich elementów. Użyteczny w analizie anomalii i reprezentatywności danych.

## Dane Wejściowe
- **n**: liczba elementów tablicy (n > 0)
- **A[1..n]**: tablica n liczb

## Wynik
**indeks, A[indeks]**: pozycja i wartość elementu najbliższego średniej

## Strategia Rozwiązania

### Kroki Algorytmu
1. Wczytaj n i elementy tablicy
2. Oblicz średnią: `srednia ← suma / n`
3. Dla każdego elementu oblicz różnicę: `roznica ← |A[i] - srednia|`
4. Śledź element z najmniejszą różnicą
5. Zwróć ten element

## Przykład

### Dane Wejściowe
```
n = 5
A = [10, 20, 30, 40, 50]
```

### Przebieg Algorytmu
- Suma = 150
- Średnia = 150 / 5 = 30

| i | A[i] | Różnica |A[i] - 30| | Czy mniejsza? |
|---|------|---|---|---|
| 1 | 10 | |10-30| = 20 | początkowa |
| 2 | 20 | |20-30| = 10 | tak, nowe min |
| 3 | 30 | |30-30| = 0 | tak, nowe min |
| 4 | 40 | |40-30| = 10 | nie |
| 5 | 50 | |50-30| = 20 | nie |

### Wynik
```
Element najbliższy średniej: 30 na pozycji: 3
```

## Zastosowania
- Wyszukiwanie reprezentatywnego elementu
- Analiza odchyleń od średniej
- Detekcja anomalii
- Statystyka opisowa
- Wybór mediana (przybliżenie)

## Uwagi
- **Średnia**: obliczana z dokładnością liczbą zmiennoprzecinkową
- **Pierwsze minimum**: jeśli wiele elementów ma taką samą różnicę, zwraca pierwszego
- **Alternatywa**: można szukać elementu najbliższego medianie
- **Złożoność**: O(n) - dwa przejścia przez tablicę
