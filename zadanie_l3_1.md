# LISTA 3 - ZADANIE 1
## Ciąg Fibonacciego (wersja iteracyjna i rekurencyjna)

### Opis
Obliczyć n-ty wyraz ciągu Fibonacciego, gdzie F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2) dla n≥2. Pokazać zarówno wersję iteracyjną jak i rekurencyjną.

---

## WERSJA ITERACYJNA

### Wyjaśnienie (iteracyjne)
1. Jeśli n=0, zwróć 0
2. Jeśli n=1, zwróć 1
3. Inicjalizuj: a=0, b=1
4. Dla i od 2 do n:
   - c = a + b
   - a = b
   - b = c
5. Zwróć b

### Pseudokod iteracyjny

```
algorithm FibonacciIteracyjnie(n)
  read(n)
  
  if (n = 0) then
    result ← 0
  else if (n = 1) then
    result ← 1
  else
    a ← 0
    b ← 1
    for i ← 2 to n do
      c ← a + b
      a ← b
      b ← c
    end for
    result ← b
  end if
  
  write("F(", n, ") = ", result)
  
end algorithm
```

### Przykłady iteracyjne

**Przykład 1: n=0**
- Wynik: 0

**Przykład 2: n=1**
- Wynik: 1

**Przykład 3: n=5**
- Krok 1 (i=2): a=0, b=1 → c=1, a=1, b=1
- Krok 2 (i=3): a=1, b=1 → c=2, a=1, b=2
- Krok 3 (i=4): a=1, b=2 → c=3, a=2, b=3
- Krok 4 (i=5): a=2, b=3 → c=5, a=3, b=5
- Wynik: F(5) = 5

**Przykład 4: n=10**
- Ciąg: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
- Wynik: F(10) = 55

### Potencjalne problemy (iteracyjne)

1. **Brak warunków bazowych (n=0, n=1)**
   - Problem: Pętla `for i ← 1 to n` dla wszystkich n
   - Wynik: Dla n=0 lub n=1 błędne wyniki
   - Rozwiązanie: `if (n=0)` i `if (n=1)` na początku

2. **Źle zainicjalizowane a i b**
   - Problem: `a ← 1, b ← 1` zamiast `a ← 0, b ← 1`
   - Wynik: F(2)=2 zamiast F(2)=1
   - Rozwiązanie: zawsze `a ← 0` i `b ← 1`

3. **Zły zakres pętli**
   - Problem: `for i ← 1 to n` zamiast `2 to n`
   - Wynik: Jedno dodatkowe dodawanie
   - Rozwiązanie: `for i ← 2 to n`

4. **Brak rotacji zmiennych (a, b, c)**
   - Problem: `a ← c`, `b ← a` (błędna kolejność)
   - Wynik: Wartości się zduplikują
   - Rozwiązanie: `a ← b`, `b ← c`

5. **Zwrot a zamiast b na końcu**
   - Problem: `result ← a`
   - Wynik: Zwrócona będzie F(n-1) zamiast F(n)
   - Rozwiązanie: `result ← b`

### Złożoność (iteracyjna)

- **Czasowa: O(n)** - pętla wykonuje się n-2 razy
- **Pamięciowa: O(1)** - tylko trzy zmienne a, b, c

---

## WERSJA REKURENCYJNA

### Wyjaśnienie (rekurencyjne)
1. **Przypadek bazowy 1:** Jeśli n=0, zwróć 0
2. **Przypadek bazowy 2:** Jeśli n=1, zwróć 1
3. **Przypadek rekurencyjny:** Zwróć F(n-1) + F(n-2)

### Pseudokod rekurencyjny

```
algorithm FibonacciRekurencyjnie(n)
  
  if (n = 0) then
    return 0
  else if (n = 1) then
    return 1
  else
    return FibonacciRekurencyjnie(n-1) + FibonacciRekurencyjnie(n-2)
  end if
  
end algorithm

// Program główny
program MAIN
  read(n)
  result ← FibonacciRekurencyjnie(n)
  write("F(", n, ") = ", result)
end program
```

### Drzewo wywołań rekurencyjnych (n=5)

