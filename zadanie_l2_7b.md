# LISTA 2 - ZADANIE 7b
## Mnożenie dwóch macierzy

### Opis
Pomnożyć macierz A(n×p) przez macierz B(p×m) i otrzymać macierz wynikową C(n×m), gdzie C[w,k] = suma(A[w,s] × B[s,k]) dla s od 1 do p.

### Wyjaśnienie
1. Wczytaj wymiary: n (wiersze A), p (kolumny A = wiersze B), m (kolumny B)
2. Wczytaj macierz A(n×p)
3. Wczytaj macierz B(p×m)
4. Dla każdego wiersza w macierzy A (1 do n):
   - Dla każdej kolumny k macierzy B (1 do m):
     - Oblicz iloczyn skalarny wiersza w-tego z A z kolumną k-tą z B
     - C[w,k] = A[w,1]×B[1,k] + A[w,2]×B[2,k] + ... + A[w,p]×B[p,k]

### Pseudokod

```
algorithm MnozenieceMacierzy(A, B, C, n, p, m)
  read(n, p, m)
  
  // Wczytywanie macierzy A(n×p)
  write("Wczytaj macierz A (n=", n, " wierszy, p=", p, " kolumn):")
  for w ← 1 to n do
    for s ← 1 to p do
      read(A[w,s])
    end for
  end for
  
  // Wczytywanie macierzy B(p×m)
  write("Wczytaj macierz B (p=", p, " wierszy, m=", m, " kolumn):")
  for s ← 1 to p do
    for k ← 1 to m do
      read(B[s,k])
    end for
  end for
  
  // Mnożenie macierzy
  for w ← 1 to n do
    for k ← 1 to m do
      C[w,k] ← 0
      for s ← 1 to p do
        C[w,k] ← C[w,k] + A[w,s] × B[s,k]
      end for
    end for
  end for
  
  // Wypisanie wyniku
  write("Macierz C = A × B (n=", n, " wierszy, m=", m, " kolumn):")
  for w ← 1 to n do
    for k ← 1 to m do
      write(C[w,k], " ")
    end for
    writeln()
  end for
  
end algorithm
```

### Potencjalne problemy logiczne

1. **Błędne wymiary: p A ≠ wiersze B**
   - Problem: A jest 2×3, B jest 2×4 (p=3 ≠ 2)
   - Wynik: Mnożenie nie jest zdefiniowane matematycznie
   - Rozwiązanie: Zawsze `if (p_A = wiersze_B)` przed mnożeniem

2. **Brak inicjalizacji C[w,k] na zero**
   - Problem: `C[w,k] ← A[w,s] × B[s,k]` zamiast `C[w,k] ← 0; for s...`
   - Wynik: Suma będzie sumowała ze śmieciami z pamięci
   - Rozwiązanie: `C[w,k] ← 0` na początku każdej iteracji w,k

3. **Zniesienie pętli po s (wymiar wspólny)**
   - Problem: `C[w,k] ← A[w,1] × B[1,k]` - tylko jeden wyraz zamiast sumy
   - Wynik: Całkowicie błędny wynik - brak sumy po wymiarze wspólnym
   - Rozwiązanie: `for s ← 1 to p do` wewnątrz

4. **Zamiana porządku pętli**
   - Problem: `for k ← 1 to m do for w ← 1 to n do` (zamiast w,k,s)
   - Wynik: Logicznie OK, ale gorsze cache misses
   - Rozwiązanie: Zawsze w-k-s (najczęściej preferowany porządek)

5. **Użycie = zamiast ←**
   - Problem: `C[w,k] = A[w,s] × B[s,k]` (porównanie zamiast przypisania)
   - Wynik: C nie będzie zmieniana, albo błąd składniowy
   - Rozwiązanie: `←` dla przypisania

6. **Złe indeksy w pętli s**
   - Problem: `for s ← 0 to p-1` lub `for s ← 2 to p`
   - Wynik: Pominięcie elementów lub błędy dostępu
   - Rozwiązanie: Dokładnie `for s ← 1 to p`

