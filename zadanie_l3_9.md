# LISTA 3 - ZADANIE 9
## Znalezienie maksimum - Dziel i Zwyciężaj (Divide and Conquer)

### Opis
Znaleźć maksymalny element w tablicy korzystając z algorytmu "dziel i zwyciężaj" (divide and conquer). Algorytm dzieli tablicę na połowy, rekurencyjnie znajduje maksimum w każdej części, a następnie zwraca większe z dwóch.

### Idea
1. Jeśli tablica ma 1 element, to jest maksimum
2. Podziel tablicę na dwie połowy
3. Rekurencyjnie znajdź maksimum w lewej połowie
4. Rekurencyjnie znajdź maksimum w prawej połowie
5. Zwróć większe z dwóch maksimów

### Pseudokod

```
algorithm MaximumDzielIZwyciężaj(A, lewa, prawa)
  
  if (lewa = prawa) then
    // Jeden element - to maksimum
    return A[lewa]
  else
    // Podziel tablicę na połowy
    środek ← (lewa + prawa) div 2
    
    // Znajdź maksimum w lewej połowie
    maxLewy ← MaximumDzielIZwyciężaj(A, lewa, środek)
    
    // Znajdź maksimum w prawej połowie
    maxPrawy ← MaximumDzielIZwyciężaj(A, środek+1, prawa)
    
    // Zwróć większe z nich
    if (maxLewy > maxPrawy) then
      return maxLewy
    else
      return maxPrawy
    end if
  end if
  
end algorithm

// Program główny
program MAIN
  read(n)
  
  for i ← 1 to n do
    read(A[i])
  end for
  
  result ← MaximumDzielIZwyciężaj(A, 1, n)
  write("Maksimum = ", result)
  
end program
```

---

### Alternatywna forma (bardziej zwięzła)

```
algorithm MaxDZ(A, l, p)
  if (l = p) then
    return A[l]
  else
    m ← (l + p) div 2
    return max(MaxDZ(A, l, m), MaxDZ(A, m+1, p))
  end if
end algorithm
```

---

### Przykłady

**Przykład 1: [3, 7, 2, 9, 1]**

```
MaxDZ(A, 1, 5)
├─ m = (1+5) div 2 = 3
├─ MaxDZ(A, 1, 3)
│  ├─ m = (1+3) div 2 = 2
│  ├─ MaxDZ(A, 1, 2)
│  │  ├─ m = (1+2) div 2 = 1
│  │  ├─ MaxDZ(A, 1, 1) → 3
│  │  ├─ MaxDZ(A, 2, 2) → 7
│  │  └─ max(3, 7) = 7
│  ├─ MaxDZ(A, 3, 3) → 2
│  └─ max(7, 2) = 7
├─ MaxDZ(A, 4, 5)
│  ├─ m = (4+5) div 2 = 4
│  ├─ MaxDZ(A, 4, 4) → 9
│  ├─ MaxDZ(A, 5, 5) → 1
│  └─ max(9, 1) = 9
└─ max(7, 9) = 9
```

Wynik: **Maksimum = 9** ✓

---

**Przykład 2: [5, 2, 8, 1]**

```
MaxDZ(A, 1, 4)
├─ m = 2
├─ MaxDZ(A, 1, 2)
│  ├─ m = 1
│  ├─ MaxDZ(A, 1, 1) → 5
│  ├─ MaxDZ(A, 2, 2) → 2
│  └─ max(5, 2) = 5
├─ MaxDZ(A, 3, 4)
│  ├─ m = 3
│  ├─ MaxDZ(A, 3, 3) → 8
│  ├─ MaxDZ(A, 4, 4) → 1
│  └─ max(8, 1) = 8
└─ max(5, 8) = 8
```

Wynik: **Maksimum = 8** ✓

---

**Przykład 3: [42]** (jeden element)

```
MaxDZ(A, 1, 1)
├─ lewa = prawa = 1
└─ return A[1] = 42
```

Wynik: **Maksimum = 42** ✓

---

**Przykład 4: [-5, -2, -8, -1]** (liczby ujemne)

```
MaxDZ(A, 1, 4)
├─ m = 2
├─ MaxDZ(A, 1, 2) → max(-5, -2) = -2
├─ MaxDZ(A, 3, 4) → max(-8, -1) = -1
└─ max(-2, -1) = -1
```

Wynik: **Maksimum = -1** ✓

---

**Przykład 5: [10, 10, 10, 10]** (elementy równe)

```
MaxDZ(A, 1, 4)
├─ m = 2
├─ MaxDZ(A, 1, 2) → 10
├─ MaxDZ(A, 3, 4) → 10
└─ max(10, 10) = 10
```

Wynik: **Maksimum = 10** ✓

---

### Drzewo rekurencji [3, 7, 2, 9, 1]

