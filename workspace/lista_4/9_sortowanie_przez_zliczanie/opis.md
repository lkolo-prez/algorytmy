````markdown
# Sortowanie przez Zliczanie - Wyjaśnienie

## Opis
Sortowanie przez zliczanie (Counting Sort) to algorytm sortowania **nie oparty na porównaniach**. Zamiast porównywać elementy, liczy ile razy każda wartość występuje w tablicy. Działa efektywnie gdy zakres wartości (k) jest niewielki w porównaniu do liczby elementów (n). Jest to algorytm **liniowy O(n+k)**.

## Dane Wejściowe
- **n**: liczba elementów tablicy
- **A[1..n]**: tablica n **liczb całkowitych**
- Zakres wartości: [min_val, max_val]

## Wynik
**A[1..n]**: tablica posortowana rosnąco

## Strategia Rozwiązania

### Idea Algorytmu
1. **Znajdź zakres**: Określ min i max wartość w tablicy
2. **Zliczanie**: Policz ile razy każda wartość występuje
3. **Kumulatywne sumowanie**: Przekształć liczniki w pozycje
4. **Budowanie wyniku**: Umieść elementy na właściwych pozycjach
5. **Kopiowanie**: Skopiuj wynik do oryginalnej tablicy

### Krok po kroku
```
Tablica: [4, 2, 2, 8, 3, 3, 1]  (n=7)

Krok 1: Zakres
  min = 1, max = 8, k = 8

Krok 2: Zliczanie
  Count: [0,1,2,2,1,0,0,1]
  Indeks: 1 2 3 4 5 6 7 8
  Znaczenie: 1 wystąpił 1 raz, 2 wystąpił 2 razy, itd.

Krok 3: Kumulatywne sumowanie
  Count: [0,1,3,5,6,6,6,7]
  Znaczenie: pozycje końcowe dla każdej wartości

Krok 4: Budowanie wyniku (od końca!)
  A[7]=1: Output[Count[1]]=Output[1]←1, Count[1]←0
  A[6]=3: Output[Count[3]]=Output[5]←3, Count[3]←4
  A[5]=3: Output[Count[3]]=Output[4]←3, Count[3]←3
  A[4]=8: Output[Count[8]]=Output[7]←8, Count[8]←6
  A[3]=2: Output[Count[2]]=Output[3]←2, Count[2]←2
  A[2]=2: Output[Count[2]]=Output[2]←2, Count[2]←1
  A[1]=4: Output[Count[4]]=Output[6]←4, Count[4]←5

  Output: [1, 2, 2, 3, 3, 4, 8]

Wynik: [1, 2, 2, 3, 3, 4, 8]
```

## Złożoność Algorytmu

### Złożoność Czasowa
- **Zawsze**: **O(n + k)**
  - n - liczba elementów
  - k - zakres wartości (max - min + 1)

**Analiza kroków:**
1. Znajdź min/max: O(n)
2. Inicjalizacja Count: O(k)
3. Zliczanie: O(n)
4. Kumulatywne sumowanie: O(k)
5. Budowanie wyniku: O(n)
6. Kopiowanie: O(n)

**Łącznie**: O(n + k)

**Kiedy efektywny?**
- Gdy k = O(n), wtedy **O(n)** - liniowy!
- Gdy k >> n, wtedy O(k) - nieefektywny

### Złożoność Pamięciowa
- **O(n + k)**
  - Count[k]: O(k)
  - Output[n]: O(n)

## Przypadki Szczególne

### Przypadek Optymistyczny
**Mały zakres k ≈ n**: [1, 2, 3, 4, 5]
- k = 5, n = 5
- Złożoność: O(n) - **liniowa!**

### Przypadek Pesymistyczny
**Duży zakres k >> n**: [1, 1000000]
- k = 1000000, n = 2
- Złożoność: O(k) - bardzo nieefektywny!
- Count[1000000] - ogromna tablica

**Wniosek**: Counting Sort działa **tylko** gdy k = O(n)

## Stabilność Sortowania

**Algorytm jest STABILNY** ✓ (jeśli budujemy od końca)

**Dlaczego?**
Budując wynik **od końca tablicy wejściowej**, zachowujemy względną kolejność równych elementów.

