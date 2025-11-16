# LISTA 3 - ZADANIE 6
## Funkcja F(y,z) - Mnożenie "Rosyjskiego Chłopka" (Russian Peasant)

### Opis
Obliczyć iloczyn dwóch liczb y × z za pomocą algorytmu "Rosyjskiego Chłopka" (ang. Russian Peasant Multiplication). Algorytm wykorzystuje:
- Dzielenie przez 2 (prawy przesunięcie bitowe)
- Mnożenie przez 2 (lewy przesunięcie bitowe)
- Dodawanie

Historycznie używany gdy mnożenie było kosztowne, a dzielenie i dodawanie tanie.

### Zasada algorytmu

F(y, z) = ?
- Jeśli y = 0, to F(0, z) = 0
- Jeśli y jest parzyste: F(y, z) = F(y/2, z×2)
- Jeśli y jest nieparzyste: F(y, z) = z + F(y-1, z) = z + F((y-1)/2, z×2)

---

## Wersja rekurencyjna

### Pseudokod

```
algorithm FRekurencyjnie(y, z)
  
  if (y = 0) then
    return 0
  else if (y mod 2 = 1) then
    // y nieparzyste
    return z + FRekurencyjnie((y-1)/2, z×2)
  else
    // y parzyste
    return FRekurencyjnie(y/2, z×2)
  end if
  
end algorithm

// Program główny
program MAIN
  read(y, z)
  result ← FRekurencyjnie(y, z)
  write(y, " × ", z, " = ", result)
end program
```

---

## Wersja iteracyjna

### Pseudokod

```
algorithm FIteracyjnie(y, z)
  read(y, z)
  
  wynik ← 0
  
  while (y > 0) do
    if (y mod 2 = 1) then
      wynik ← wynik + z
    end if
    
    y ← y div 2
    z ← z × 2
  end while
  
  write("Wynik = ", wynik)
  
end algorithm
```

---

### Przykłady

**Przykład 1: y=13, z=7** (13 × 7 = 91)

Rekurencyjnie:
```
F(13, 7) = 7 + F(6, 14)
         = 7 + F(3, 28)
         = 7 + (28 + F(2, 56))
         = 7 + 28 + F(1, 112)
         = 7 + 28 + (112 + F(0, 224))
         = 7 + 28 + 112 + 0
         = 147... CZEKAJ, TO BŁĘDO!

Poprawnie:
F(13, 7) = 7 + F(6, 14)           [13 nieparzyste]
         = 7 + F(3, 28)           [6 parzyste]
         = 7 + (28 + F(1, 56))    [3 nieparzyste]
         = 7 + 28 + (56 + F(0, 112)) [1 nieparzyste]
         = 7 + 28 + 56 + 0
         = 91 ✓
```

Iteracyjnie, krok po kroku:

| Krok | y | z | y nieparzyste? | wynik |
|------|---|---|----|-------|
| 1 | 13 | 7 | TAK | 0 + 7 = 7 |
| 2 | 6 | 14 | NIE | 7 |
| 3 | 3 | 28 | TAK | 7 + 28 = 35 |
| 4 | 1 | 56 | TAK | 35 + 56 = 91 |
| 5 | 0 | 112 | - | Koniec |

Wynik: **13 × 7 = 91** ✓

---

**Przykład 2: y=12, z=5** (12 × 5 = 60)

| Krok | y | z | y nieparzyste? | wynik |
|------|---|---|---|----|
| 1 | 12 | 5 | NIE | 0 |
| 2 | 6 | 10 | NIE | 0 |
| 3 | 3 | 20 | TAK | 0 + 20 = 20 |
| 4 | 1 | 40 | TAK | 20 + 40 = 60 |
| 5 | 0 | 80 | - | Koniec |

Wynik: **12 × 5 = 60** ✓

---

**Przykład 3: y=8, z=3** (8 × 3 = 24)

| Krok | y | z | y nieparzyste? | wynik |
|------|---|---|---|------|
| 1 | 8 | 3 | NIE | 0 |
| 2 | 4 | 6 | NIE | 0 |
| 3 | 2 | 12 | NIE | 0 |
| 4 | 1 | 24 | TAK | 0 + 24 = 24 |
| 5 | 0 | 48 | - | Koniec |

Wynik: **8 × 3 = 24** ✓

---

**Przykład 4: y=1, z=100** (1 × 100 = 100)

| Krok | y | z | y nieparzyste? | wynik |
|------|---|----|----|--------|
| 1 | 1 | 100 | TAK | 0 + 100 = 100 |
| 2 | 0 | 200 | - | Koniec |

Wynik: **1 × 100 = 100** ✓

