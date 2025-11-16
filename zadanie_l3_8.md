# LISTA 3 - ZADANIE 8
## Sprawdzenie palindromu rekurencyjnie

### Opis
Sprawdzić czy tablica (lub napis) stanowi palindrom (czyta się tak samo od przodu i od tyłu) używając rekurencji.

Palindrom: element na pozycji i = element na pozycji n+1-i dla każdego i.

### Idea
Aby sprawdzić palindrom:
1. Porównaj pierwszy element z ostatnim: A[1] = A[n]?
2. Jeśli nie, zwróć FALSE (nie palindrom)
3. Jeśli tak, sprawdź rekurencyjnie wewnętrzną część (od 2 do n-1)

### Pseudokod

```
algorithm CzyPalindrom(A, lewa, prawa)
  
  if (lewa >= prawa) then
    // Całą tablicę sprawdziliśmy - to palindrom!
    return TRUE
  else if (A[lewa] ≠ A[prawa]) then
    // Znaleziono różnicę - nie palindrom
    return FALSE
  else
    // Rekurencyjnie sprawdź wewnętrzną część
    return CzyPalindrom(A, lewa+1, prawa-1)
  end if
  
end algorithm

// Program główny
program MAIN
  read(n)
  
  for i ← 1 to n do
    read(A[i])
  end for
  
  if (CzyPalindrom(A, 1, n)) then
    write("To PALINDROM")
  else
    write("To NIE palindrom")
  end if
  
end program
```

---

### Przykłady

**Przykład 1: [1, 2, 3, 2, 1]** - Palindrom

```
Krok 1: CzyPalindrom(A, 1, 5)
  A[1]=1, A[5]=1 → równe
  → CzyPalindrom(A, 2, 4)

Krok 2: CzyPalindrom(A, 2, 4)
  A[2]=2, A[4]=2 → równe
  → CzyPalindrom(A, 3, 3)

Krok 3: CzyPalindrom(A, 3, 3)
  lewa=3 >= prawa=3 → STOP
  → return TRUE
```

Wynik: **TAK, to palindrom** ✓

---

**Przykład 2: [R, A, D, A, R]** - Palindrom (słowo RADAR)

```
Krok 1: CzyPalindrom(A, 1, 5)
  A[1]='R', A[5]='R' → równe
  → CzyPalindrom(A, 2, 4)

Krok 2: CzyPalindrom(A, 2, 4)
  A[2]='A', A[4]='A' → równe
  → CzyPalindrom(A, 3, 3)

Krok 3: CzyPalindrom(A, 3, 3)
  lewa=3 >= prawa=3 → STOP
  → return TRUE
```

Wynik: **TAK, to palindrom** ✓

---

**Przykład 3: [1, 2, 3, 4, 5]** - NIE palindrom

```
Krok 1: CzyPalindrom(A, 1, 5)
  A[1]=1, A[5]=5 → różne! 1 ≠ 5
  → return FALSE
```

Wynik: **NIE, to nie palindrom** ✓

---

**Przykład 4: [A, B, C, B, A]** - Palindrom

```
Krok 1: CzyPalindrom(A, 1, 5)
  A[1]='A', A[5]='A' → równe
  → CzyPalindrom(A, 2, 4)

Krok 2: CzyPalindrom(A, 2, 4)
  A[2]='B', A[4]='B' → równe
  → CzyPalindrom(A, 3, 3)

Krok 3: CzyPalindrom(A, 3, 3)
  lewa=3 >= prawa=3 → STOP
  → return TRUE
```

Wynik: **TAK, to palindrom** ✓

---

**Przykład 5: [7]** - Palindrom (jeden element)

```
Krok 1: CzyPalindrom(A, 1, 1)
  lewa=1 >= prawa=1 → STOP
  → return TRUE
```

Wynik: **TAK, to palindrom** ✓

---

**Przykład 6: [H, E, L, L, O]** - NIE palindrom (słowo HELLO)

```
Krok 1: CzyPalindrom(A, 1, 5)
  A[1]='H', A[5]='O' → różne! H ≠ O
  → return FALSE
```

Wynik: **NIE, to nie palindrom** ✓

---

### Drzewo rekurencji [A, B, A]

```
CzyPalindrom(A, 1, 3)
├─ A[1]='A', A[3]='A' → równe
└─ CzyPalindrom(A, 2, 2)
   ├─ lewa=2 >= prawa=2 → STOP
   └─ return TRUE

Wynik: TRUE
```

---

### Drzewo rekurencji [A, B, C]

