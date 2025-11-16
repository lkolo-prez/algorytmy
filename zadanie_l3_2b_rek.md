# LISTA 3 - ZADANIE 2b REK
## Potęga liczby (wersja rekurencyjna)

### Opis
Obliczyć a^n (a do potęgi n) rekurencyjnie, gdzie a^n = a × a^(n-1), z warunkiem bazowym a^0 = 1.

### Wyjaśnienie
1. **Przypadek bazowy:** Jeśli n=0, zwróć 1
2. **Przypadek rekurencyjny:** Zwróć a × Potega(a, n-1)

### Pseudokod

```
algorithm PotegaRekurencyjnie(a, n)
  
  if (n < 0) then
    return ERROR
  else if (n = 0) then
    return 1
  else
    return a × PotegaRekurencyjnie(a, n-1)
  end if
  
end algorithm

// Program główny
program MAIN
  read(a, n)
  result ← PotegaRekurencyjnie(a, n)
  write(a, "^", n, " = ", result)
end program
```

### Drzewo wywołań (a=2, n=4)

```
Potega(2, 4)
  ↓ 2 × Potega(2, 3)
      ↓ 2 × Potega(2, 2)
          ↓ 2 × Potega(2, 1)
              ↓ 2 × Potega(2, 0)
                  ↓ 1 (zwrot: 1)
              ← 2 × 1 = 2
          ← 2 × 2 = 4
      ← 2 × 4 = 8
  ← 2 × 8 = 16
```

### Przykłady

**Przykład 1: n=0**
- Zwróć bezpośrednio 1
- Dla każdego a: a^0 = 1
- Wynik: 1

**Przykład 2: a=2, n=3**
- Potega(2,3) = 2 × Potega(2,2)
- Potega(2,2) = 2 × Potega(2,1)
- Potega(2,1) = 2 × Potega(2,0)
- Potega(2,0) = 1
- Potega(2,1) = 2 × 1 = 2
- Potega(2,2) = 2 × 2 = 4
- Potega(2,3) = 2 × 4 = 8
- Wynik: 2^3 = 8

**Przykład 3: a=3, n=4**
- 3^4 = 3 × 3^3 = 3 × 27 = 81
- Wynik: 81

**Przykład 4: a=5, n=2**
- 5^2 = 5 × 5 = 25
- Wynik: 25

---

### Potencjalne problemy logiczne

1. **Brak przypadku bazowego**
   - Problem: `if (n > 0) return a × Potega(a, n-1)`
   - Wynik: Nieskończona rekurencja aż do Stack Overflow
   - Rozwiązanie: `if (n = 0) return 1` na początku

2. **Zły warunek bazowy**
   - Problem: `if (n = 1) return a` (brakuje n=0)
   - Wynik: Dla n=0 nieskończona rekurencja
   - Rozwiązanie: `if (n = 0) return 1`

3. **Brak mnożenia w rekurencji**
   - Problem: `return Potega(a, n-1)` (bez a ×)
   - Wynik: Zawsze zwróci 1 (dla n>0)
   - Rozwiązanie: `return a × Potega(a, n-1)`

4. **Parametr a nie jest używany**
   - Problem: `return Potega(a, n-1) × Potega(a, n-1)` (brakuje a)
   - Wynik: 2^(2^n) zamiast a^n
   - Rozwiązanie: Zawsze mnożyć przez `a` (nie przez wynik rekurencji)

5. **Parametr n nie zmienia się**
   - Problem: `return a × Potega(a, n)` (n bez zmian)
   - Wynik: Nieskończona rekurencja
   - Rozwiązanie: `Potega(a, n-1)` - zmniejszanie n

6. **Brak obsługi liczb ujemnych n**
   - Problem: Brak warunku `if (n < 0)`
   - Wynik: Dla n=-3 nieskończona rekurencja
   - Rozwiązanie: Zwrócić błąd dla n < 0

