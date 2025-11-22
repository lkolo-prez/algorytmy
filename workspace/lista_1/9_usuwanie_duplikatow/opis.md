# Usuwanie Duplikatów - Wyjaśnienie

## Opis
Algorytm usuwa zduplikowane elementy z tablicy. Każdy unikalny element pojawia się w wynikowej tablicy tylko raz. Elementy pojawiają się w kolejności pierwszego występienia.

## Dane Wejściowe
- **n**: liczba elementów tablicy (n ≥ 1)
- **A[1..n]**: tablica n liczb (mogą być duplikaty)

## Wynik
**A[1..licznik]**: tablica z unikalnymi elementami, licznik = liczba unikalnych elementów

## Strategia Rozwiązania

### Kroki Algorytmu
1. Wczytaj n i elementy tablicy A
2. Zainicjalizuj `licznik ← 1` (pierwszy element zawsze unikalny)
3. Dla każdego elementu od 2 do n:
   - Sprawdź czy jest w już przetworzonej części (od 1 do licznik)
   - Jeśli nie jest, dodaj go na pozycję licznik+1 i zwiększ licznik
4. Wypisz pierwsze licznik elementów

## Przykład

### Dane Wejściowe
```
n = 8
A = [5, 3, 5, 7, 3, 9, 5, 7]
```

### Przebieg Algorytmu
| i | A[i] | Czy duplikat? | Akcja | licznik | Tablica |
|---|------|---|---|---|---|
| Start | - | - | - | 1 | [5, ...] |
| 2 | 3 | nie | dodaj | 2 | [5, 3, ...] |
| 3 | 5 | tak | pomiń | 2 | [5, 3, ...] |
| 4 | 7 | nie | dodaj | 3 | [5, 3, 7, ...] |
| 5 | 3 | tak | pomiń | 3 | [5, 3, 7, ...] |
| 6 | 9 | nie | dodaj | 4 | [5, 3, 7, 9, ...] |
| 7 | 5 | tak | pomiń | 4 | [5, 3, 7, 9, ...] |
| 8 | 7 | tak | pomiń | 4 | [5, 3, 7, 9, ...] |

### Wynik
```
[5, 3, 7, 9]  (4 elementy unikalne)
```

## Zastosowania
- Czyszczenie danych
- Analiza zbiorów danych
- Generowanie listy unikalnych wartości
- Usuwanie duplikatów z logów
- Deduplikacja baz danych

## Uwagi
- **Złożoność**: O(n²) - dla każdego elementu sprawdzamy wszystkie poprzednie
- **Optymalizacja**: użyć zbioru/hasha dla O(n) średnio
- **Kolejność**: zachowuje kolejność pierwszych występień
- **Alternatywa**: sortowanie → usuwanie sąsiednich duplikatów O(n log n)
- **Edge case**: tablica bez duplikatów → licznik = n
