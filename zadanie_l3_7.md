# LISTA 3 - ZADANIE 7
## Odwracanie tablicy rekurencyjnie

### Opis
Odwrócić zawartość tablicy A (zmienić kolejność elementów z A[1]...A[n] na A[n]...A[1]) używając rekurencji.

### Idea
Aby odwrócić tablicę:
1. Zamień pierwszy element z ostatnim: A[1] ↔ A[n]
2. Odwróć pozostałą część (od pozycji 2 do n-1)

### Wersja 1: Rekurencja dwukierunkowa

**Pseudokod:**

```
algorithm OdwracanieTablicy(A, lewa, prawa)
  
  if (lewa < prawa) then
    // Zamień elementów na skrajach
    temp ← A[lewa]
    A[lewa] ← A[prawa]
    A[prawa] ← temp
    
    // Rekurencyjnie odwróć wewnętrzną część
    OdwracanieTablicy(A, lewa+1, prawa-1)
  end if
  
end algorithm

// Program główny
program MAIN
  read(n)
  
  for i ← 1 to n do
    read(A[i])
  end for
  
  write("Tablica przed: ")
  for i ← 1 to n do
    write(A[i], " ")
  end for
  writeln()
  
  OdwracanieTablicy(A, 1, n)
  
  write("Tablica po: ")
  for i ← 1 to n do
    write(A[i], " ")
  end for
  writeln()
  
end program
```

---

### Wersja 2: Rekurencja z pomocniczą tablicą

**Pseudokod:**

```
algorithm OdwracanieRekurencyjnie(A, n, indeks)
  
  if (indeks > 0) then
    OdwracanieRekurencyjnie(A, n, indeks-1)
    write(A[indeks], " ")
  end if
  
end algorithm
```

(Nie modyfikuje A, ale drukuje w odwrotnym porządku)

---

### Przykłady

**Przykład 1: n=5**

Tablica początkowa: [1, 2, 3, 4, 5]

Krok po kroku:

```
Krok 1: Zamień A[1] z A[5]
  [5, 2, 3, 4, 1] → Rekurencja(2, 4)

Krok 2: Zamień A[2] z A[4]
  [5, 4, 3, 2, 1] → Rekurencja(3, 3)

Krok 3: lewa=3, prawa=3 → lewa ≥ prawa, STOP
```

Tablica końcowa: [5, 4, 3, 2, 1] ✓

---

**Przykład 2: n=3**

Tablica początkowa: [10, 20, 30]

```
Krok 1: Zamień A[1] z A[3]
  [30, 20, 10] → Rekurencja(2, 2)

Krok 2: lewa=2, prawa=2 → lewa ≥ prawa, STOP
```

Tablica końcowa: [30, 20, 10] ✓

---

**Przykład 3: n=4**

Tablica początkowa: [A, B, C, D]

```
Krok 1: Zamień A[1] z A[4]
  [D, B, C, A] → Rekurencja(2, 3)

Krok 2: Zamień A[2] z A[3]
  [D, C, B, A] → Rekurencja(3, 2)

Krok 3: lewa=3, prawa=2 → lewa > prawa, STOP
```

Tablica końcowa: [D, C, B, A] ✓

---

**Przykład 4: n=1**

Tablica początkowa: [42]

```
Krok 1: lewa=1, prawa=1 → lewa ≥ prawa, STOP
```

Tablica końcowa: [42] (bez zmian - OK!) ✓

---

### Drzewo rekurencji (n=4)

```
Odwracanie(A, 1, 4)
├─ Zamień A[1] ↔ A[4]: [D,B,C,A]
└─ Odwracanie(A, 2, 3)
   ├─ Zamień A[2] ↔ A[3]: [D,C,B,A]
   └─ Odwracanie(A, 3, 2)
      └─ 3 > 2 → STOP
```

---

### Potencjalne problemy logiczne

1. **Zły warunek zamiany (≤ zamiast <)**
   - Problem: `if (lewa ≤ prawa)`
   - Wynik: Dla n nieparzystych środkowy element się zamieniał z sobą (ok), ale logika rozmyta
   - Rozwiązanie: `if (lewa < prawa)`

2. **Brak zamiany elementów**
   - Problem: Bez `temp` i zamiany
   - Wynik: Tablica niezmieniona
   - Rozwiązanie: `temp ← A[lewa]`, `A[lewa] ← A[prawa]`, `A[prawa] ← temp`

3. **Kierunek rekurencji**
   - Problem: `OdwracanieRekurencyjnie(A, lewa-1, prawa+1)`
   - Wynik: Indeksy wychodzą poza tablicę
   - Rozwiązanie: Zawsze `OdwracanieRekurencyjnie(A, lewa+1, prawa-1)`

4. **Brak warunku bazowego**
   - Problem: Zawsze rekurencja bez warunku (jeśli lewa < prawa)
   - Wynik: Stack Overflow
   - Rozwiązanie: `if (lewa < prawa)` na początku

5. **Niepoprawna inicjalizacja w programie głównym**
   - Problem: `OdwracanieRekurencyjnie(A, 0, n)` zamiast `OdwracanieRekurencyjnie(A, 1, n)`
   - Wynik: Błędy dostępu do pamięci (w pseudokodzie tablica od 1)
   - Rozwiązanie: `OdwracanieRekurencyjnie(A, 1, n)`

### Tablica przyczynów

| Parametry | lewa < prawa? | Co się dzieje |
|-----------|---|---|
| (1,5) | TAK | Zamienia A[1]↔A[5] |
| (2,4) | TAK | Zamienia A[2]↔A[4] |
| (3,3) | NIE | STOP |
| (4,2) | NIE | STOP |

---

### Złożoność

- **Czasowa: O(n)** - każdy element przesunięty dokładnie raz
- **Pamięciowa: O(n)** - głębokość stosu = n/2

---

### Porównanie wersji

| Aspekt | Rekurencyjna | Iteracyjna |
|--------|------------|---------|
| Złożoność czasowa | O(n) | O(n) |
| Złożoność pamięciowa | O(n) - stos | O(1) |
| Elegancja | Wysoka | Niska |
| Wydajność | Gorsza | Lepsza |
| Wad | Stack Overflow | Brak |

### Iteracyjna wersja (dla porównania)

```
algorithm OdwracanieIteracyjnie(A, n)
  lewa ← 1
  prawa ← n
  
  while (lewa < prawa) do
    temp ← A[lewa]
    A[lewa] ← A[prawa]
    A[prawa] ← temp
    
    lewa ← lewa + 1
    prawa ← prawa - 1
  end while
end algorithm
```

---

### Zastosowanie

1. **Problemy na tablicach:** Palindrom, odwracanie
2. **Algorytmy:** Szybkie sortowanie (partycjonowanie)
3. **Struktury danych:** Deque, Stos
4. **Strumienie:** Czytanie od końca

### Uwagi

- Klasyczne zadanie rekurencji dwukierunkowej
- Niezbędne dla zrozumienia rekurencji
- Iteracyjna wersja zawsze lepsza w praktyce
- Doskonały przykład "dziel i zwyciężaj" na tablicach

### Ćwiczenie

Ręcznie odwróć tablicę [1, 2, 3, 4, 5, 6] używając tego algorytmu