### Ścieżka wykonania dla a=3, n=3

```
Poziom 1: Potega(3, 3) → czy 3 = 0? NIE
Poziom 2: Potega(3, 2) → czy 2 = 0? NIE
Poziom 3: Potega(3, 1) → czy 1 = 0? NIE
Poziom 4: Potega(3, 0) → czy 0 = 0? TAK → zwróć 1

Zwrotnie wstecz:
Poziom 4: Zwrot 1
Poziom 3: 3 × 1 = 3
Poziom 2: 3 × 3 = 9
Poziom 1: 3 × 9 = 27
```

### Porównanie z wersją iteracyjną

| Aspekt | Iteracyjna | Rekurencyjna |
|--------|-----------|--------------|
| Złożoność czasowa | O(n) | O(n) |
| Złożoność pamięciowa | O(1) | O(n) - stos rekurencji |
| Elegancja | Mniejsza | Większa |
| Zrozumiałość | Łatwiej | Trudniej dla początkujących |
| Wydajność | Szybsza | Wolniejsza |
| Głębokość stosu | Nie | n poziomów |

### Zagrożenia

1. **Stack Overflow dla dużych n:**
   - Dla n=100000 przepełnienie stosu
   - Rozwiązanie: Iteracja

2. **Przestrzeń stosu ograniczona:**
   - Zazwyczaj kilka MB
   - n ≈ 1000-10000 może być problemem

### Tablica rekurencji dla a=2, n=4

```
Stos po każdym połączeniu:
| Potega(2,0) | ← zwrot 1
| Potega(2,1) | 2 × 1 = 2 ← zwrot 2
| Potega(2,2) | 2 × 2 = 4 ← zwrot 4
| Potega(2,3) | 2 × 4 = 8 ← zwrot 8
| Potega(2,4) | 2 × 8 = 16 ← zwrot 16
```

### Tablica wartości z głębokością stosu

| a | n | a^n | Głębokość stosu |
|---|---|-----|-----------------|
| 2 | 0 | 1 | 1 |
| 2 | 5 | 32 | 5 |
| 2 | 10 | 1024 | 10 |
| 2 | 30 | ~10^9 | 30 |
| 2 | 1000 | ... | 1000 - NIEBEZPIECZNE |

### Optymalizacja - Fast Exponentiation (Dziel i Zwyciężaj)

Wersja O(log n):

```
algorithm PotegaSzybka(a, n)
  if (n = 0) then
    return 1
  else if (n mod 2 = 0) then
    // n jest parzyste
    x ← PotegaSzybka(a, n/2)
    return x × x
  else
    // n jest nieparzyste
    return a × PotegaSzybka(a, n-1)
  end if
end algorithm
```

Dla a=2, n=16: zamiast 16 mnożeń mamy 4 mnożenia!

```
2^16 = (2^8)^2 = ((2^4)^2)^2 = (((2^2)^2)^2)^2
```

Głębokość: O(log n) zamiast O(n)

### Zastosowanie

- Nauka rekurencji
- Matematyka: obliczenia potęg
- Fizyka
- Kryptografia (z modulo - RSA)

### Uwagi

- Rekurencyjna wersja jest elegancka ale wolna
- Dla każdego n jest dokładnie jedno wywołanie rekurencyjne
- Stos jest liniowy względem n
- Szybka potęga (binary exponentiation) jest znacznie lepsza O(log n)
- Świetny przykład rekurencji równoważnej iteracji

### Tail Recursion Optimization

```
algorithm PotegaRekurencyjnieTail(a, n, acc)
  if (n = 0) then
    return acc
  else
    return PotegaRekurencyjnieTail(a, n-1, acc×a)
  end if
end algorithm

// Inicjalizacja: PotegaRekurencyjnieTail(a, n, 1)
```

Z tail recursion: część kompilatorów optymalizuje do O(1) pamięci!
