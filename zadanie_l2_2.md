# LISTA 2 - ZADANIE 2
## Rozmiana kwoty na monety

### Opis
Rozmienić daną kwotę na monety o nominałach 5zł, 2zł, 1zł tak, aby liczba monet była minimalna. Algorytm zachłanny.

### Wyjaśnienie
1. Wczytaj kwotę do rozmienienia
2. Zdefiniuj nominały w kolejności malejącej: [5, 2, 1]
3. Dla każdego nominału:
   - Policz ile takich monet się zmieści: `ile ← kwota div nominał`
   - Wypisz tę liczbę
   - Zmniejsz kwotę o wykorzystane monety: `kwota ← kwota mod nominał`
4. Procedura kończy się gdy `kwota = 0`

### Pseudokod

```
algorithm RozmianaMonet(kwota)
  read(kwota)
  
  Nom[1] ← 5
  Nom[2] ← 2
  Nom[3] ← 1
  
  for i ← 1 to 3 do
    ile ← kwota div Nom[i]
    kwota ← kwota mod Nom[i]
    write("Monet", Nom[i], "zł:", ile)
  end for
  
end algorithm
```

### Potencjalne problemy logiczne

1. **Zła kolejność nominałów**
   - Problem: Jeśli będzie [1, 2, 5], algorytm NIE będzie zachłanny
   - Rozwiązanie: Zawsze od największego do najmniejszego

2. **Zamiana operacji div i mod**
   - Problem: `ile ← kwota mod Nom[i]` da resztę zamiast liczby monet
   - Rozwiązanie: `ile ← kwota div Nom[i]` dla liczby, `kwota mod` dla reszty

3. **Niezaktualizowana kwota**
   - Problem: Jeśli zapomnniemy `kwota ← kwota mod Nom[i]`, reszta będzie niepoprawna
   - Rozwiązanie: Zawsze aktualizować `kwota ← kwota mod Nom[i]`

4. **Nominały nie pokrywające całych liczb**
   - Problem: Jeśli będą [5, 2] bez 1, rozmiana 1zł będzie niemożliwa
   - Rozwiązanie: Zawsze mieć nominał 1 na końcu

5. **Nominały niesprzedające się ze sobą**
   - Problem: Jeśli będą [6, 4], pewne kwoty nie będą się dać rozmienić
   - Rozwiązanie: NWD nominałów musi być 1

### Przykład 1

**Dane:** kwota = 18

**Obliczenia:**
- i=1: ile = 18 div 5 = 3, kwota = 18 mod 5 = 3 → 3 monety po 5zł
- i=2: ile = 3 div 2 = 1, kwota = 3 mod 2 = 1 → 1 moneta po 2zł
- i=3: ile = 1 div 1 = 1, kwota = 1 mod 1 = 0 → 1 moneta po 1zł

**Wynik:**
```
Monet 5 zł: 3
Monet 2 zł: 1
Monet 1 zł: 1
Razem: 5 monet
```

---

### Przykład 2

**Dane:** kwota = 27

**Obliczenia:**
- i=1: ile = 27 div 5 = 5, kwota = 27 mod 5 = 2 → 5 monet po 5zł
- i=2: ile = 2 div 2 = 1, kwota = 2 mod 2 = 0 → 1 moneta po 2zł
- i=3: ile = 0 div 1 = 0, kwota = 0 mod 1 = 0 → 0 monet po 1zł

**Wynik:**
```
Monet 5 zł: 5
Monet 2 zł: 1
Monet 1 zł: 0
Razem: 6 monet
```

---

### Przykład 3

**Dane:** kwota = 7

**Obliczenia:**
- i=1: ile = 7 div 5 = 1, kwota = 7 mod 5 = 2 → 1 moneta po 5zł
- i=2: ile = 2 div 2 = 1, kwota = 2 mod 2 = 0 → 1 moneta po 2zł
- i=3: ile = 0 div 1 = 0, kwota = 0 mod 1 = 0 → 0 monet po 1zł

**Wynik:**
```
Monet 5 zł: 1
Monet 2 zł: 1
Monet 1 zł: 0
Razem: 2 monety
```

---

### Przykład 4 (kwota = 1)

**Dane:** kwota = 1

**Obliczenia:**
- i=1: ile = 1 div 5 = 0, kwota = 1 mod 5 = 1 → 0 monet po 5zł
- i=2: ile = 1 div 2 = 0, kwota = 1 mod 2 = 1 → 0 monet po 2zł
- i=3: ile = 1 div 1 = 1, kwota = 1 mod 1 = 0 → 1 moneta po 1zł

**Wynik:**
```
Monet 5 zł: 0
Monet 2 zł: 0
Monet 1 zł: 1
Razem: 1 moneta
```

---

### Złożoność
- **Czasowa: O(1)** - zawsze dokładnie 3 iteracje (stała liczba nominałów)
- **Pamięciowa: O(1)** - przechowyujemy tylko zmienne, nie tablice

### Właściwości algorytmu

1. **Algorytm zachłanny** - zawsze wybiera największą możliwą monetę
2. **Minimalność** - dla nominałów [5, 2, 1] zawsze daje minimalną liczbę monet
3. **Poprawność** - dla kwoty > 0 zawsze się skończy (ostatnia moneta 1zł)

### Uwagi
- Algorytm zachłanny NIE zawsze daje optymalny wynik dla innych nominałów
- Przykład: Dla nominałów [6, 4, 1] i kwoty 12:
  - Zachłanny: 2×6 + 0×4 + 0×1 = 2 monety ✓
  - Ale dla kwoty 10:
    - Zachłanny: 1×6 + 1×4 + 0×1 = 2 monety
    - Optymalny: 0×6 + 0×4 + 10×1 = 10 monet (gorzej!)
    - Optymalny: 1×6 + 1×4 = 2 monety (równo, ale różnie)