```
            Max(1,5)
          /        \
      Max(1,3)     Max(4,5)
      /    \         /    \
   Max(1,2) 2    Max(4,4) 1
   /    \         (9)
  3      7
  
Najpierw zbiega w dół do pojedynczych elementów,
potem zbiera się w górę porównując
```

---

### Potencjalne problemy logiczne

1. **Zły warunek bazowy**
   - Problem: `if (lewa > prawa)` zamiast `if (lewa = prawa)`
   - Wynik: Może brakować wywołań, błędne wyniki
   - Rozwiązanie: `if (lewa = prawa) return A[lewa]`

2. **Błędy przy dzieleniu**
   - Problem: `środek ← (lewa + prawa + 1) div 2` lub bez +1
   - Wynik: Potencjalne pominięcie elementów lub duplikacja
   - Rozwiązanie: `środek ← (lewa + prawa) div 2`

3. **Zły zakres rekurencji**
   - Problem: `MaxDZ(A, lewa, środek)` i `MaxDZ(A, środek, prawa)` (duplikacja środka!)
   - Wynik: Środkowy element liczony dwukrotnie
   - Rozwiązanie: `MaxDZ(A, lewa, środek)` i `MaxDZ(A, środek+1, prawa)`

4. **Odwrotny operator porównania**
   - Problem: `return maxPrawy if (maxLewy < maxPrawy)`
   - Wynik: Zwraca zawsze to samo lub odwrotnie
   - Rozwiązanie: `if (maxLewy > maxPrawy) return maxLewy; else return maxPrawy`

5. **Brak warunku - wpadnięcie w nieskończoność**
   - Problem: Bez `if (lewa = prawa)`
   - Wynik: Stack Overflow
   - Rozwiązanie: Zawsze bazowy!

6. **Zwrot złej wartości w bazie**
   - Problem: `return 0` zamiast `return A[lewa]`
   - Wynik: Zawsze będzie 0, jeśli to najmniejsza wartość
   - Rozwiązanie: `return A[lewa]`

### Tablica liczby operacji porównania

| n | Porównania (D&Z) | Porównania (liniowe) |
|---|---|---|
| 2 | 1 | 1 |
| 4 | 3 | 3 |
| 8 | 7 | 7 |
| 16 | 15 | 15 |
| 1000 | ~1998 | ~999 |

---

### Złożoność

- **Czasowa: O(n)**
  - Każdy element porównany dokładnie raz
  - Relacja: T(n) = 2×T(n/2) + 1 = O(n)
  - (Taka sama jak algorytm liniowy!)

- **Pamięciowa: O(log n)**
  - Głęb. stosu = log₂(n)

### Porównanie algorytmów znalezienia max

| Algorytm | Złożoność | Porównania |
|----------|-----------|-----------|
| Liniowy | O(n) | n-1 |
| Dziel i Zwyciężaj | O(n) | n-1 |
| Szybkie sortowanie | O(n log n) | ... |

Dziel i Zwyciężaj ma **tę samą złożoność** co liniowy, ale pokazuje ideę strategii!

---

### Zastosowanie

1. **Edukacja:** Nauka "dziel i zwyciężaj"
2. **Rozszerzenia:** Na inne operacje (min, suma, etc.)
3. **Processory:** Przetwarzanie równoległe (każna połowa na innym procesorze!)
4. **Analiza:** Przykład klasycznego podejścia

---

### Warianty

1. **Znalezienie minimum:**
   ```
   if (minLewy < minPrawy) return minLewy; else return minPrawy
   ```

2. **Znalezienie pozycji maksimum:**
   ```
   Zwracaj indeks zamiast wartości
   ```

3. **Znalezienie k-tego największego:**
   ```
   Bardziej skomplikowana modyfikacja
   ```

---

### Historia algorytmu

- Jeden z klasycznych przykładów "dziel i zwyciężaj"
- Pokazuje strategię, choć nie lepszy niż liniowy
- Inspiracja do bardziej zaawansowanych algorytmów
- Merge sort, Quick sort używają podobnego podejścia

---

### Uwagi

- **Złożoność: O(n) - nie lepsza niż liniowy!**
- Ale pokazuje **strukturę** algorytmu dziel i zwyciężaj
- Mergesort i Quicksort używają tej samej ideii, ale na sortowaniu
- Ilość porównań: n-1 (optymalne dla znalezienia max!)
- Algorytm jest **zawsze optymalny** dla tego problemu

### Ćwiczenie

Ręcznie oblicz maksimum dla [8, 3, 1, 7, 2, 9, 4] używając D&Z
(Rysuj drzewo rekurencji!)

### Powiązane problemy

- Znalezienie minimum (analogiczny)
- Znalezienie drugiego maksimum
- Mediana tablicy (bardziej skomplikowany D&Z)
- Selekcja k-tego elementu (Quickselect)
