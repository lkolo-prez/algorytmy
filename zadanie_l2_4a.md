# LISTA 2 - ZADANIE 4a
## Tablica n×n z przekątną = 0

### Opis
Wypełnić tablicę n×n kolejnymi liczbami naturalnymi od 1 do n², a następnie ustawić wszystkie elementy na przekątnej głównej (A[i,i]) na 0.

### Wyjaśnienie
1. Wczytaj rozmiar tablicy n
2. Zainicjalizuj licznik: `licz ← 0`
3. Przejdź po całej tablicy w porządku wiersz po wierszu
4. Każdej pozycji przypisz kolejną liczbę: `A[w,k] ← ++licz`
5. Po całkowitym wypełnieniu, przejdź po przekątni i ustaw wszystkie `A[i,i] ← 0`

### Pseudokod

```
algorithm TablicaPrzekatnaZero(A, n)
  read(n)
  
  licz ← 0
  for w ← 1 to n do
    for k ← 1 to n do
      licz ← licz + 1
      A[w,k] ← licz
    end for
  end for
  
  for i ← 1 to n do
    A[i,i] ← 0
  end for
  
end algorithm
```

### Potencjalne problemy logiczne

1. **Źle iterowana przekątna**
   - Problem: `A[i,i+1]` lub `A[i+1,i]` lub `A[i-1,i-1]` dałyby złe pozycje
   - Rozwiązanie: Zawsze dokładnie `A[i,i]` dla głównej przekątni

2. **Niezresetowany licznik**
   - Problem: Jeśli `licz` nie będzie resetować w ramach każdego wiersza
   - Rozwiązanie: Licznik musi być stale rosnący dla całej tablicy

3. **Zła inicjalizacja licznika**
   - Problem: `licz ← 1` zamiast `licz ← 0` spowoduje liczby od 2
   - Rozwiązanie: Zawsze `licz ← 0` przed pętlami, inkrementować na starcie

4. **Indeksowanie od 0**
   - Problem: W niektórych językach tablice zaczynają się od 0
   - Rozwiązanie: Pseudokod zakłada indeksowanie od 1

5. **Overwriting zamiast ustawiania na 0**
   - Problem: Zapomnienie kroku z `A[i,i] ← 0`
   - Rozwiązanie: Zawsze mieć drugą pętlę dla przekątni

### Przykład 1

**Dane:** n = 3

**Krok 1 - Wypełnianie kolejnymi liczbami:**
```
1  2  3
4  5  6
7  8  9
```

**Krok 2 - Ustawianie przekątni na 0:**
```
Przekątna główna: (1,1)=1, (2,2)=5, (3,3)=9
```

**Wynik:**
```
0  2  3
4  0  6
7  8  0
```

---

### Przykład 2

**Dane:** n = 4

**Krok 1:**
```
1   2   3   4
5   6   7   8
9  10  11  12
13 14  15  16
```

**Krok 2 - Zerowanie przekątni (1,1), (2,2), (3,3), (4,4):**

**Wynik:**
```
0   2   3   4
5   0   7   8
9  10   0  12
13 14  15   0
```

---

### Przykład 3

**Dane:** n = 2

**Krok 1:**
```
1  2
3  4
```

**Krok 2:**
```
0  2
3  0
```

---

### Przykład 4

**Dane:** n = 1

**Krok 1:**
```
1
```

**Krok 2:**
```
0
```

---

### Złożoność

- **Czasowa: O(n²)** - przchodzimy całą tablicę n² razy (n²+n operacji)
- **Pamięciowa: O(n²)** - przechowujemy tablicę n×n

### Struktura tablicy

**Liczby zaraz:**
```
1      2      3     ...    n
n+1    n+2    n+3   ...   2n
...
(n-1)n+1 (n-1)n+2 ... n²
```

**Przekątna główna:**
- Pozycje: (1,1), (2,2), (3,3), ..., (n,n)
- Wartości przed modyfikacją: 1, n+2, 2n+3, ..., n²

### Uwagi

- To zadanie łączy dwie operacje: wypełnianie i modyfikację
- Przekątna główna zawsze ma n elementów niezależnie od n
- Przekątna poboczna (A[i,n+1-i]) byłaby innym zadaniem