**Przykład stabilności:**
```
Wejście: [(2,a), (1,b), (2,c), (1,d)]

Zliczanie:
  Count[1] = 2  (indeksy: 2, 4)
  Count[2] = 2  (indeksy: 1, 3)

Kumulatywne:
  Count[1] = 2  (pozycje 1-2)
  Count[2] = 4  (pozycje 3-4)

Budowanie od końca:
  i=4: (1,d) → Output[2] ← (1,d), Count[1]=1
  i=3: (2,c) → Output[4] ← (2,c), Count[2]=3
  i=2: (1,b) → Output[1] ← (1,b), Count[1]=0
  i=1: (2,a) → Output[3] ← (2,a), Count[2]=2

Wynik: [(1,b), (1,d), (2,a), (2,c)]
        ↑      ↑      ↑      ↑
       (1,b) przed (1,d) ✓
       (2,a) przed (2,c) ✓
```

**Uwaga**: Jeśli budujemy od początku, algorytm staje się niestabilny!

## Zalety i Wady

### Zalety
✓ **O(n) gdy k=O(n)** - liniowa złożoność!
✓ **Stabilny** (przy właściwej implementacji)
✓ **Prosty do zrozumienia**
✓ **Deterministyczny** - zawsze ta sama złożoność
✓ **Podstawa dla Radix Sort**
✓ **Świetny dla małych zakresów** (np. oceny 1-6)

### Wady
✗ **Tylko dla liczb całkowitych** (lub dyskretnych wartości)
✗ **O(k) pamięci** - duży zakres = dużo pamięci
✗ **Nieefektywny dla dużego k**
✗ **Nie działa dla liczb rzeczywistych**
✗ **Wymaga znajomości zakresu**

## Zastosowania
- **Małe zakresy wartości**: oceny (1-10), wiek (0-150), kod ASCII (0-255)
- **Jako część Radix Sort**: sortowanie cyfr
- **Histogram**: zliczanie wystąpień
- **Preprocessing**: przed innymi algorytmami
- **Statystyki**: gdy potrzebujemy rozkładu wartości

## Przykłady praktyczne

### 1. Sortowanie ocen (1-6)
```
n = 1000 studentów
k = 6 ocen
O(1000 + 6) = O(1000) - doskonałe!
```

### 2. Sortowanie wieku (0-150)
```
n = 1000000 osób
k = 151
O(1000000 + 151) ≈ O(n) - świetne!
```

### 3. Sortowanie liczb (1-1000000)
```
n = 100 liczb
k = 1000000
O(100 + 1000000) = O(1000000) - fatalne!
Lepszy Quick Sort: O(100 log 100) ≈ O(664)
```

## Optymalizacje

### 1. Offset dla ujemnych liczb
```pseudocode
offset ← -min_val
for i ← 1 to n do {
  Count[A[i] + offset] ← Count[A[i] + offset] + 1
}
```

### 2. W miejscu (in-place) - trudne!
- Możliwe ale skomplikowane
- Traci stabilność
- Rzadko używane

### 3. Częściowe sortowanie
Jeśli potrzebujemy tylko top-k elementów, możemy przerwać wcześniej.

## Porównanie z algorytmami porównaniowymi

| Algorytm | Złożoność | Zakres danych |
|----------|-----------|---------------|
| Counting Sort | O(n+k) | Liczby całkowite, k=O(n) |
| Quick Sort | O(n log n) | Dowolne |
| Merge Sort | O(n log n) | Dowolne |
| Heap Sort | O(n log n) | Dowolne |

**Wniosek**: 
- Counting Sort: **szybszy** gdy k=O(n)
- Algorytmy porównaniowe: **uniwersalniejsze**

## Dolna granica sortowania

**Twierdzenie**: Każdy algorytm sortowania **oparty na porównaniach** wymaga Ω(n log n) porównań.

**Counting Sort łamie tę barierę!** Jak?
- **Nie używa porównań** elementów
- Działa na dyskretnych wartościach
- Używa indeksowania zamiast porównań

## Warianty

### 1. Counting Sort dla obiektów
```pseudocode
// Zliczamy klucze, przechowujemy obiekty
Count[klucz(obj)]++
```

### 2. Counting Sort z histogramem
```pseudocode
// Tylko zliczanie, bez sortowania
for i ← 1 to n do {
  Count[A[i]]++
}
return Count  // histogram
```

### 3. Radix Sort
- Wielokrotne zastosowanie Counting Sort
- Sortowanie po cyfrach
- Patrz: osobne zadanie

## Ciekawostki
1. **Harold H. Seward (1954)**: Pierwszy opis algorytmu
2. **Nie jest "sortowaniem"**: To bardziej "indeksowanie"
3. **Quantum sort**: W informatyce kwantowej możliwe O(1)!
4. **MapReduce**: Counting Sort używany w rozproszonych systemach

````