```
CzyPalindrom(A, 1, 3)
├─ A[1]='A', A[3]='C' → różne!
└─ return FALSE

Wynik: FALSE (szybko, na pierwszym porównaniu!)
```

---

### Potencjalne problemy logiczne

1. **Zły warunek bazowy (≤ zamiast ≥)**
   - Problem: `if (lewa ≤ prawa)`
   - Wynik: Dla elementów w pozycjach równych się zamieniają, ale logika rozmyta
   - Rozwiązanie: `if (lewa >= prawa)`

2. **Brakuje warunku na nierówność elementów**
   - Problem: Bezpośrednio `CzyPalindrom(A, lewa+1, prawa-1)`
   - Wynik: Nie sprawdzi czy elementy się równają
   - Rozwiązanie: `if (A[lewa] ≠ A[prawa]) return FALSE`

3. **Zwrot FALSE zamiast TRUE dla bazowego**
   - Problem: `if (lewa >= prawa) return FALSE`
   - Wynik: Każdy palindrom zwróci FALSE
   - Rozwiązanie: `return TRUE`

4. **Zły kierunek przesuwania wskaźników**
   - Problem: `CzyPalindrom(A, lewa-1, prawa+1)` lub `CzyPalindrom(A, lewa, prawa)`
   - Wynik: Stack Overflow
   - Rozwiązanie: `CzyPalindrom(A, lewa+1, prawa-1)`

5. **Brak bazy do rekurencji**
   - Problem: Nigdy się nie zatrzyma
   - Wynik: Stack Overflow
   - Rozwiązanie: `if (lewa >= prawa)` na początku

6. **Pomylona kolejność logiki**
   - Problem: `if (CzyPalindrom(...)) return FALSE; else return TRUE`
   - Wynik: Wynik odwrócony
   - Rozwiązanie: Zwracać TRUE i FALSE w prawidłowych miejscach

### Tablica porównań

| Element 1 | Element 2 | Równe? | Działanie |
|-----------|-----------|--------|-----------|
| A[1] | A[n] | TAK | Idź dalej |
| A[1] | A[n] | NIE | Zwróć FALSE |
| A[2] | A[n-1] | TAK | Idź dalej |
| ... | ... | ... | ... |

---

### Złożoność

- **Czasowa: O(n)** - każdy element porównany maksymalnie raz (ale może szybciej jeśli nierówność na początku)
- **Pamięciowa: O(n)** - głębokość stosu = n/2

---

### Porównanie wersji

| Aspekt | Rekurencyjna | Iteracyjna |
|--------|------------|---------|
| Złożoność czasowa | O(n) | O(n) |
| Złożoność pamięciowa | O(n) - stos | O(1) |
| Elegancja | Wysoka | Niska |
| Wydajność | Gorsza | Lepsza |

---

### Iteracyjna wersja (dla porównania)

```
algorithm CzyPalindromIteracyjnie(A, n)
  lewa ← 1
  prawa ← n
  jestPalindrom ← TRUE
  
  while (lewa < prawa) do
    if (A[lewa] ≠ A[prawa]) then
      jestPalindrom ← FALSE
      break  // Wyjście z pętli
    end if
    
    lewa ← lewa + 1
    prawa ← prawa - 1
  end while
  
  return jestPalindrom
end algorithm
```

---

### Zastosowanie

1. **Weryfikacja danych:** Sprawdzanie kodu kreskowego
2. **Przetwarzanie tekstu:** Słowa/zdania palindromowe
3. **Bioinformatyka:** Sekwencje DNA (PALINDROMY w DNA!)
4. **Algorytmy:** Sprawdzanie symetrii

### Znane palindromy

| Typ | Przykład |
|-----|----------|
| Liczby | 121, 12321 |
| Słowa | RADAR, LEVEL, HANNAH |
| Frazy | A man, a plan, a canal: Panama |
| DNA | GAATTC (sekwencja EcoRI) |

---

### Uwagi

- Klasyczne zadanie do nauczania rekurencji
- Dwukierunkowa rekurencja (z obu stron)
- Wersja iteracyjna zawsze lepsza w praktyce (brak stack)
- Szybko odpowiada NIE (jeśli nierówność na początku)
- Musisz czekać na koniec by potwierdzić TAK

### Ćwiczenie

Sprawdź czy te tablice są palindromami:
1. [5, 4, 3, 4, 5]
2. [1, 2, 3]
3. [A, A, A, A, A]
4. [1, 2, 2, 1]
