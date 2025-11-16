# LISTA 3 - ZADANIE 2b
## Potęga liczby (wersja iteracyjna)

### Opis
Obliczyć a^n (a do potęgi n), gdzie a to liczba, n to całkowita potęga (n ≥ 0).

### Wyjaśnienie
1. Jeśli n = 0, zwróć 1 (każda liczba do potęgi 0 to 1)
2. Inicjalizuj `wynik ← 1`
3. Dla każdego i od 1 do n:
   - Pomnóż wynik przez a: `wynik ← wynik × a`
4. Zwróć wynik

### Pseudokod

```
algorithm PotegaIteracyjnie(a, n)
  read(a, n)
  
  if (n < 0) then
    write("Błąd: potęga ujemna nie definiowana w całkowitych")
  else if (n = 0) then
    result ← 1
  else
    result ← 1
    for i ← 1 to n do
      result ← result × a
    end for
  end if
  
  write(a, "^", n, " = ", result)
  
end algorithm
```

### Przykłady

**Przykład 1: n=0**
- Warunek bazowy: a^0 = 1 (dla każdego a)
- a=5, n=0 → 5^0 = 1
- Wynik: 1

**Przykład 2: a=2, n=5**
- Krok 1 (i=1): result = 1 × 2 = 2
- Krok 2 (i=2): result = 2 × 2 = 4
- Krok 3 (i=3): result = 4 × 2 = 8
- Krok 4 (i=4): result = 8 × 2 = 16
- Krok 5 (i=5): result = 16 × 2 = 32
- Wynik: 2^5 = 32

**Przykład 3: a=3, n=3**
- 3^3 = 3 × 3 × 3 = 27
- Wynik: 27

**Przykład 4: a=10, n=4**
- 10^4 = 10000
- Wynik: 10000

---

### Potencjalne problemy logiczne

1. **Brak warunku dla n=0**
   - Problem: Pętla `for i ← 1 to n` dla n=0
   - Wynik: Pętla się nie wykonuje, `result` niezainicjalizowany
   - Rozwiązanie: `if (n = 0) result ← 1` na początku

2. **Zła inicjalizacja wyniku**
   - Problem: `result ← 0` zamiast `result ← 1`
   - Wynik: Każde mnożenie da 0
   - Rozwiązanie: Zawsze `result ← 1`

3. **Brak obsługi a=0**
   - Problem: 0^n dla n>0 powinno dać 0
   - Wynik: Pętla działa, wynik = 0 (ok matematycznie)
   - Rozwiązanie: Logicznie OK, ale test powinien to uwzględnić

4. **Zła operacja - dodawanie zamiast mnożenia**
   - Problem: `result ← result + a`
   - Wynik: n × a zamiast a^n
   - Rozwiązanie: Dokładnie `result × a`

5. **Parametr n nie zmienia się w pętli**
   - Problem: Pętla OK, ale `n ← n - 1` wewnątrz (zniszczenie n)
   - Wynik: Po pętli n = 0
   - Rozwiązanie: Użyć zmiennej pomocniczej `i` do liczenia

6. **Brak ochrony przed overflow'em**
   - Problem: Dla dużych a i n wartość przekracza zakres
   - Wynik: Przepełnienie, błędne wyniki
   - Rozwiązanie: Użyć `long`, `long long` lub BigInteger

### Tablica wartości

| a | n | a^n | Uwagi |
|---|---|-----|-------|
| 2 | 0 | 1 | Przypadek bazowy |
| 5 | 0 | 1 | Przypadek bazowy |
| 2 | 10 | 1024 | 2^10 |
| 10 | 6 | 1000000 | Duża liczba |
| 2 | 31 | 2147483648 | Overflow w int! |

### Złożoność

- **Czasowa: O(n)** - pętla od 1 do n
- **Pamięciowa: O(1)** - tylko jedna zmienna wynik

### Warianty

1. **Potęga szybka (Fast Exponentiation - O(log n)):**
   ```
   Użycie: a^n = (a^2)^(n/2) jeśli n parzyste
           a^n = a × a^(n-1) jeśli n nieparzyste
   ```

2. **Potęga modulo:** a^n mod m (dla kryptografii)

### Zastosowanie

- Matematyka: obliczenia potęg
- Fizyka: prawa potęgowe
- Informatyka: analiza złożoności
- Kryptografia: potęgi modulo

### Uwagi

- Niższe złożoności niż naiwna O(n) są możliwe (fast exponentiation)
- Dla liczb zmiennoprzecinkowych trzeba być ostrożnym z błędami zaokrągleń
- W praktyce dla dużych n wykorzystuje się algorytm szybkiego potęgowania

