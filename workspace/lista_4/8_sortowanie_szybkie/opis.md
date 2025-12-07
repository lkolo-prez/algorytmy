````markdown
# Sortowanie Szybkie (Quick Sort) - Wyjaśnienie

## Opis
Sortowanie szybkie (Quick Sort) to jeden z najszybszych i najpopularniejszych algorytmów sortowania w praktyce. Wykorzystuje paradygmat "dziel i zwyciężaj". Wybiera element zwany pivotem, dzieli tablicę na dwie części (mniejsze i większe od pivota), a następnie rekurencyjnie sortuje obie części. Opracowany przez Tony'ego Hoare'a w 1960 roku.

## Dane Wejściowe
- **n**: liczba elementów tablicy (n > 0)
- **A[1..n]**: tablica n liczb do posortowania

## Wynik
**A[1..n]**: tablica posortowana rosnąco

## Strategia Rozwiązania

### Idea Algorytmu
1. **Wybierz pivot** (element podziału, np. ostatni element)
2. **Partycjonuj**: Podziel tablicę tak, że:
   - Elementy mniejsze od pivota są po lewej
   - Elementy większe od pivota są po prawej
   - Pivot jest na właściwej pozycji
3. **Rekurencyjnie sortuj** lewą i prawą część

### Krok po kroku
```
[10, 7, 8, 9, 1, 5]  pivot=5

Partycjonowanie:
  1 < 5 → lewa strona
  7 > 5 → prawa strona
  8 > 5 → prawa strona
  9 > 5 → prawa strona
  10 > 5 → prawa strona

Po partycjonowaniu: [1, 5, 8, 9, 7, 10]
                        ↑
                      pivot na miejscu!

Rekursja:
  Lewo: [1]           → posortowane
  Prawo: [8,9,7,10]   → sortuj rekurencyjnie
    pivot=10
    [7,8,9,10]

Wynik: [1, 5, 7, 8, 9, 10]
```

## Złożoność Algorytmu

### Złożoność Czasowa
- **Średnia (Average Case)**: **O(n log n)** ✓
  - Najczęstszy przypadek
  - Dobry wybór pivota dzieli tablicę mniej więcej na połowę

- **Optymistyczna (Best Case)**: **O(n log n)**
  - Pivot zawsze dzieli tablicę na równe połowy
  - Głębokość rekursji: log n
  - Na każdym poziomie: n operacji

- **Pesymistyczna (Worst Case)**: **O(n²)** ✗
  - Pivot zawsze jest najmniejszy lub największy
  - Głębokość rekursji: n
  - Przykład: tablica już posortowana z pivotem jako ostatni element

**Analiza:**
```
Best/Average: T(n) = 2T(n/2) + O(n) = O(n log n)
Worst: T(n) = T(n-1) + O(n) = O(n²)
```

### Złożoność Pamięciowa
- **Średnia**: O(log n) - stos rekursji
- **Pesymistyczna**: O(n) - niezbalansowana rekursja

## Przypadki Szczególne

### Przypadek Optymistyczny
**Pivot zawsze w środku**: 
- Złożoność: O(n log n)
- Idealne zbalansowanie

### Przypadek Pesymistyczny
**Tablica posortowana, pivot=ostatni**: [1,2,3,4,5]
```
pivot=5: [1,2,3,4] | [5]
pivot=4: [1,2,3] | [4] | [5]
pivot=3: [1,2] | [3] | [4] | [5]
...
→ O(n²) degeneracja!
```

### Przypadek Średni
**Tablica losowa**: 
- Złożoność: O(n log n)
- Bardzo szybki w praktyce

## Stabilność Sortowania

**Algorytm jest NIESTABILNY** ✗

**Dlaczego?**
Partycjonowanie może zamienić równe elementy miejscami.

**Przykład:**
```
[(3,a), (1,b), (3,c), (2,d)]  pivot=(2,d)

Partycjonowanie:
  (1,b) < (2,d) → lewo
  (3,a) > (2,d) → prawo
  (3,c) > (2,d) → prawo
  
[(1,b), (2,d), (3,c), (3,a)]
                ↑      ↑
           (3,c) przed (3,a) - niestabilne!
```

