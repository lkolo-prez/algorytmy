# LISTA 2 - ZADANIE 5b
## Tablica "wężykowa" (Snake pattern)

### Opis
Wypełnić tablicę n×n kolejnymi liczbami w schemacie "wężyka": wiersze nieparzyste od lewej do prawej, wiersze parzyste od prawej do lewej.

### Wyjaśnienie
1. Zainicjalizuj licznik: `licz ← 0`
2. Dla każdego wiersza w:
   - Jeśli w jest **nieparzysty** (w mod 2 = 1): wypełniaj od k=1 do n
   - Jeśli w jest **parzysty** (w mod 2 = 0): wypełniaj od k=n do 1
3. Licznik ciągle rośnie, tworząc wąż

### Pseudokod

```
algorithm TablicaWezyk(A, n)
  read(n)
  
  licz ← 0
  
  for w ← 1 to n do
    if (w mod 2 = 1) then
      // Wiersz nieparzysty: od lewej do prawej
      for k ← 1 to n do
        licz ← licz + 1
        A[w,k] ← licz
      end for
    else
      // Wiersz parzysty: od prawej do lewej
      for k ← n downto 1 do
        licz ← licz + 1
        A[w,k] ← licz
      end for
    end if
  end for
  
end algorithm
```

### Potencjalne problemy logiczne

1. **Zły test parzystości**
   - Problem: `w mod 2 = 0` zamiast `w mod 2 = 1` da odwrotne kierunki
   - Rozwiązanie: Zawsze `w mod 2 = 1` dla nieparzystych

2. **Niezresetowany licznik między wierszami**
   - Problem: Jeśli `licz ← 0` wewnątrz każdego wariantu if
   - Rozwiązanie: Licznik musi być całkowicie GLOBALNY i ciągle rosnący

3. **Brak downto w wierszach parzystych**
   - Problem: `for k ← 1 to n` w obu przypadkach
   - Rozwiązanie: Użyć `downto` dla wierszy parzystych

4. **Inkrementacja licznika w złym miejscu**
   - Problem: Jeśli `licz ← licz + 1` będzie poza pętlą wewnętrzną
   - Rozwiązanie: `licz ← licz + 1` musi być wewnątrz pętli po k

5. **Logika if zamieszana**
   - Problem: Jeśli warunki będą `if (w > n/2)` lub inne
   - Rozwiązanie: Zawsze dokładnie `if (w mod 2 = 1)`

### Przykład 1

**Dane:** n = 5

**Obliczenia:**

Wiersz 1 (w=1, nieparzysty):
- k: 1→5, licz: 0→1→2→3→4→5

Wiersz 2 (w=2, parzysty):
- k: 5→1 (wstecz), licz: 5→6→7→8→9→10

Wiersz 3 (w=3, nieparzysty):
- k: 1→5, licz: 10→11→12→13→14→15

Wiersz 4 (w=4, parzysty):
- k: 5→1 (wstecz), licz: 15→16→17→18→19→20

Wiersz 5 (w=5, nieparzysty):
- k: 1→5, licz: 20→21→22→23→24→25

**Wynik:**
```
0   1   2   3   4
9   8   7   6   5
10  11  12  13  14
19  18  17  16  15
20  21  22  23  24
```

---

### Przykład 2

**Dane:** n = 3

**Wynik:**
```
1  2  3
6  5  4
7  8  9
```

---

### Przykład 3

**Dane:** n = 4

**Wynik:**
```
1   2   3   4
8   7   6   5
9  10  11  12
16 15  14  13
```

---

### Przykład 4

**Dane:** n = 2

**Wynik:**
```
1  2
4  3
```

---

### Właściwości wzoru

1. **Każdy wiersz zawiera dokładnie n liczb**: Brak luk, brak duplikatów
2. **Liczby są ciągłe**: Od 1 do n²
3. **Połączenie wierszy tworzy wąż**: Koniec wiersza nieparzystego = początek parzystego

### Złożoność

- **Czasowa: O(n²)** - każda pozycja wypełniana dokładnie raz
- **Pamięciowa: O(n²)** - przechowujemy tablicę n×n

### Przypadek graniczny

**Dane:** n = 1

**Wynik:**
```
1
```

---

### Zastosowanie

- Algorytmy odczytywania macierzy w specjalnych porządkach
- Kompresja obrazów (niektóre kodeki skanują wężykiem)
- Testy wdrażania operacji na macierzach
- Struktury danych dla gier (pola szachownicy)

### Porównanie z spiralą

| Cecha | Spirala | Wężyk |
|-------|---------|-------|
| Kierunek | Spiralowy: prawo→dół→lewo→góra | Wierszami: zmienia się kierunek |
| Wypełnienie | Warstwami od zewnątrz | Wierszami od góry |
| Kompleksość | Bardziej skomplikowana logika | Prostsza logika |
| Zaczęcie | (1,1) → prawo | (1,1) → prawo |

### Uwagi

- To popularne zadanie w testach programistycznych
- Nazwa "wężyk" pochodzi od wyglądu liczb
- Warunek `w mod 2 = 1` jest kluczowy
- W C++ można użyć `(w-1) % 2 == 0` zamiast `w mod 2 = 1`