```
              F(5)
             /    \
          F(4)      F(3)
         /   \       /   \
       F(3)  F(2)  F(2)  F(1)
      / \    / \    / \
    F(2) F(1) F(1) F(0) F(1) F(0)
   / \
 F(1) F(0)
```

### Przykłady rekurencyjne

**Przykład 1: n=0**
- Bezpośrednio return 0
- Wynik: 0

**Przykład 2: n=3**
- F(3) = F(2) + F(1)
- F(2) = F(1) + F(0) = 1 + 0 = 1
- F(1) = 1
- F(3) = 1 + 1 = 2
- Wynik: 2

**Przykład 3: n=5**
- Jak powyżej na drzewie
- Wynik: 5

**Przykład 4: n=6**
- F(6) = F(5) + F(4) = 5 + 3 = 8
- Wynik: 8

### Potencjalne problemy (rekurencyjne)

1. **Brak przypadków bazowych**
   - Problem: `if (n > 1) return F(n-1) + F(n-2)`
   - Wynik: Nieskończona rekurencja
   - Rozwiązanie: `if (n=0) return 0`, `if (n=1) return 1`

2. **Zły warunek bazowy**
   - Problem: `if (n <= 0) return 1` zamiast `return 0`
   - Wynik: Wszystkie wartości przesunięte i błędne
   - Rozwiązanie: F(0)=0, F(1)=1

3. **Błędna rekurencja**
   - Problem: `return F(n-1) + F(n-3)` zamiast `F(n-2)`
   - Wynik: Zupełnie inny ciąg
   - Rozwiązanie: Dokładnie F(n-1) + F(n-2)

4. **Brak return**
   - Problem: Obliczenie `F(n-1) + F(n-2)` ale bez return
   - Wynik: Zwrot losowej wartości
   - Rozwiązanie: `return` przed każdą ścieżką

5. **Parametr nie zmienia się w rekurencji**
   - Problem: `return F(n) + F(n)` (n się nie zmienia)
   - Wynik: Nieskończona rekurencja
   - Rozwiązanie: `F(n-1) + F(n-2)` - zmniejszanie n

### Porównanie wersji

| Aspekt | Iteracyjna | Rekurencyjna |
|--------|-----------|--------------|
| Złożoność czasowa | O(n) | O(2^n) - wykładnicza! |
| Złożoność pamięciowa | O(1) | O(n) - stos rekurencji |
| Elegancja | Mniej elegancka | Bardzo elegancka |
| Wydajność | Szybka | Bardzo wolna dla dużych n |
| n=40 czas | <1ms | kilka sekund |

### Optymalizacja rekurencji - MEMOIZACJA

```
algorithm FibonacciMemo(n)
  // Statyczna tablica zapamiętywania
  static memo[...] ← {-1}
  
  if (memo[n] ≠ -1) then
    return memo[n]
  end if
  
  if (n = 0) then
    result ← 0
  else if (n = 1) then
    result ← 1
  else
    result ← FibonacciMemo(n-1) + FibonacciMemo(n-2)
  end if
  
  memo[n] ← result
  return result
  
end algorithm
```

Z memoizacją: **O(n)** zamiast O(2^n)!

### Tablica wartości Fibonacciego

| n | F(n) | Iteracyjnie | Rekurencyjnie |
|---|------|------------|---------------|
| 0 | 0 | - | - |
| 5 | 5 | szybko | wolniej |
| 10 | 55 | szybko | wolniej |
| 20 | 6765 | szybko | bardzo wolnie |
| 30 | 832040 | szybko | kilka sekund |
| 40 | 102334155 | szybko | kilka minut! |

### Zastosowanie

- Matematyka: teoria liczb, złota proporcja
- Biologia: rozmnażanie króleików (przykład Fibonacciego!)
- Informatyka: analiza algorytmów
- Finanse: prognozy trendów
- Przyroda: spirale rakowic, płatki kwiatów

### Uwagi

- Bardzo popularne zadanie rekurencji w nauce programowania
- Świetny przykład do pokazania różnicy między iteracją a rekurencją
- Memoizacja jest kluczem do czynienia rekurencji wydajną
- Dla bardzo dużych n nawet iteracja osiąga limit (overflow liczb)
