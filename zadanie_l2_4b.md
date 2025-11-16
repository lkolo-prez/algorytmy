# LISTA 2 - ZADANIE 4b
## Tablica: A[w,k] = k - w

### Opis
Wypełnić tablicę n×n wzorem A[w,k] = k - w, gdzie w to numer wiersza, k to numer kolumny.

### Wyjaśnienie
1. Wczytaj rozmiar n
2. Dla każdej pozycji (w,k) w tablicy oblicz: różnicę (kolumna - wiersz)
3. Rezultat: na przekątni głównej będą zera, nad przekątną liczby dodatnie, pod - ujemne

### Pseudokod

```
algorithm TablicaRoznicaIndeksow(A, n)
  read(n)
  
  for w ← 1 to n do
    for k ← 1 to n do
      A[w,k] ← k - w
    end for
  end for
  
end algorithm
```

### Potencjalne problemy logiczne

1. **Odwrotny wzór**
   - Problem: `A[w,k] ← w - k` da macierz z odwróconym znakiem
   - Rozwiązanie: Zawsze `k - w` zgodnie z zadaniem

2. **Zamieszane indeksy w i k**
   - Problem: `A[k,w] ← k - w` da transponowaną macierz
   - Rozwiązanie: Zewnętrzna pętla po wierszach (w), wewnętrzna po kolumnach (k)

3. **Indeksowanie od 0**
   - Problem: Jeśli tablica zaczyna się od 0, wyniki będą przesunięte
   - Rozwiązanie: Pseudokod zakłada indeksowanie od 1

4. **Dodawanie zamiast odejmowania**
   - Problem: `A[w,k] ← w + k` da zupełnie inny wynik
   - Rozwiązanie: Zawsze dokładnie `k - w`

### Przykład 1

**Dane:** n = 4

**Obliczenia:**

Wiersz 1 (w=1):
- k=1: A[1,1] = 1-1 = 0
- k=2: A[1,2] = 2-1 = 1
- k=3: A[1,3] = 3-1 = 2
- k=4: A[1,4] = 4-1 = 3

Wiersz 2 (w=2):
- k=1: A[2,1] = 1-2 = -1
- k=2: A[2,2] = 2-2 = 0
- k=3: A[2,3] = 3-2 = 1
- k=4: A[2,4] = 4-2 = 2

Wiersz 3 (w=3):
- k=1: A[3,1] = 1-3 = -2
- k=2: A[3,2] = 2-3 = -1
- k=3: A[3,3] = 3-3 = 0
- k=4: A[3,4] = 4-3 = 1

Wiersz 4 (w=4):
- k=1: A[4,1] = 1-4 = -3
- k=2: A[4,2] = 2-4 = -2
- k=3: A[4,3] = 3-4 = -1
- k=4: A[4,4] = 4-4 = 0

**Wynik:**
```
 0   1   2   3
-1   0   1   2
-2  -1   0   1
-3  -2  -1   0
```

---

### Przykład 2

**Dane:** n = 3

**Wynik:**
```
 0   1   2
-1   0   1
-2  -1   0
```

---

### Przykład 3

**Dane:** n = 5

**Wynik:**
```
 0   1   2   3   4
-1   0   1   2   3
-2  -1   0   1   2
-3  -2  -1   0   1
-4  -3  -2  -1   0
```

---

### Właściwości macierzy

1. **Przekątna główna zawsze 0:** A[i,i] = i-i = 0
2. **Macierz antysymetryczna:** A[w,k] = -(A[k,w])
   - Przykład: A[1,2] = 1, A[2,1] = -1
3. **Górny trójkąt dodatni:** Ponad przekątną liczby > 0
4. **Dolny trójkąt ujemny:** Pod przekątną liczby < 0

### Złożoność

- **Czasowa: O(n²)** - przechodzimy każdą pozycję tablicy
- **Pamięciowa: O(n²)** - przechowujemy tablicę n×n

### Zastosowanie

Ta macierz pojawia się w:
- Analizie odległości między indeksami
- Testowaniu operacji na macierzach
- Grafach jako macierz wag względnych
- Algorytmach obsługi macierzy antysymetrycznych

### Uwagi

- To zadanie nie wymaga iteracyjnego procesu, tylko prosty wzór
- Macierz zawsze będzie antysymetryczna niezależnie od n
- Można to zapisać bez pętli w niektórych językach programowania
