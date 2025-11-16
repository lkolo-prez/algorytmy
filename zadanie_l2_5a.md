# LISTA 2 - ZADANIE 5a
## Tablica spiralna n×n

### Opis
Wypełnić tablicę n×n kolejnymi liczbami naturalnymi w spirali: prawo → dół → lewo → góra → powtórzyć dla wewnętrznej ramki.

### Wyjaśnienie
1. Definiujemy "ramkę" czterema granicami: g (górny wiersz), d (dolny), l (lewa kolumna), p (prawa)
2. Poruszamy się czterema kierunkami:
   - **Górny wiersz** od l do p (w prawo)
   - **Prawy słup** od g+1 do d (w dół)
   - **Dolny wiersz** od p-1 do l (w lewo) - jeśli g < d
   - **Lewy słup** od d-1 do g+1 (w górę) - jeśli l < p
3. Po każdym pełnym obrocie zmniejszamy ramkę: g++, d--, l++, p--
4. Powtarzamy aż ramka się skurczy (g > d lub l > p)

### Pseudokod

```
algorithm TablicaSpirala(A, n)
  read(n)
  
  g ← 1
  d ← n
  l ← 1
  p ← n
  licz ← 0
  
  while (g ≤ d) and (l ≤ p) do
    // Górny wiersz: w = g, k od l do p
    for k ← l to p do
      licz ← licz + 1
      A[g,k] ← licz
    end for
    
    // Prawy słup: k = p, w od g+1 do d
    for w ← g+1 to d do
      licz ← licz + 1
      A[w,p] ← licz
    end for
    
    if (g < d) then
      // Dolny wiersz: w = d, k od p-1 do l
      for k ← p-1 downto l do
        licz ← licz + 1
        A[d,k] ← licz
      end for
    end if
    
    if (l < p) then
      // Lewy słup: k = l, w od d-1 do g+1
      for w ← d-1 downto g+1 do
        licz ← licz + 1
        A[w,l] ← licz
      end for
    end if
    
    g ← g + 1
    d ← d - 1
    l ← l + 1
    p ← p - 1
    
  end while
  
end algorithm
```

### Potencjalne problemy logiczne

1. **Brak warunków if(g < d) i if(l < p)**
   - Problem: Duplikowanie wierszy/kolumn gdy ramka jest zbyt mała
   - Rozwiązanie: Zawsze sprawdzać przed iteracją dolnego wiersza i lewego słupa

2. **Zła kolejność objazdów**
   - Problem: Jeśli zmienisz kolejność: lewo → dół → prawo → góra, spirala będzie zła
   - Rozwiązanie: Zawsze: prawo, dół, lewo (jeśli możliwe), góra (jeśli możliwe)

3. **Błędne zakresy pętli downto**
   - Problem: `for k ← p to l` zamiast `p-1 downto l`
   - Rozwiązanie: Zawsze `downto` dla pętli wstecznych

4. **Nieskończona pętla while**
   - Problem: Jeśli zapomnimy zmniejszać ramkę (g++, d--, l++, p--)
   - Rozwiązanie: Zawsze na końcu iteracji zmniejszać wszystkie cztery granice

5. **Brak inkrementacji licznika**
   - Problem: Jeśli zapomnniemy `licz ← licz + 1`, będziemy wpisywać to samo
   - Rozwiązanie: Każde przypisanie musi być poprzedzone inkrementacją

### Przykład 1

**Dane:** n = 3

**Iteracja 1 (g=1, d=3, l=1, p=3):**
```
Górny wiersz (w=1, k: 1→3): 1, 2, 3
Prawy słup (k=3, w: 2→3): 4, 5
Dolny wiersz (w=3, k: 2→1): 6, 7
Lewy słup (k=1, w: 2→2): 8
```

**Wynik po iteracji 1:**
```
1  2  3
8  ?  4
7  6  5
```

**Iteracja 2 (g=2, d=2, l=2, p=2):**
- Górny wiersz: A[2,2] = 9
- Prawy słup: pusto (g+1=3 > d=2)
- Dolny wiersz: warunek g < d = (2 < 2) = false, pomijamy
- Lewy słup: warunek l < p = (2 < 2) = false, pomijamy

**Wynik końcowy:**
```
1  2  3
8  9  4
7  6  5
```

---

### Przykład 2

**Dane:** n = 4

**Wynik:**
```
1   2   3   4
12  13  14  5
11  16  15  6
10  9   8   7
```

---

### Przykład 3

**Dane:** n = 5

**Wynik:**
```
1   2   3   4   5
16  17  18  19  6
15  24  25  20  7
14  23  22  21  8
13  12  11  10  9
```

---

### Przykład 4

**Dane:** n = 2

**Iteracja 1 (g=1, d=2, l=1, p=2):**
```
Górny wiersz: 1, 2
Prawy słup: 3
Dolny wiersz (g < d: 1 < 2): 4
Lewy słup (l < p: 1 < 2): pusto (w: 1 downto 2 - brak elementów)
```

**Wynik:**
```
1  2
4  3
```

---

### Złożoność

- **Czasowa: O(n²)** - każda pozycja odwiedzana dokładnie raz
- **Pamięciowa: O(n²)** - przechowujemy tablicę n×n

### Kroki algorytmu (krótko)

1. Zainicjalizuj cztery granice
2. Dopóki ramka istnieje:
   - Wypełnij górny wiersz (prawo)
   - Wypełnij prawy słup (dół)
   - Jeśli możliwe, wypełnij dolny wiersz (lewo)
   - Jeśli możliwe, wypełnij lewy słup (góra)
   - Zmniejsz ramkę

### Zastosowanie

- Testy algorytmów obsługi macierzy
- Wizualizacja pojęcia "spirali" w programowaniu
- Struktura danych do reprezentacji map w grach

### Uwagi

- Sprawdzenia `if (g < d)` i `if (l < p)` są KLUCZOWE
- Dla n=1 algorytm po prostu wpisze 1 i gotowe
- Spirala zawsze zaczyna się od (1,1) i idzie w prawo
