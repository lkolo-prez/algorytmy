# Liczenie Elementów Spełniających Warunek - Wyjaśnienie

## Opis
Algorytm liczy, ile elementów tablicy spełnia określony warunek (w tym przypadku A[i] > k). Warunek można modyfikować (>=, <, ==, itp.).

## Dane Wejściowe
- **n**: liczba elementów tablicy (n > 0)
- **A[1..n]**: tablica n liczb
- **k**: wartość warunku do sprawdzenia

## Wynik
**licznik**: ilość elementów spełniających warunek

## Strategia Rozwiązania

### Kroki Algorytmu
1. Wczytaj n i k
2. Wczytaj n elementów do tablicy A
3. Zainicjalizuj `licznik ← 0`
4. Przeglądaj całą tablicę
5. Dla każdego elementu sprawdź warunek (A[i] > k)
6. Jeśli warunek jest spełniony, zwiększ licznik
7. Wypisz wynik

## Przykład

### Dane Wejściowe
```
n = 7
k = 15
A = [10, 20, 5, 25, 15, 30, 8]
```

### Przebieg Algorytmu
| i | A[i] | A[i] > 15? | licznik |
|---|------|-----------|---------|
| 1 | 10 | nie | 0 |
| 2 | 20 | tak | 1 |
| 3 | 5 | nie | 1 |
| 4 | 25 | tak | 2 |
| 5 | 15 | nie | 2 |
| 6 | 30 | tak | 3 |
| 7 | 8 | nie | 3 |

### Wynik
```
Liczba elementów > 15 wynosi: 3
```

## Zastosowania
- Filtrowanie danych
- Sprawdzanie warunków na zbiorach
- Statystyka (ile elementów poniżej średniej)
- Walidacja danych
- Liczenie anomalii w danych

## Uwagi
- **Modyfikowalny warunek**: algorytm pracuje dla dowolnego warunku
- **Możliwe warunki**: >, <, >=, <=, ==, != lub kombinacje (and, or)
- **Przykład wariantu**: zliczanie liczb parzystych `if (A[i] mod 2 = 0)`
- **Optymalizacja**: można zatrzymać wcześniej, jeśli licznik osiągnie limit
