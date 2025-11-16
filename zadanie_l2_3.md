# LISTA 2 - ZADANIE 3
## k-ty co do wielkości element

### Opis
Znaleźć k-ty najmniejszy element w zbiorze n liczb. Po posortowaniu tablica, szukany element to A[k].

### Wyjaśnienie
1. Wczytaj n elementów do tablicy
2. Wczytaj k (numer pozycji po sortowaniu)
3. Posortuj tablicę rosnąco (np. sortowanie bąbelkowe)
4. Zwróć element na pozycji k: `A[k]`
5. Dla k-tego co do wielkości MAXA: zwróć `A[n-k+1]`

### Pseudokod

```
algorithm KtyElement(A, n, k)
  read(n)
  for i ← 1 to n do
    read(A[i])
  end for
  read(k)
  
  // Sortowanie bąbelkowe rosnące
  for i ← 1 to n-1 do
    for j ← 1 to n-i do
      if A[j] > A[j+1] then
        temp ← A[j]
        A[j] ← A[j+1]
        A[j+1] ← temp
      end if
    end for
  end for
  
  write("k-ty element:", A[k])
end algorithm
```

### Potencjalne problemy logiczne

1. **k poza zakresem**
   - Problem: Jeśli k > n lub k < 1, dostaniemy błąd indeksowania
   - Rozwiązanie: Sprawdzić `if k >= 1 and k <= n` przed dostępem

2. **Brak sortowania**
   - Problem: Zwrócimy element z pozycji k w oryginalnej tablicy, nieposortowanej
   - Rozwiązanie: Zawsze wykonać sortowanie przed zwróceniem wyniku

3. **Zła granica pętli sortowania**
   - Problem: `for j ← 1 to n` zamiast `n-i` spowoduje więcej iteracji i bąbelki
   - Rozwiązanie: Użyć `for j ← 1 to n-i` dla optymalnej optymalizacji

4. **Zły operator porównania**
   - Problem: `if A[j] < A[j+1]` da sortowanie malejące
   - Rozwiązanie: `if A[j] > A[j+1]` dla rosnącego

5. **Brak zamiany**
   - Problem: Jeśli zapomnimy `A[j] ← A[j+1]` i `A[j+1] ← temp`
   - Rozwiązanie: Zawsze trzeba temp dla bezpiecznej zamiany

6. **Zła interpretacja "k-ty co do wielkości"**
   - Problem: Pomyłka między "k-ty najmniejszy" a "k-ty największy"
   - Rozwiązanie: k-ty najmniejszy to `A[k]`, k-ty największy to `A[n-k+1]`

### Przykład 1

**Dane:**
- n = 8
- A = [3, 1, 4, 1, 5, 9, 2, 6]
- k = 3

**Sortowanie:**
```
Początek: [3, 1, 4, 1, 5, 9, 2, 6]
Po pętle i=1: [1, 3, 1, 4, 5, 2, 6, 9]
Po pętle i=2: [1, 1, 3, 4, 2, 5, 6, 9]
Po pętle i=3: [1, 1, 2, 3, 4, 5, 6, 9]
Po pętle i=4+: [1, 1, 2, 3, 4, 5, 6, 9] (brak zmian)
```

**Wynik:** A[3] = 2 (trzeci najmniejszy element)

---

### Przykład 2

**Dane:**
- n = 5
- A = [5, 2, 8, 1, 9]
- k = 1

**Sortowanie:** [1, 2, 5, 8, 9]

**Wynik:** A[1] = 1 (najmniejszy element)

---

### Przykład 3

**Dane:**
- n = 5
- A = [5, 2, 8, 1, 9]
- k = 5

**Sortowanie:** [1, 2, 5, 8, 9]

**Wynik:** A[5] = 9 (największy element)

---

### Przykład 4 (szukanie k-tego największego)

**Dane:**
- n = 7
- A = [10, 3, 7, 2, 9, 1, 5]
- k = 2 (drugi największy)

**Sortowanie:** [1, 2, 3, 5, 7, 9, 10]

**Obliczenie:** k-ty największy = A[n-k+1] = A[7-2+1] = A[6] = 9

**Wynik:** 9 (drugi największy)

---

### Złożoność

- **Czasowa: O(n²)** - sortowanie bąbelkowe ma złożoność n²
- **Pamięciowa: O(n)** - przechowujemy tablicę

### Alternatywy (bardziej efektywne)

1. **Sortowanie szybkie (QuickSort):** O(n log n) średnio
2. **Algorytm select (Hoare):** O(n) średnio
3. **Sterta (Heap):** O(n log k) dla k-tego elementu

### Uwagi

- Sortowanie bąbelkowe to najprostsza metoda, ale najwolniejsza
- Dla dużych tablic lepiej użyć QuickSort lub algorytmu select
- Jeśli potrzebujemy wielu k-tych elementów, można posortować raz
- Stabilność sortowania: Jeśli są duplikaty, ten sam element pojawia się wielokrotnie