## Zalety i Wady

### Zalety
✓ **Bardzo szybki w praktyce** - często najszybszy
✓ **O(n log n) średnio** - dobra złożoność
✓ **Sortowanie w miejscu** - O(log n) pamięci
✓ **Cache-friendly** - dobry dla lokalności pamięci
✓ **Prosty do implementacji** (wersja podstawowa)
✓ **Łatwo zrównoleglić**

### Wady
✗ **O(n²) w najgorszym przypadku** - bez optymalizacji
✗ **Niestabilny**
✗ **Rekurencyjny** - narzut stosu
✗ **Wymaga dobrego wyboru pivota**

## Wybór Pivota

### 1. Ostatni element (podstawowa)
```pseudocode
pivot ← A[high]
```
- Najprostszy
- O(n²) dla posortowanych!

### 2. Losowy element
```pseudocode
idx ← random(low, high)
zamień A[idx] ↔ A[high]
pivot ← A[high]
```
- Unika O(n²) dla posortowanych
- Oczekiwana złożoność: O(n log n)

### 3. Median-of-three
```pseudocode
mid ← (low + high) / 2
mediana ← median(A[low], A[mid], A[high])
```
- Jeszcze lepszy wybór
- Używany w praktycznych implementacjach

### 4. Ninther (mediana median)
- Mediana z 9 elementów
- Bardzo dobry, ale kosztowny

## Optymalizacje

### 1. Introsort (Introspective Sort)
```pseudocode
if głębokość_rekursji > 2*log(n) then {
  HeapSort(A)  // unikamy O(n²)
} else {
  QuickSort(A)
}
```
- Używany w C++ `std::sort()`
- Gwarantuje O(n log n)

### 2. Hybrydowe z Insertion Sort
```pseudocode
if n < 10 then {
  InsertionSort(A)
  return
}
// Kontynuuj Quick Sort
```
- Dla małych partycji insertion sort szybszy

### 3. Trzywymiarowe partycjonowanie
```
[< pivot] [== pivot] [> pivot]
```
- Efektywne dla wielu duplikatów
- Algorytm Dijkstry (Dutch National Flag)

### 4. Tail recursion elimination
```pseudocode
while low < high do {
  pi ← Partition(A, low, high)
  if pi - low < high - pi then {
    QuickSort(A, low, pi-1)
    low ← pi + 1  // zamiast rekursji
  } else {
    QuickSort(A, pi+1, high)
    high ← pi - 1
  }
}
```
- Redukuje pamięć do O(log n)

## Zastosowania
- **Standardowe biblioteki**: C `qsort()`, C++ (częściowo)
- **Ogólnego przeznaczenia**: domyślny wybór
- **Duże zbiory danych** w pamięci
- **Gdy stabilność nieważna**
- **Systemy czasu rzeczywistego** (z Introsort)

## Porównanie

| Algorytm | Średnia | Najgorsza | Pamięć | Stabilny |
|----------|---------|-----------|--------|----------|
| Quick Sort | O(n log n) | O(n²)* | O(log n) | ✗ |
| Merge Sort | O(n log n) | O(n log n) | O(n) | ✓ |
| Heap Sort | O(n log n) | O(n log n) | O(1) | ✗ |

*Z randomizacją oczekiwana O(n log n)

## Warianty

### Dual-Pivot Quick Sort
- Dwa pivoty zamiast jednego
- Używany w Java 7+ `Arrays.sort()`
- Około 10% szybszy niż klasyczny

### Quick Select
- Wariant do znajdowania k-tego najmniejszego
- O(n) średnio

## Historia
- **1960**: Tony Hoare opracowuje algorytm
- **1962**: Pierwsza publikacja
- **Najpopularniejszy algorytm sortowania!**
- **Turing Award 1980**: Hoare otrzymuje za wkład do informatyki

````
