# Tablica z Przekątną = 0 - Wyjaśnienie

## Opis
Algorytm zeruje główną przekątną macierzy kwadratowej (elementy gdzie i = j). Wczytuje macierz n×n, ustawia elementy A[i,i] = 0, i wypisuje wynik.

## Dane Wejściowe
- **n**: wymiar macierzy (n×n)
- **A[1..n][1..n]**: macierz kwadratowa

## Wynik
**A[1..n][1..n]**: macierz z wyzerotaną główną przekątną

## Strategia Rozwiązania

### Kroki Algorytmu
1. Wczytaj wymiar n
2. Wczytaj macierz n×n
3. Dla każdego i od 1 do n: A[i,i] ← 0
4. Wypisz zmodyfikowaną macierz

### Główna Przekątna
Elementy gdzie nr wiersza = nr kolumny: A[1,1], A[2,2], A[3,3], ...

## Przykład

### Dane Wejściowe
```
n = 3
A = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
```

### Przebieg Algorytmu
- Ustaw A[1,1] ← 0 (było 1)
- Ustaw A[2,2] ← 0 (było 5)
- Ustaw A[3,3] ← 0 (było 9)

### Wynik
```
[
  [0, 2, 3],
  [4, 0, 6],
  [7, 8, 0]
]
```

## Zastosowania
- Przetwarzanie macierzy
- Eliminacja Gaussa (przygotowanie)
- Operacje algebraiczne na macierzach
- Grafy (usunięcie pętli zwrotnych)

## Uwagi
- **Główna przekątna**: A[i,i] dla i = 1 do n
- **Poboczna przekątna**: A[i, n-i+1]
- **Liczba zmian**: dokładnie n elementów
- **Odwracalność**: operacja jest odwracalna (zachowujemy wartości)