### Przykład 1

**Dane:**
```
n=2, p=3, m=2

Macierz A(2×3):
1  2  3
4  5  6

Macierz B(3×2):
7  8
9  10
11 12
```

**Obliczenia - wiersz 1, kolumna 1:**
- C[1,1] = A[1,1]×B[1,1] + A[1,2]×B[2,1] + A[1,3]×B[3,1]
- C[1,1] = 1×7 + 2×9 + 3×11 = 7 + 18 + 33 = 58

**Obliczenia - wiersz 1, kolumna 2:**
- C[1,2] = 1×8 + 2×10 + 3×12 = 8 + 20 + 36 = 64

**Obliczenia - wiersz 2:**
- C[2,1] = 4×7 + 5×9 + 6×11 = 28 + 45 + 66 = 139
- C[2,2] = 4×8 + 5×10 + 6×12 = 32 + 50 + 72 = 154

**Wynik C(2×2):**
```
58  64
139 154
```

---

### Przykład 2

**Dane:**
```
n=1, p=4, m=1

Macierz A(1×4):
1 2 3 4

Macierz B(4×1):
2
2
2
2
```

**Obliczenia:**
- C[1,1] = 1×2 + 2×2 + 3×2 + 4×2 = 2+4+6+8 = 20

**Wynik C(1×1):**
```
20
```

---

### Przykład 3

**Dane:**
```
n=2, p=2, m=3

Macierz A(2×2):
1  0
0  1

Macierz B(2×3):
1  2  3
4  5  6
```

**Obliczenia:**
- C[1,1] = 1×1 + 0×4 = 1
- C[1,2] = 1×2 + 0×5 = 2
- C[1,3] = 1×3 + 0×6 = 3
- C[2,1] = 0×1 + 1×4 = 4
- C[2,2] = 0×2 + 1×5 = 5
- C[2,3] = 0×3 + 1×6 = 6

**Wynik C(2×3):**
```
1  2  3
4  5  6
```

(A jest macierzą tożsamości I, więc I×B = B)

---

### Przykład 4

**Dane:**
```
n=3, p=1, m=1

Macierz A(3×1):
1
2
3

Macierz B(1×1):
5
```

**Wynik C(3×1):**
```
5
10
15
```

---

### Złożoność

- **Czasowa: O(n × m × p)** - trzy zagnieżdżone pętle
  - Dla macierzy kwadratowych n×n: **O(n³)**
  - Asymptotycznie takie same jak pętle for-for-for
- **Pamięciowa: O(n×p + p×m + n×m)** - przechowywanie trzech macierzy
  - Dla macierzy kwadratowych: **O(n²)**

### Algorytmy szybszego mnożenia

| Algorytm | Złożoność | Uwagi |
|----------|-----------|-------|
| Naiwny (podwójna pętla) | O(n³) | Standardowy |
| Strassen | O(n^2.807) | Dziel i zwyciężaj |
| Coppersmith-Winograd | O(n^2.373) | Zaawansowany |

### Właściwości mnożenia macierzy

1. **Nie jest przemienne:** A×B ≠ B×A (w ogólności)
2. **Jest łączne:** (A×B)×C = A×(B×C)
3. **Rozdzielność względem dodawania:** A×(B+C) = A×B + A×C
4. **Element neutralny:** A×I = A (I - macierz tożsamości)

### Uwagi

- Mnożenie macierzy to kubiczna O(n³) dla dużych macierzy
- Dla praktycznych problemów szukamy algorytmów szybszych (Strassen)
- Kolejność pętli wpływa na wydajność ze względu na cache
- Można zoptymalizować poprzez transpozycję B (lepszy dostęp do pamięci)

### Zastosowanie

- Algebra liniowa i systemy równań liniowych
- Transformacje geometryczne w grafice 3D
- Metoda najmniejszych kwadratów (regresja)
- Sieci neuronowe (mnożenie macierzy wag)
- Teoria grafów (macierze sąsiedztwa)
- Krytografia (operacje na macierzach)
