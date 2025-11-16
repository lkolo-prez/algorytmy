# LISTA 3 - ZADANIE 3
## Największy Wspólny Dzielnik - Algorytm Euklidesa

### Opis
Znaleźć NWD(a, b) - największy wspólny dzielnik dwóch liczb dodatnich przy pomocy algorytmu Euklidesa. Algorytm wykorzystuje fakt, że NWD(a,b) = NWD(b, a mod b).

### Wyjaśnienie
1. Jeśli b = 0, to NWD(a, b) = a (przypadek bazowy)
2. W przeciwnym razie, NWD(a, b) = NWD(b, a mod b)
3. Powtarzaj dopóki reszta nie będzie równa 0

### Wersja rekurencyjna

**Pseudokod:**

```
algorithm NWDRekurencyjnie(a, b)
  
  if (b = 0) then
    return a
  else
    return NWDRekurencyjnie(b, a mod b)
  end if
  
end algorithm

// Program główny
program MAIN
  read(a, b)
  result ← NWDRekurencyjnie(a, b)
  write("NWD(", a, ", ", b, ") = ", result)
end program
```

---

### Wersja iteracyjna

**Pseudokod:**

```
algorithm NWDIteracyjnie(a, b)
  read(a, b)
  
  while (b ≠ 0) do
    temp ← b
    b ← a mod b
    a ← temp
  end while
  
  result ← a
  write("NWD(", a, ", ", b, ") = ", result)
  
end algorithm
```

---

### Przykłady

**Przykład 1: a=48, b=18**

Rekurencyjnie:
- NWD(48, 18) = NWD(18, 48 mod 18) = NWD(18, 12)
- NWD(18, 12) = NWD(12, 18 mod 12) = NWD(12, 6)
- NWD(12, 6) = NWD(6, 12 mod 6) = NWD(6, 0)
- NWD(6, 0) = 6

Wynik: **NWD(48, 18) = 6**

---

**Przykład 2: a=100, b=75**

Iteracyjnie krok po kroku:
- Krok 1: a=100, b=75 → temp=75, b=100%75=25, a=75
- Krok 2: a=75, b=25 → temp=25, b=75%25=0, a=25
- Pętla kończy się bo b=0
- Wynik: a=25

Wynik: **NWD(100, 75) = 25**

---

**Przykład 3: a=17, b=13** (liczby pierwsze)

- NWD(17, 13) = NWD(13, 4)
- NWD(13, 4) = NWD(4, 1)
- NWD(4, 1) = NWD(1, 0)
- NWD(1, 0) = 1

Wynik: **NWD(17, 13) = 1** (liczby względnie pierwsze)

---

**Przykład 4: a=100, b=0**

- NWD(100, 0) = 100 (zaraz warunek bazowy)

Wynik: **NWD(100, 0) = 100**

---

### Drzewo wywołań (a=48, b=18)

```
NWD(48, 18)
  ↓ NWD(18, 12)  [48 mod 18 = 12]
    ↓ NWD(12, 6)  [18 mod 12 = 6]
      ↓ NWD(6, 0)  [12 mod 6 = 0]
        ↓ 6 (zwrot: 6)
```

---

### Potencjalne problemy logiczne

1. **Brak warunku bazowego b=0**
   - Problem: `if (b > 0) return NWD(b, a mod b)`
   - Wynik: Nieskończona rekurencja
   - Rozwiązanie: `if (b = 0) return a` na początku

2. **Zwrot b zamiast a**
   - Problem: `if (b = 0) return b` (zwraca 0!)
   - Wynik: Zawsze zwraca 0
   - Rozwiązanie: `return a`

3. **Zamiana kolejności parametrów w rekurencji**
   - Problem: `return NWD(a mod b, b)` zamiast `NWD(b, a mod b)`
   - Wynik: Błędne wyniki
   - Rozwiązanie: zawsze `NWD(b, a mod b)`

