# Tablica: A[i,j] = j - i - Wyjaśnienie

## Opis
Algorytm tworzy macierz n×n, gdzie każdy element A[i,j] jest równy j - i. Macierz jest generowana bez wczytywania, tylko na podstawie pozycji elementu.

## Dane Wejściowe
- **n**: wymiar macierzy (n×n)

## Wynik
**A[1..n][1..n]**: macierz gdzie A[i,j] = j - i

## Strategia Rozwiązania

### Kroki Algorytmu
1. Wczytaj wymiar n
2. Dla każdej pozycji (i,j) ustaw A[i,j] ← j - i
3. Wypisz macierz

### Właściwości
- Główna przekątna zawsze 0 (j - i = 0 gdy i = j)
- Powyżej przekątnej wartości dodatnie
- Poniżej przekątnej wartości ujemne
- Symetria: A[i,j] = -A[j,i]

## Przykład

### Dane Wejściowe
```
n = 4
```

### Przebieg Algorytmu
- A[1,1] = 1-1 = 0
- A[1,2] = 2-1 = 1
- A[1,3] = 3-1 = 2
- A[2,1] = 1-2 = -1
- A[2,2] = 2-2 = 0
- ...

### Wynik
```
[
  [0,  1,  2,  3],
  [-1, 0,  1,  2],
  [-2, -1, 0,  1],
  [-3, -2, -1, 0]
]
```

## Zastosowania
- Testowanie algorytmów macierzowych
- Generowanie macierzy bez I/O
- Macierze różnic
- Badanie symetrii macierzy
- Algorytmy strukturalne

## Uwagi
- **Brak wczytywania**: wszystkie wartości generowane ze wzoru
- **Szybkość**: O(n²) wypisywania, ale nie trzeba czytać danych
- **Wzór**: prosty do zapamiętania i implementacji
- **Właściwości**: antisymetryczna (A^T = -A)
