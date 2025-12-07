````markdown
# Sortowanie Pozycyjne (Radix Sort) - Wyjaśnienie

## Opis
Sortowanie pozycyjne (Radix Sort) sortuje liczby cyfra po cyfrze, od najmniej znaczącej (LSD) lub najbardziej znaczącej (MSD). Używa stabilnego algorytmu pomocniczego (zwykle Counting Sort) do sortowania po każdej cyfrze. Nie opiera się na porównaniach.

## Złożoność Algorytmu

### Złożoność Czasowa
- **Zawsze**: **O(d · (n + k))**
  - d = liczba cyfr w największej liczbie
  - n = liczba elementów
  - k = podstawa systemu (10 dla dziesiętnego)

**Dla systemu dziesiętnego (k=10)**:
- O(d · n) gdy k jest stałe

**Przykład**:
- Sortowanie 1000 liczb 3-cyfrowych
- d = 3, n = 1000, k = 10
- O(3 · (1000 + 10)) = O(3030) ≈ O(n)

### Złożoność Pamięciowa
- **O(n + k)** - dla Counting Sort jako algorytmu pomocniczego

## Przypadki Szczególne

### Przypadek Optymistyczny
**Wszystkie liczby 1-cyfrowe**: [1, 5, 3, 9, 2]
- d = 1
- Złożoność: O(n) - jedna pętla Counting Sort

### Przypadek Pesymistyczny
**Bardzo długie liczby**: liczby o d >> log n cyfrach
- Złożoność: O(d·n) może być gorsza niż O(n log n)

**Przykład**:
```
n = 100, d = 1000 (1000-cyfrowe liczby)
Radix: O(1000 · 100) = O(100,000)
Quick Sort: O(100 · log 100) ≈ O(664)
→ Quick Sort lepszy!
```

## Stabilność Sortowania

**Algorytm jest STABILNY** ✓

**Dlaczego?**
- Używa stabilnego Counting Sort dla każdej cyfry
- Sortowanie od najmniej znaczącej cyfry (LSD) zachowuje względną kolejność
- Każdy krok sortowania zachowuje wyniki poprzedniego

**Przykład:**
```
[(123,a), (456,b), (123,c)]

Cyfra jednostek (3, 6, 3):
  Counting Sort: [(123,a), (123,c), (456,b)]
  
Cyfra dziesiątek (2, 2, 5):
  Counting Sort: [(123,a), (123,c), (456,b)]
  
Cyfra setek (1, 1, 4):
  Counting Sort: [(123,a), (123,c), (456,b)]

Wynik: [(123,a), (123,c), (456,b)]
       ↑        ↑
      (123,a) przed (123,c) - stabilne! ✓
```

## Warianty

### 1. LSD Radix Sort (Least Significant Digit)
- Sortuje od najmniej znaczącej cyfry
- **Wymaga stabilnego sortowania**
- Prostszy, częściej używany

### 2. MSD Radix Sort (Most Significant Digit)
- Sortuje od najbardziej znaczącej cyfry
- Rekurencyjny
- Może zakończyć wcześniej (jak Quick Sort)
- Bardziej skomplikowany

## Zalety i Wady

### Zalety
✓ **O(d·n) - liniowy** gdy d = O(1) lub d = O(log n)
✓ **Stabilny**
✓ **Deterministyczny** - zawsze ta sama złożoność
✓ **Prosty do implementacji** (LSD)
✓ **Nie używa porównań**
✓ **Efektywny dla liczb całkowitych**

### Wady
✗ **Tylko dla liczb całkowitych** (lub konwertowalnych)
✗ **O(d·n) może być > O(n log n)** dla dużego d
✗ **O(n+k) pamięci**
✗ **Nie in-place**
✗ **Wymaga znajomości d** (liczby cyfr)

## Zastosowania
- **Sortowanie liczb całkowitych** o ograniczonej liczbie cyfr
- **Sortowanie stringów** o stałej długości
- **Sortowanie dat** (YYYYMMDD)
- **Sortowanie adresów IP** (4 bajty)
- **Suffix arrays** w algorytmach tekstowych

## Optymalizacje

### 1. Większa podstawa (radix)
```
Zamiast podstawy 10, użyj podstawy 256 (bajt)
d zmniejsza się, ale k rośnie
Kompromis: często optymalne dla radix = 256
```

### 2. MSD z cutoff
```pseudocode
if n < 10 then {
  InsertionSort(A)
  return
}
// Kontynuuj MSD Radix Sort
```

### 3. Hybrydowy z Quick Sort
Dla długich liczb przełącz na Quick Sort.

## Przykład krok po kroku

```
Tablica: [170, 45, 75, 90, 802, 24, 2, 66]

Sortowanie po cyfrze jednostek:
  Count: [170, 90, 802, 2, 24, 45, 75, 66]
  
Sortowanie po cyfrze dziesiątek:
  Count: [802, 2, 24, 45, 66, 170, 75, 90]
  
Sortowanie po cyfrze setek:
  Count: [2, 24, 45, 66, 75, 90, 170, 802]

Wynik: [2, 24, 45, 66, 75, 90, 170, 802] ✓
```

## Porównanie z algorytmami porównaniowymi

**Kiedy Radix Sort lepszy?**
```
d ≤ log n  →  O(d·n) ≤ O(n log n)

Przykład:
n = 1,000,000 (milion)
d = 6 (liczby 6-cyfrowe)
log n ≈ 20

Radix: O(6·1,000,000) = 6M
Quick: O(1,000,000·20) = 20M
→ Radix 3x szybszy!
```

**Kiedy Quick Sort lepszy?**
```
d >> log n

Przykład:
n = 100
d = 100 (długie liczby)

Radix: O(100·100) = 10,000
Quick: O(100·7) = 700
→ Quick Sort 14x szybszy!
```

## Ciekawostki
1. **Herman Hollerith (1887)**: Użył w maszynie sortującej karty perforowane
2. **Najstarszy algorytm sortowania** używany komputerowo!
3. **Suffix Array**: Radix Sort używany w konstrukcji
4. **GPU**: Bardzo efektywny na kartach graficznych

````
