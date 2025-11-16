# LISTA 2 - ZADANIE 6b
## Zamiana dwóch wierszy macierzy

### Opis
Zamienić zawartość dwóch wskazanych wierszy macierzy n×m. Najpierw przeczytać macierz, następnie podać numery dwóch wierszy do zamiany, a na koniec wypisać zmienioną macierz.

### Wyjaśnienie
1. Wczytaj wymiary: n i m
2. Wczytaj macierz A[n,m]
3. Wczytaj numery wierszy do zamiany: w1 i w2
4. Dla każdej kolumny k=1 do m:
   - Zamień A[w1, k] z A[w2, k] używając zmiennej tymczasowej
5. Wypisz zmienioną macierz

### Pseudokod

```
algorithm ZamianaDwochWierszy(A, n, m)
  read(n, m)
  
  // Wczytywanie macierzy
  for w ← 1 to n do
    for k ← 1 to m do
      read(A[w,k])
    end for
  end for
  
  // Wczytywanie numerów wierszy
  read(w1, w2)
  
  // Zamiana dwóch wierszy
  for k ← 1 to m do
    temp ← A[w1,k]
    A[w1,k] ← A[w2,k]
    A[w2,k] ← temp
  end for
  
  // Wypisanie wyniku
  for w ← 1 to n do
    for k ← 1 to m do
      write(A[w,k], " ")
    end for
    writeln()
  end for
  
end algorithm
```

### Potencjalne problemy logiczne

1. **Zamiana bez zmiennej tymczasowej**
   - Problem: `A[w1,k] ← A[w2,k]` i `A[w2,k] ← A[w1,k]` bez temp
   - Wynik: Oba pola będą zawierać wartość z w2
   - Rozwiązanie: Zawsze użyć `temp` do przechowywania starej wartości

2. **Zamienianie kolumn zamiast wierszy**
   - Problem: `temp ← A[k,w1]` zamiast `A[w1,k]`
   - Wynik: Zamienią się kolumny zamiast wierszy
   - Rozwiązanie: Zawsze indeks wiersza (w1, w2) na pierwszej pozycji

3. **Brak pętli po kolumnach**
   - Problem: Zamiana tylko `A[w1,1]` z `A[w2,1]`
   - Wynik: Tylko pierwszy element każdego wiersza się zamieni
   - Rozwiązanie: Pętla `for k ← 1 to m`

4. **Zły zakres pętli**
   - Problem: `for k ← 1 to n` zamiast `to m`
   - Wynik: Jeśli m < n, będą błędy; jeśli m > n, część się nie zmieni
   - Rozwiązanie: Zawsze `for k ← 1 to m` dla wierszy

5. **Indeksy poza zakresem**
   - Problem: w1 = 0 lub w2 > n
   - Wynik: Dostęp do pamięci poza macierzą
   - Rozwiązanie: Walidacja: `if (w1 >= 1 AND w1 <= n AND w2 >= 1 AND w2 <= n)`

6. **Zamiana wiersza z samym sobą**
   - Problem: w1 = w2 = 3
   - Wynik: Wiersz pozostaje niezmieniony (logicznie OK)
   - Rozwiązanie: Poprawne zachowanie - nie ma błędu

### Przykład 1

**Dane:**
```
n=3, m=3
1  2  3
4  5  6
7  8  9

w1=1, w2=3
```

**Zamiana wiersza 1 z wierszem 3:**

Krok po kroku (k=1,2,3):
- k=1: temp=1, A[1,1]←7, A[3,1]←1
- k=2: temp=2, A[1,2]←8, A[3,2]←2
- k=3: temp=3, A[1,3]←9, A[3,3]←3

**Wynik:**
```
7  8  9
4  5  6
1  2  3
```

---

### Przykład 2

**Dane:**
```
n=2, m=4
1  2  3  4
5  6  7  8

w1=1, w2=2
```

**Zamiana wiersza 1 z wierszem 2:**

**Wynik:**
```
5  6  7  8
1  2  3  4
```

---

### Przykład 3

**Dane:**
```
n=4, m=2
10  20
30  40
50  60
70  80

w1=2, w2=4
```

**Zamiana wiersza 2 z wierszem 4:**

**Wynik:**
```
10  20
70  80
50  60
30  40
```

---

### Przykład 4

**Dane:**
```
n=3, m=3
1  2  3
4  5  6
7  8  9

w1=2, w2=2
```

**Zamiana wiersza 2 z wierszem 2:**

**Wynik:**
```
1  2  3
4  5  6
7  8  9
```

(Bez zmian - wiersz zamieniany z sobą)

---

### Złożoność

- **Czasowa: O(n×m)** - wczytanie macierzy O(n×m) + zamiana O(m) + wypisanie O(n×m)
- **Pamięciowa: O(n×m)** - przechowywanie macierzy

### Warianty rozszerzenia

1. **Zamiana wielu par wierszy:** Powtórzyć procedurę dla kilku par
2. **Zamiana kolumn:** Zmodyfikować pętlę - `for w ← 1 to n` zamiast `for k ← 1 to m`
3. **Rotacja wierszy:** Zamienić w1↔w2, w2↔w3, itd.
4. **Odwracanie wiersza:** Zamienić A[w,1]↔A[w,m], A[w,2]↔A[w,m-1], itp.

### Porównanie z zamianą kolumn

| Operacja | Pseudokod | Pętla zewnętrzna |
|----------|-----------|-----------------|
| Zamiana wierszy | `for k ← 1 to m` | Po kolumnach |
| Zamiana kolumn | `for w ← 1 to n` | Po wierszach |

### Uwagi

- To najprostsza operacja na macierzach
- Wiele algorytmów sortowania macierzy używa tej operacji
- Zmiana wymaga `temp` do zachowania jednej wartości
- Nie sprawdzamy zakresu w1, w2 - założyć że są prawidłowe
- W praktyce dodać walidację: `if (w1 >= 1 AND w2 <= n)` itp.

### Zastosowanie

- Sortowanie wierszy macierzy (bubbleSort na wierszach)
- Operacje permutacyjne na danych
- Macierze reprezentujące relacje - zmiana kolejności elementów
- Transformacje obrazów (zmiana kolejności linii skanowania)
