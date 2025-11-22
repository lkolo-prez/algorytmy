# Mnożenie Macierzy - Wyjaśnienie

## Opis
Algorytm mnoży dwie macierze: A (n×m) i B (m×k), tworząc wynik C (n×k). Iloczyn C[i,j] jest sumą iloczynów i-tego wiersza A z j-tą kolumną B.

## Dane Wejściowe
- **n**: liczba wierszy macierzy A
- **m**: liczba kolumn macierzy A = liczba wierszy macierzy B
- **k**: liczba kolumn macierzy B
- **A[1..n][1..m]**: macierz n×m
- **B[1..m][1..k]**: macierz m×k

## Wynik
**C[1..n][1..k]**: macierz iloczynu, gdzie C[i,j] = Σ(A[i,l] * B[l,j])

## Strategia Rozwiązania

### Kroki Algorytmu
1. Wczytaj wymiary n, m, k
2. Wczytaj macierz A (n×m)
3. Wczytaj macierz B (m×k)
4. Dla każdego elementu C[i,j]:
   - Oblicz sumę iloczynów: Σ(A[i,l] * B[l,j]) dla l od 1 do m
5. Wypisz macierz C

### Warunek Mnożliwości
- Liczba kolumn A = Liczba wierszy B
- Wymiar wyniku: (n × m) × (m × k) = (n × k)

## Przykład

### Dane Wejściowe
```
n = 2, m = 3, k = 2
A = [
  [1, 2, 3],
  [4, 5, 6]
]

B = [
  [7, 8],
  [9, 10],
  [11, 12]
]
```

### Przebieg Mnożenia
```
C[1,1] = 1·7 + 2·9 + 3·11 = 7 + 18 + 33 = 58
C[1,2] = 1·8 + 2·10 + 3·12 = 8 + 20 + 36 = 64
C[2,1] = 4·7 + 5·9 + 6·11 = 28 + 45 + 66 = 139
C[2,2] = 4·8 + 5·10 + 6·12 = 32 + 50 + 72 = 154

Wynik:
C = [
  [58,  64],
  [139, 154]
]
```

## Zastosowania
- Algebra liniowa
- Grafika 3D (transformacje)
- Sztuczna inteligencja (sieci neuronowe)
- Systemy równań liniowych
- Kodowanie/dekodowanie
- Przetwarzanie sygnałów

## Uwagi
- **Warunek**: kolumny A = wiersze B
- **Nie przemienne**: A·B ≠ B·A (zwykle)
- **Złożoność**: O(n·m·k) - triple loop
- **Optymalizacja**: algorytm Strasassena O(n^2.807)
- **Wymiar wyniku**: (liczba wierszy A) × (liczba kolumn B)
