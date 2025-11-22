# Odwracanie Tablicy - Rekurencyjnie - Wyjaśnienie

## Opis
Algorytm odwraca tablicę usando rekursji. Zamiast pętli, każde wołanie rekurencyjne przetwarza parę elementów z obu końców.

## Dane Wejściowe
- **n**: liczba elementów
- **A[1..n]**: tablica do odwrócenia

## Wynik
**A[1..n]**: tablica z odwróconą kolejnością

## Strategi Rekurencyjna
1. Zamień elementy na pozycjach lewo i prawo
2. Rekursywnie odwróć tablicę od (lewo+1) do (prawo-1)
3. Warunek bazowy: gdy lewo ≥ prawo, koniec

## Przykład
```
A = [1, 2, 3, 4, 5]

Wołanie 1: zamiana A[1] ↔ A[5] → [5, 2, 3, 4, 1], rekursja(2, 4)
Wołanie 2: zamiana A[2] ↔ A[4] → [5, 4, 3, 2, 1], rekursja(3, 3)
Wołanie 3: lewo = prawo = 3, STOP

Wynik: [5, 4, 3, 2, 1]
```

## Zastosowania
- Edukacyjny przykład rekursji
- Przetwarzanie struktur danych
- Algorytmy grafowe (DFS)

## Uwagi
- **Pamięć**: stos rekursji = n/2 poziomów
- **Porównanie z iteracyjnym**: ta sama złożoność, ale elegancka
- **Optymalizacja**: zmień licznik z (n div 2) na mniejszy dla mniejszego stosu