---

### Drzewo rekurencji (y=13, z=7)

```
F(13, 7)
├─ 7
└─ F(6, 14)
   └─ F(3, 28)
      ├─ 28
      └─ F(1, 56)
         ├─ 56
         └─ F(0, 112)
            └─ 0

Suma: 7 + 28 + 56 + 0 = 91
```

---

### Potencjalne problemy logiczne

1. **Brak warunku bazowego (y=0)**
   - Problem: `if (y > 0)...` (nigdy nie zwraca 0)
   - Wynik: Nieskończona rekurencja
   - Rozwiązanie: `if (y = 0) return 0`

2. **Zły operator - zamiast parzystości**
   - Problem: `if (y mod 2 = 0)` i `else` zamienione
   - Wynik: Dodawanie w złych miejscach
   - Rozwiązanie: `if (y mod 2 = 1)` dla nieparzystych

3. **Brak mnożenia z przez 2**
   - Problem: `z ← z` zamiast `z ← z × 2`
   - Wynik: Wartości nie będą rosnąć, błędny wynik
   - Rozwiązanie: `z ← z × 2` lub `z ← z << 1`

4. **Brak dzielenia y przez 2**
   - Problem: `y ← y` zamiast `y ← y div 2`
   - Wynik: Pętla nieskończona (iteracyjnie)
   - Rozwiązanie: `y ← y div 2` lub `y ← y >> 1`

5. **Błędna rekurencja - użycie y zamiast (y-1)/2**
   - Problem: `F(y-1, z×2)` zamiast `F((y-1)/2, z×2)`
   - Wynik: Zbyt wiele iteracji (ale czasami zadziała wolniej)
   - Rozwiązanie: Dzielić przez 2, nie tylko odejmować 1

6. **Nieinicjalizowany wynik w wersji iteracyjnej**
   - Problem: `wynik ← 1` zamiast `wynik ← 0`
   - Wynik: Wynik będzie o 1 za duży
   - Rozwiązanie: `wynik ← 0` na początek

### Tablica wartości

| y | z | F(y,z) | Liczba iteracji |
|---|---|--------|-----------------|
| 1 | 10 | 10 | 1 |
| 5 | 8 | 40 | 3 |
| 8 | 5 | 40 | 4 |
| 13 | 7 | 91 | 4 |
| 16 | 6 | 96 | 5 |
| 32 | 3 | 96 | 6 |

---

### Złożoność

- **Czasowa: O(log y)**
  - W każdej iteracji y dzielone przez 2
  - Liczba iteracji ≈ log₂(y)
  - Znacznie lepsze niż naiwne O(y)!

- **Pamięciowa:**
  - Rekurencyjna: O(log y) - głęb. stosu
  - Iteracyjna: O(1)

---

### Porównanie z mnożeniem naiwnym

| Typ | Złożoność | Czas dla y=1000 |
|-----|-----------|-----------------|
| Naiwne | O(y) | 1000 operacji |
| Rosyjski chłopek | O(log y) | ~10 operacji |

---

### Algorytm w reprezentacji binarnej

Liczba 13 w binarnej to 1101₂

Czytając od prawej:
- 1 (nieparzyste) → dodaj z×2⁰
- 0 (parzyste) → nie dodawaj z×2¹
- 1 (nieparzyste) → dodaj z×2²
- 1 (nieparzyste) → dodaj z×2³

```
13 × 7 = (1101₂) × 7
       = (1×2³ + 1×2² + 0×2¹ + 1×2⁰) × 7
       = 8×7 + 4×7 + 0×7 + 1×7
       = 56 + 28 + 0 + 7
       = 91
```

---

### Historia

- Algorytm znany od czasów starożytnych Egipcjan
- Bardzo efektywny na komputerach (operacje bitowe są szybkie)
- W nowoczesnych CPU mnożenie jest zoptymalizowane, ale algorytm wciąż pokazuje ideę

### Zastosowanie

1. **Mnożenie dużych liczb:** BigInteger
2. **Potęgowanie:** Szybkie a^n mod m (kryptografia)
3. **Układy cyfrowe:** Gdy mnożenie jest droga
4. **Edukacja:** Nauka algorytmów efektywnych

### Uwagi

- Jeden z **najstarszych** algorytmów mnożenia
- Elegancki przykład "dziel i zwyciężaj"
- W praktyce: CPU robią to w sprzęcie szybciej
- Ale algorytmicznie: genialny!
- Możliwy zarówno rekurencyjnie jak i iteracyjnie

### Ćwiczenie

Pomnóż 25 × 11 metodą rosyjskiego chłopka (ręcznie, krok po kroku)
