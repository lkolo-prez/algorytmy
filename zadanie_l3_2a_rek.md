# LISTA 3 - ZADANIE 2a REK
## Silnia liczby (wersja rekurencyjna)

### Opis
Obliczyć silnię liczby n rekurencyjnie: n! = n × (n-1)!, gdzie 0! = 1.

### Wyjaśnienie
1. **Przypadek bazowy:** Jeśli n=0 lub n=1, zwróć 1
2. **Przypadek rekurencyjny:** Zwróć n × silnia(n-1)

### Pseudokod

```
algorithm SilniaRekurencyjnie(n)
  
  if (n < 0) then
    return ERROR
  else if (n = 0 OR n = 1) then
    return 1
  else
    return n × SilniaRekurencyjnie(n-1)
  end if
  
end algorithm

// Program główny
program MAIN
  read(n)
  result ← SilniaRekurencyjnie(n)
  write(n, "! = ", result)
end program
```

### Drzewo wywołań (n=5)

```
Silnia(5)
  ↓ 5 × Silnia(4)
      ↓ 4 × Silnia(3)
          ↓ 3 × Silnia(2)
              ↓ 2 × Silnia(1)
                  ↓ 1 (zwrot: 1)
              ← 2 × 1 = 2
          ← 3 × 2 = 6
      ← 4 × 6 = 24
  ← 5 × 24 = 120
```

### Przykłady

**Przykład 1: n=0**
- Zwróć bezpośrednio 1
- Wynik: 0! = 1

**Przykład 2: n=3**
- Silnia(3) = 3 × Silnia(2)
- Silnia(2) = 2 × Silnia(1)
- Silnia(1) = 1
- Silnia(2) = 2 × 1 = 2
- Silnia(3) = 3 × 2 = 6
- Wynik: 3! = 6

**Przykład 3: n=5**
- Jak na drzewie powyżej
- Wynik: 5! = 120

**Przykład 4: n=1**
- Zwróć bezpośrednio 1
- Wynik: 1! = 1

---

### Potencjalne problemy logiczne

1. **Brak przypadków bazowych**
   - Problem: `if (n > 1) return n × Silnia(n-1)`
   - Wynik: Nieskończona rekurencja aż do Stack Overflow
   - Rozwiązanie: `if (n=0 OR n=1) return 1` na początku

2. **Zły warunek bazowy**
   - Problem: `if (n = 1) return 1` (brakuje n=0)
   - Wynik: Dla n=0 nieskończona rekurencja
   - Rozwiązanie: `if (n = 0 OR n = 1) return 1`

3. **Brak mnożenia w rekurencji**
   - Problem: `return Silnia(n-1)` (bez n ×)
   - Wynik: Zawsze zwróci 1
   - Rozwiązanie: `return n × Silnia(n-1)`

4. **Zły operator - dodawanie zamiast mnożenia**
   - Problem: `return n + Silnia(n-1)`
   - Wynik: Oblicza sumę zamiast iloczynu
   - Rozwiązanie: Dokładnie `×` (mnożenie)

5. **Parametr nie zmienia się**
   - Problem: `return n × Silnia(n)` (n bez zmian)
   - Wynik: Nieskończona rekurencja
   - Rozwiązanie: `Silnia(n-1)` - zmniejszanie parametru

6. **Brak obsługi liczb ujemnych**
   - Problem: Brak warunku `if (n < 0)`
   - Wynik: Dla n=-5 nieskończona rekurencja
   - Rozwiązanie: Zwrócić błąd dla n < 0

### Ścieżka wykonania dla n=4

```
Poziom 1: Silnia(4) → czy 4 = 0 lub 1? NIE
Poziom 2: Silnia(3) → czy 3 = 0 lub 1? NIE
Poziom 3: Silnia(2) → czy 2 = 0 lub 1? NIE
Poziom 4: Silnia(1) → czy 1 = 0 lub 1? TAK → zwróć 1

Zwrotnie wstecz:
Poziom 4: Zwrot 1
Poziom 3: 2 × 1 = 2
Poziom 2: 3 × 2 = 6
Poziom 1: 4 × 6 = 24
```

### Porównanie z wersją iteracyjną

| Aspekt | Iteracyjna | Rekurencyjna |
|--------|-----------|--------------|
| Złożoność czasowa | O(n) | O(n) |
| Złożoność pamięciowa | O(1) | O(n) - stos rekurencji |
| Elegancja | Mniejsza | Większa |
| Zrozumiałość | Łatwiej | Trudniej dla początkujących |
| Wydajność | Szybsza | Wolniejsza ze względu na Stack |
| Głębokość stosu | Nie | n poziomów |

### Zagrożenia

1. **Stack Overflow dla dużych n:**
   - Dla n=10000 przepełnienie stosu
   - Rozwiązanie: Iteracja lub tail recursion optimization

2. **Wiele zbędnych wywołań (jak Fibonacci):**
   - Tutaj nie dotyczy - każde n wołane tylko raz
   - Ale dla bardziej złożonych rekursji problem!

3. **Przestrzeń stosu ograniczona:**
   - Zazwyczaj kilka MB
   - n ≈ 1000-10000 może być problemem

### Tablica rekurencji dla n=3

```
Stos po każdym połączeniu:
| Silnia(1) | ← zwrot 1
| Silnia(2) | 2 × 1 = 2 ← zwrot 2
| Silnia(3) | 3 × 2 = 6 ← zwrot 6
```

### Tablica wartości z głębokością stosu

| n | n! | Głębokość stosu |
|---|----|----|
| 0 | 1 | 1 |
| 5 | 120 | 5 |
| 10 | 3628800 | 10 |
| 100 | ... | 100 |
| 1000 | ... | 1000 - NIEBEZPIECZNE |

### Zastosowanie

- Nauka rekurencji (jeden z pierwszych przykładów)
- Kombinatoryka
- Analiza algorytmów
- Teorii liczb

### Uwagi

- Rekurencyjna wersja jest bardziej elegancka ale mniej wydajna
- Dla każdego n jest DOKŁADNIE jedno wywołanie rekurencyjne (w porównaniu z Fibonacci)
- Stos jest liniowy względem n
- W praktyce używa się wersji iteracyjnej ze względu na wydajność
- Świetny przykład do nauczania rekurencji

### Optymalizacja - Tail Recursion

Wiele kompilatorów optymalizuje tail recursion (zwrot funkcji jest ostatnią operacją):

```
// Tail recursion version
algorithm SilniaRekurencyjnieTail(n, acc)
  if (n = 0) then
    return acc
  else
    return SilniaRekurencyjnieTail(n-1, n×acc)
  end if
end algorithm

// Inicjalizacja: SilniaRekurencyjnieTail(n, 1)
```

Z tail recursion: złożoność pamięciowa może być zoptymalizowana do O(1)!
