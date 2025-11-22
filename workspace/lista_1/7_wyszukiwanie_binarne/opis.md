# Wyszukiwanie Binarne - Wyjaśnienie

## Opis
Wyszukiwanie binarne to efektywny algorytm wyszukiwania, który wymaga, aby tablica była posortowana. Polega na dzieleniu przedziału poszukiwań na połowy i eliminowaniu połowy, w której szukana wartość nie może być.

## Dane Wejściowe
- **n**: liczba elementów tablicy (n > 0)
- **A[1..n]**: tablica n liczb (MUSI BYĆ POSORTOWANA rosnąco)
- **x**: szukana wartość

## Wynik
- **pozycja**: indeks znalezionego elementu (lub -1 jeśli nie znaleziono)

## Strategia Rozwiązania

### Kroki Algorytmu
1. Wczytaj n, x i posortowaną tablicę A
2. Zainicjalizuj `lewo ← 1`, `prawo ← n`
3. Dopóki `lewo <= prawo`:
   - Oblicz środek: `srodek ← (lewo + prawo) div 2`
   - Jeśli A[srodek] = x, znaleziono! Zwróć srodek
   - Jeśli A[srodek] < x, szukaj w prawej połowie: `lewo ← srodek + 1`
   - Jeśli A[srodek] > x, szukaj w lewej połowie: `prawo ← srodek - 1`
4. Wypisz wynik

## Przykład

### Dane Wejściowe
```
n = 8
x = 25
A = [5, 10, 15, 20, 25, 30, 35, 40]  (posortowana!)
```

### Przebieg Algorytmu
| Iteracja | lewo | prawo | srodek | A[srodek] | Akcja |
|----------|------|-------|--------|-----------|-------|
| 1 | 1 | 8 | 4 | 20 | 20 < 25, lewo = 5 |
| 2 | 5 | 8 | 6 | 30 | 30 > 25, prawo = 5 |
| 3 | 5 | 5 | 5 | 25 | 25 = 25, znaleziono! |

### Wynik
```
Element znaleziony na pozycji: 5
```

## Zastosowania
- Wyszukiwanie w dużych, posortowanych zbiorach
- Bazy danych (indeksy)
- Słowniki
- Szukanie granic w zbiorze

## Uwagi
- **Wymóg**: tablica MUSI być posortowana!
- **Złożoność**: O(log n) - mnogo szybsze niż liniowe dla dużych danych
- **Przykład**: dla n=1.000.000, max 20 iteracji vs 500.000 średnio w liniowym
- **Optymalizacja**: interpolacyjne wyszukiwanie dla równomiernie rozłożonych danych
- **Duplikaty**: zwraca jedno z pozycji, nie zawsze pierwszą
