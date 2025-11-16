# LISTA 3 - ZADANIE 2a
## Silnia liczby (wersja iteracyjna)

### Opis
Obliczyć silnię liczby n: n! = 1 × 2 × 3 × ... × n, gdzie 0! = 1.

### Wyjaśnienie
1. Jeśli n < 0, błąd (silnia nie istnieje dla liczb ujemnych)
2. Jeśli n = 0 lub n = 1, zwróć 1 (przypadek bazowy)
3. Inicjalizuj `wynik ← 1`
4. Dla każdego i od 2 do n:
   - Pomnóż wynik przez i: `wynik ← wynik × i`
5. Zwróć wynik

### Pseudokod

```
algorithm SilniaIteracyjnie(n)
  read(n)
  
  if (n < 0) then
    write("Błąd: silnia dla liczb ujemnych nie istnieje")
  else if (n = 0 OR n = 1) then
    result ← 1
  else
    result ← 1
    for i ← 2 to n do
      result ← result × i
    end for
  end if
  
  write(n, "! = ", result)
  
end algorithm
```

### Przykłady

**Przykład 1: n=0**
- Warunek bazowy: 0! = 1
- Wynik: 1

**Przykład 2: n=5**
- Krok 1 (i=2): result = 1 × 2 = 2
- Krok 2 (i=3): result = 2 × 3 = 6
- Krok 3 (i=4): result = 6 × 4 = 24
- Krok 4 (i=5): result = 24 × 5 = 120
- Wynik: 5! = 120

**Przykład 3: n=1**
- Warunek bazowy
- Wynik: 1! = 1

**Przykład 4: n=10**
- 10! = 3628800
- Wynik: 3628800

---

### Potencjalne problemy logiczne

1. **Brak warunku dla n=0 i n=1**
   - Problem: Pętla zawsze od 2, ale `result` niezainicjalizowany
   - Wynik: Dla n=0 błęd dostępu do pamięci
   - Rozwiązanie: `if (n=0 OR n=1) result ← 1` na początek

2. **Zła inicjalizacja wyniku**
   - Problem: `result ← 0` zamiast `result ← 1`
   - Wynik: Każde mnożenie da 0
   - Rozwiązanie: Zawsze `result ← 1` (element neutralny mnożenia)

3. **Pętla od 1 zamiast od 2**
   - Problem: `for i ← 1 to n`
   - Wynik: Jeden dodatkowy `result × 1` (OK matematycznie, ale zbędny)
   - Rozwiązanie: `for i ← 2 to n` (optymalizacja)

4. **Brak obsługi liczb ujemnych**
   - Problem: Nie ma warunku `if (n < 0)`
   - Wynik: Pętla się nie wykonuje, zwrot `result=1` (błędnie!)
   - Rozwiązanie: Dodać `if (n < 0)` i zwrócić błąd

5. **Brak ochrony przed overflow'em**
   - Problem: Dla n>20 wartość przekracza zakres int
   - Wynik: Przepełnienie, błędne wyniki
   - Rozwiązanie: Użyć `long`, `long long` lub BigInteger

6. **Operacja zamiast mnożenia**
   - Problem: `result ← result + i` zamiast `×`
   - Wynik: Oblicza sumę zamiast iloczynu
   - Rozwiązanie: Dokładnie `result × i`

### Tablica wartości

| n | n! | Uwagi |
|---|----|----|
| 0 | 1 | Przypadek bazowy |
| 1 | 1 | Przypadek bazowy |
| 5 | 120 | Zwykły przypadek |
| 10 | 3628800 | Większa liczba |
| 20 | 2432902008176640000 | Overflow w int! |
| 21 | ... | Overflow w long! |

### Złożoność

- **Czasowa: O(n)** - pętla od 2 do n
- **Pamięciowa: O(1)** - tylko jedna zmienna wynik

### Zastosowanie

- Kombinatoryka: liczba permutacji, kombinacji
- Rachunek prawdopodobieństwa
- Analiza algorytmów
- Matematyka dyskretna

### Uwagi

- Silnia rośnie BARDZO szybko (faktorialna)
- Dla n>20 potrzebne są typy danych większe niż int
- Może być obliczona znacznie szybciej niż rekurencyjnie
- W praktyce duże wartości silni obliczane przez memoizację

