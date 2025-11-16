# LISTA 2 - ZADANIE 7a
## Dodawanie dwóch macierzy

### Opis
Dodać dwie macierze A(n×m) i B(n×m) i otrzymać macierz wynikową C(n×m), gdzie C[w,k] = A[w,k] + B[w,k].

### Wyjaśnienie
1. Wczytaj wymiary n i m (obie macierze mają te same wymiary)
2. Wczytaj macierz A
3. Wczytaj macierz B
4. Dla każdego wiersza w (1 do n):
   - Dla każdej kolumny k (1 do m):
     - Oblicz: C[w,k] = A[w,k] + B[w,k]
5. Wypisz macierz C

### Pseudokod

```
algorithm DodawanieMacierzy(A, B, C, n, m)
  read(n, m)
  
  // Wczytywanie macierzy A
  write("Wczytaj macierz A:")
  for w ← 1 to n do
    for k ← 1 to m do
      read(A[w,k])
    end for
  end for
  
  // Wczytywanie macierzy B
  write("Wczytaj macierz B:")
  for w ← 1 to n do
    for k ← 1 to m do
      read(B[w,k])
    end for
  end for
  
  // Dodawanie macierzy
  for w ← 1 to n do
    for k ← 1 to m do
      C[w,k] ← A[w,k] + B[w,k]
    end for
  end for
  
  // Wypisanie wyniku
  write("Macierz C = A + B:")
  for w ← 1 to n do
    for k ← 1 to m do
      write(C[w,k], " ")
    end for
    writeln()
  end for
  
end algorithm
```

### Potencjalne problemy logiczne

1. **Macierze o różnych wymiarach**
   - Problem: A(2×3) + B(3×2) nie jest zdefiniowane
   - Wynik: Błędne wyniki lub błąd dostępu do pamięci
   - Rozwiązanie: Zawsze `if (n_A = n_B AND m_A = m_B)` przed dodawaniem

2. **Dodawanie zamiast kopiowania**
   - Problem: `C[w,k] ← A[w,k]` zamiast `A[w,k] + B[w,k]`
   - Wynik: C będzie kopią A, bez wpływu B
   - Rozwiązanie: Zawsze `C[w,k] ← A[w,k] + B[w,k]`

3. **Błędny operator - odejmowanie zamiast dodawania**
   - Problem: `C[w,k] ← A[w,k] - B[w,k]`
   - Wynik: Będzie odejmowanie, a nie dodawanie
   - Rozwiązanie: Dokładnie `+` dla dodawania

4. **Zły zakres pętli**
   - Problem: `for w ← 1 to m` i `for k ← 1 to n`
   - Wynik: Zamieszanie wymiarów, błąd dostępu
   - Rozwiązanie: Zawsze `for w ← 1 to n` (wiersze), `for k ← 1 to m` (kolumny)

5. **Wczytywanie obu macierzy do A**
   - Problem: `read(A[w,k])` dla obu macierzy
   - Wynik: B nie będzie zawierać danych, tylko stare wartości
   - Rozwiązanie: Różne macierze: `read(A[w,k])`, `read(B[w,k])`

6. **Brak walidacji zakresu indeksów**
   - Problem: n lub m poza rozumnym zakresem (np. n = -5)
   - Wynik: Błedy pamięci
   - Rozwiązanie: `if (n > 0 AND m > 0)` na początku

### Przykład 1

**Dane:**
```
n=2, m=3

Macierz A:
1  2  3
4  5  6

Macierz B:
7  8  9
10 11 12
```

**Obliczenia:**

Wiersz 1:
- C[1,1] = 1 + 7 = 8
- C[1,2] = 2 + 8 = 10
- C[1,3] = 3 + 9 = 12

Wiersz 2:
- C[2,1] = 4 + 10 = 14
- C[2,2] = 5 + 11 = 16
- C[2,3] = 6 + 12 = 18

**Wynik:**
```
8  10  12
14 16  18
```

---

### Przykład 2

**Dane:**
```
n=3, m=2

Macierz A:
1  2
3  4
5  6

Macierz B:
-1  -2
-3  -4
-5  -6
```

**Wynik:**
```
0  0
0  0
0  0
```

---

### Przykład 3

**Dane:**
```
n=2, m=2

Macierz A:
1  -2
3   4

Macierz B:
-1  2
-3  -4
```

**Wynik:**
```
0  0
0  0
```

---

### Przykład 4

**Dane:**
```
n=1, m=4

Macierz A:
1  2  3  4

Macierz B:
5  6  7  8
```

**Wynik:**
```
6  8  10  12
```

---

### Złożoność

- **Czasowa: O(n×m)** - dwie pętle zagnieżdżone, każda operacja dodawania to O(1)
- **Pamięciowa: O(n×m)** - trzy macierze: A, B, C każda n×m

### Właściwości dodawania macierzy

1. **Przemienność:** A + B = B + A
2. **Łączność:** (A + B) + C = A + (B + C)
3. **Element neutralny:** A + O = A (gdzie O to macierz zerowa)
4. **Element odwrotny:** A + (-A) = O

### Warianty

1. **Dodawanie in-place:** C ← A, następnie C[w,k] += B[w,k]
2. **Dodawanie skalarów:** Każdy element + stała
3. **Macierze blokowe:** Dzielenie na podmacierze, dodawanie blokami
4. **Dodawanie rozmaitych wymiarów:** Broadcasting (jak w NumPy)

### Uwagi

- Dodawanie to operacja element-by-element
- Wymiary muszą być identyczne
- Operacja jest bardzo efektywna - linearnie względem liczby elementów
- Możliwe przechowywanie wyniku w jednej z macierzy wejściowych

### Zastosowanie

- Algebra liniowa
- Systemy równań liniowych
- Fizyka - dodawanie wektorów w postaci macierzy
- Grafika komputerowa - transformacje koloru
- Przetwarzanie obrazów - mieszanie warstw