4. **Użycie dzielenia zamiast modulo**
   - Problem: `return NWD(b, a div b)` (dzielenie całkowite zamiast reszty)
   - Wynik: Zupełnie inne wyniki
   - Rozwiązanie: `a mod b` (reszta z dzielenia!)

5. **Brak obsługi ujemnych liczb**
   - Problem: NWD(-12, 8) nie jest definiowany
   - Wynik: Algorytm może nie skończyć się
   - Rozwiązanie: Użyć wartości bezwzględnych

6. **Nieskończona pętla w wersji iteracyjnej**
   - Problem: `while (a ≠ b)` zamiast `while (b ≠ 0)`
   - Wynik: Jeśli a ≠ b, pętla nigdy się nie skończy
   - Rozwiązanie: `while (b ≠ 0)`

### Tablica wartości

| a | b | NWD | Kroki | Uwagi |
|---|---|-----|-------|-------|
| 48 | 18 | 6 | 3 | Zwykły przypadek |
| 100 | 75 | 25 | 2 | Szybko |
| 17 | 13 | 1 | 4 | Liczby pierwsze |
| 1000 | 1 | 1 | 1 | Najmniejszy |
| 56 | 56 | 56 | 1 | Równe |

---

### Złożoność

- **Czasowa: O(log(min(a, b)))**
  - Liczba kroków ≈ log wartości mniejszej liczby
  - Jedna z najbardziej efektywnych operacji!
  
- **Pamięciowa:**
  - Rekurencyjna: O(log(min(a,b))) - głęb. stosu
  - Iteracyjna: O(1)

### Porównanie wersji

| Aspekt | Iteracyjna | Rekurencyjna |
|--------|-----------|--------------|
| Złożoność czasowa | O(log min) | O(log min) |
| Złożoność pamięciowa | O(1) | O(log min) - stos |
| Elegancja | Mniejsza | Większa |
| Wydajność | Szybsza (brak stack) | Wolniejsza |
| Stack Overflow | NIE | Praktycznie NIGDY |

### Kroki algorytmu dla 1071 i 462

```
1071 = 2×462 + 147
462 = 3×147 + 21
147 = 7×21 + 0
NWD = 21
```

---

### Zastosowanie

1. **Matematyka:** Sprowadzanie ułamków do najprostszej postaci
   - 48/18 = (48:6)/(18:6) = 8/3

2. **Teoria liczb:** Sprawdzanie czy liczby są względnie pierwsze

3. **Kryptografia:** Algorytm RSA, obliczanie modularnych odwrotności

4. **Przetwarzanie sygnałów:** Znalezienie największego wspólnego dzielnika częstotliwości

5. **Informatyka:** GCD potrzebny do wielu algorytmów

### Historycznie

- Algorytm Euklidesa znany od czasów antycznych (~300 p.n.e.)
- Jeden z **najstarszych** znanych algorytmów
- Wciąż używany w nowoczesnych systemach kryptograficznych

### Właściwości

1. **Komutacyjność:** NWD(a, b) = NWD(b, a)
2. **Łączność:** NWD(NWD(a,b), c) = NWD(a, NWD(b,c))
3. **Element neutralny:** NWD(a, 0) = a
4. **Tożsamość Bezout:** Istnieją liczby x, y: a×x + b×y = NWD(a, b)

### Rozszerzony Algorytm Euklidesa

Pozwala znaleźć współczynniki x i y z tożsamości Bezout:

```
a×x + b×y = NWD(a, b)
```

Używane w kryptografii!

### Uwagi

- Jeden z najefektywniejszych algorytmów (logarytmiczna złożoność!)
- Wersja iteracyjna preferowana w praktyce (brak stack overflow)
- Warunek `b ≠ 0` jest ABSOLUTNIE KRYTYCZNY
- Zawsze sprawdzać wynik: NWD powinien dzielić zarówno a jak i b

### Ćwiczenie

Spróbuj ręcznie obliczyć NWD(89, 55) - liczby Fibonacciego!
