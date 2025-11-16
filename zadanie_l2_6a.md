# LISTA 2 - ZADANIE 6a
## Zamiana minimum z maksimum w macierzy

### Opis
W macierzy n×m znaleźć wartość najmniejszą i największą, a następnie je zamieniać miejscami (zamienić ich wartości).

### Wyjaśnienie
1. Przeanalizuj wszystkie elementy macierzy: A[i,j]
2. Znaleźć minimum (wartość i pozycję): min_war, min_w, min_k
3. Znaleźć maksimum (wartość i pozycję): max_war, max_w, max_k
4. Zamienić wartości: `temp ← A[min_w, min_k]`, `A[min_w, min_k] ← A[max_w, max_k]`, `A[max_w, max_k] ← temp`
5. Wypisać zmienioną macierz

### Pseudokod

```
algorithm ZamianaMINMAX(A, n, m)
  read(n, m)
  
  // Wczytywanie macierzy
  for w ← 1 to n do
    for k ← 1 to m do
      read(A[w,k])
    end for
  end for
  
  // Szukanie minimum i maksimum
  min_war ← A[1,1]
  min_w ← 1
  min_k ← 1
  
  max_war ← A[1,1]
  max_w ← 1
  max_k ← 1
  
  for w ← 1 to n do
    for k ← 1 to m do
      if (A[w,k] < min_war) then
        min_war ← A[w,k]
        min_w ← w
        min_k ← k
      end if
      
      if (A[w,k] > max_war) then
        max_war ← A[w,k]
        max_w ← w
        max_k ← k
      end if
    end for
  end for
  
  // Zamiana wartości
  temp ← A[min_w, min_k]
  A[min_w, min_k] ← A[max_w, max_k]
  A[max_w, max_k] ← temp
  
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

1. **Inicjalizacja min/max od zera zamiast pierwszego elementu**
   - Problem: `min_war ← 0`, `max_war ← 0` przy danych ujemnych
   - Przykład: Jeśli wszystkie liczby to [-5, -3, -1], max_war=0 będzie błędnie
   - Rozwiązanie: `min_war ← A[1,1]` i `max_war ← A[1,1]`

2. **Porównania z operatorami odwróconymi**
   - Problem: `if (A[w,k] > min_war)` zamiast `<`
   - Wynik: Znajdzie maksimum w polu dla minimum
   - Rozwiązanie: Precyzyjnie `<` dla minimum, `>` dla maksimum

3. **Nadpisanie min_war lub max_war bez zapisu pozycji**
   - Problem: Zmiana wartości bez jednoczesnego zapisu indeksów
   - Zamiana będzie wykonana na starych indeksach
   - Rozwiązanie: Zawsze min_w, min_k, max_w, max_k razem z wartościami

4. **Brak zapamiętania drugiego elementu podczas zamiany**
   - Problem: `A[min_w, min_k] ← A[max_w, max_k]` bez temp
   - Wynik: Oba pola będą zawierać maksimum
   - Rozwiązanie: Użyć zmiennej tymczasowej `temp`

5. **Równość min i max (wszystkie elementy takie same)**
   - Problem: Macierz [7, 7, 7] → zamiana [7, 7, 7]
   - Wynik: Poprawnie - nie zmienia się nic
   - Rozwiązanie: Logicznie OK, ale test powinien to uwzględnić

6. **Pętla wczytywania nie do n×m**
   - Problem: `for w ← 1 to n do for k ← 1 to n` zamiast m
   - Wynik: Macierz niekwadratowa będzie źle wczytana
   - Rozwiązanie: Zawsze `for k ← 1 to m`

### Przykład 1

**Dane:**
```
n=2, m=3
3  1  4
2  5  6
```

**Szukanie:**
- Min: A[1,2] = 1 (w=1, k=2)
- Max: A[2,3] = 6 (w=2, k=3)

**Zamiana:**
- temp = 1
- A[1,2] ← 6
- A[2,3] ← 1

**Wynik:**
```
3  6  4
2  5  1
```

---

### Przykład 2

**Dane:**
```
n=3, m=3
9  2  7
1  5  8
3  6  4
```

**Szukanie:**
- Min: A[2,1] = 1 (w=2, k=1)
- Max: A[2,3] = 8 (w=2, k=3)

**Wynik:**
```
9  2  7
8  5  1
3  6  4
```

---

### Przykład 3

**Dane:**
```
n=1, m=1
42
```

**Szukanie:**
- Min: A[1,1] = 42
- Max: A[1,1] = 42

**Wynik:**
```
42
```

---

### Przykład 4

**Dane:**
```
n=2, m=2
-5  10
-20  0
```

**Szukanie:**
- Min: A[2,1] = -20
- Max: A[1,2] = 10

**Wynik:**
```
-5  -20
10   0
```

---

### Złożoność

- **Czasowa: O(n×m)** - dwie pętle przeszukujące wszystkie elementy, zamiana w O(1)
- **Pamięciowa: O(n×m)** - przechowywanie całej macierzy

### Warianty

1. **Zamiana na średnią wartość:** Zamiast zamiany, zamienić obie na ich średnią
2. **Zamiana tylko w wierszu:** Szukać min i max tylko w wybranym wierszu
3. **Zamiana tylko w kolumnie:** Szukać min i max tylko w wybranej kolumnie
4. **Zamiana z najbliższymi sąsiadami:** Zamieniać min/max ze swoimi sąsiadami

### Uwagi

- Jeśli min i max się pokrywają (wszystkie elementy równe), zamiana nic nie zmienia
- Operacja zamiany jest w O(1) - tylko zmiana trzech wartości
- Należy pamiętać zarówno wartość jak i pozycję (indeksy) elementów
- To zadanie uczy śledzenia dwóch zmiennych (min i max) jednocześnie

### Zastosowanie

- Normalizacja danych
- Transformacje geometryczne (mapowanie zakresu wartości)
- Testowanie stabilności algorytmów
- Przygotowywanie danych do przetwarzania
