# Dodawanie Macierzy - Wyjaśnienie

## Opis
Algorytm dodaje dwie macierze o tych samych wymiarach n×m. Wynik C = A + B, gdzie każdy element C[i,j] = A[i,j] + B[i,j]. Macierze muszą mieć identyczne wymiary.

## Dane Wejściowe
- **n**: liczba wierszy
- **m**: liczba kolumn
- **A[1..n][1..m]**: pierwsza macierz n×m liczb
- **B[1..n][1..m]**: druga macierz n×m liczb

## Wynik
**C[1..n][1..m]**: macierz sumy, gdzie C[i,j] = A[i,j] + B[i,j]

## Strategia Rozwiązania

### Kroki Algorytmu
1. Wczytaj n, m
2. Wczytaj macierz A (n×m)
3. Wczytaj macierz B (n×m)
4. Dla każdego elementu (i,j): C[i,j] ← A[i,j] + B[i,j]
5. Wypisz macierz C

### Właściwości Dodawania
- Asocjacyjne: (A + B) + C = A + (B + C)
- Przemienne: A + B = B + A
- Element neutralny: A + 0 = A

## Przykład

### Dane Wejściowe
```
n = 2, m = 3
A = [
  [1, 2, 3],
  [4, 5, 6]
]

B = [
  [7, 8, 9],
  [10, 11, 12]
]
```

### Przebieg Operacji
```
C[1,1] = 1 + 7 = 8
C[1,2] = 2 + 8 = 10
C[1,3] = 3 + 9 = 12
C[2,1] = 4 + 10 = 14
C[2,2] = 5 + 11 = 16
C[2,3] = 6 + 12 = 18

Wynik:
C = [
  [8,  10, 12],
  [14, 16, 18]
]
```

## Zastosowania
- Algebra liniowa
- Grafika komputerowa (transformacje)
- Fizyka (wektory sił)
- Ekonomia (macierze przepływów)
- Przetwarzanie obrazów (operacje na kernelach)

## Uwagi
- **Wymiary**: muszą być identyczne dla obu macierzy
- **Złożoność**: O(n·m) - każdy element raz
- **Pamięć**: można wykonać A ← A + B (zaoszczędzić pamięć na C)
- **Liczby ujemne**: algorytm działa dla dowolnych liczb
- **Błąd**: jeśli wymiary się nie zgadzają
