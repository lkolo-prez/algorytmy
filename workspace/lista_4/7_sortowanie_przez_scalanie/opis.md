````markdown
# Sortowanie przez Scalanie - Wyjaśnienie

## Opis
Sortowanie przez scalanie (Merge Sort) to klasyczny algorytm wykorzystujący paradygmat "dziel i zwyciężaj". Algorytm rekurencyjnie dzieli tablicę na mniejsze części, sortuje je, a następnie scala posortowane fragmenty. Opracowany przez Johna von Neumanna w 1945 roku. Jest to jeden z najbardziej efektywnych i stabilnych algorytmów sortowania.

## Dane Wejściowe
- **n**: liczba elementów tablicy (n > 0)
- **A[1..n]**: tablica n liczb do posortowania

## Wynik
**A[1..n]**: tablica posortowana rosnąco

## Strategia Rozwiązania

### Idea Algorytmu (Divide and Conquer)
1. **DZIEL (Divide)**: Podziel tablicę na dwie równe połowy
2. **ZWYCIĘŻAJ (Conquer)**: Rekurencyjnie sortuj obie połowy
3. **SCAL (Merge)**: Scal dwie posortowane połowy w jedną posortowaną tablicę

### Kluczowa operacja: Scalanie
Scalanie dwóch posortowanych tablic do jednej:
```
L = [2, 5, 8]     R = [1, 3, 7]

Krok 1: 1 < 2 → wynik: [1]
Krok 2: 2 < 3 → wynik: [1, 2]
Krok 3: 3 < 5 → wynik: [1, 2, 3]
Krok 4: 5 < 7 → wynik: [1, 2, 3, 5]
Krok 5: 7 < 8 → wynik: [1, 2, 3, 5, 7]
Krok 6: pozostałe → wynik: [1, 2, 3, 5, 7, 8]
```

### Krok po kroku
```
[38, 27, 43, 3, 9, 82, 10]

DZIELENIE:
         [38, 27, 43, 3, 9, 82, 10]
           /                    \
    [38, 27, 43, 3]          [9, 82, 10]
      /        \               /      \
  [38, 27]   [43, 3]      [9, 82]    [10]
   /    \     /    \       /    \       |
 [38]  [27] [43]  [3]    [9]  [82]   [10]

SCALANIE:
 [38]  [27] [43]  [3]    [9]  [82]   [10]
   \    /     \    /       \    /       |
  [27,38]   [3,43]       [9,82]      [10]
      \        /             \          /
   [3,27,38,43]           [9,10,82]
         \                    /
      [3,9,10,27,38,43,82]
```

## Złożoność Algorytmu

### Złożoność Czasowa
- **Pesymistyczna (Worst Case)**: O(n log n)
- **Optymistyczna (Best Case)**: O(n log n)
- **Średnia (Average Case)**: O(n log n)

**Zawsze O(n log n)** - nie zależy od danych wejściowych!

**Dlaczego O(n log n)?**
- Głębokość rekursji: log n (dzielimy przez 2)
- Na każdym poziomie: n operacji (scalanie)
- Łącznie: n * log n

**Drzewo rekursji:**
```
Poziom 0: n elementów           → n operacji
Poziom 1: 2 grupy po n/2        → 2*(n/2) = n operacji
Poziom 2: 4 grupy po n/4        → 4*(n/4) = n operacji
...
Poziom log n: n grup po 1       → n*1 = n operacji

Suma: n * log n
```

### Złożoność Pamięciowa
- **O(n)** - potrzebujemy dodatkowej pamięci na tablice pomocnicze
- Nie jest sortowaniem w miejscu (in-place)
- Każde scalanie wymaga tymczasowych tablic L[] i R[]

## Przypadki Szczególne

### Przypadek Optymistyczny
**Tablica posortowana**: [1, 2, 3, 4, 5]
- Złożoność: **O(n log n)** (nie O(n)!)
- Algorytm zawsze wykonuje wszystkie dzielenia i scalania
- Nie jest adaptywny

### Przypadek Pesymistyczny
**Tablica odwrotnie posortowana**: [5, 4, 3, 2, 1]
- Złożoność: **O(n log n)**
- Tak samo jak dla posortowanej!
- To jest **zaleta** - przewidywalna wydajność

### Przypadek Średni
**Tablica losowa**: [3, 1, 4, 2, 5]
- Złożoność: **O(n log n)**
- Zawsze taka sama!

## Stabilność Sortowania

**Algorytm jest STABILNY** ✓

**Dlaczego jest stabilny?**
W operacji scalania, gdy `L[i] <= R[j]` (not strict!), bierzemy element z L.
To zachowuje względną kolejność równych elementów.

**Przykład stabilności:**
```
Wejście: [(3,a), (1,b), (3,c), (2,d)]

Dzielenie: [(3,a), (1,b)] | [(3,c), (2,d)]

Rekursja lewa:  [(3,a), (1,b)] → [(1,b), (3,a)]
Rekursja prawa: [(3,c), (2,d)] → [(2,d), (3,c)]

Scalanie: [(1,b), (3,a)] i [(2,d), (3,c)]
  1 < 2: [1,b]
  2 < 3: [1,b, 2,d]
  (3,a) <= (3,c): [1,b, 2,d, 3,a]  ← bierzemy z lewej!
  Pozostałe: [1,b, 2,d, 3,a, 3,c]

Wynik: [(1,b), (2,d), (3,a), (3,c)]
       (3,a) przed (3,c) - stabilność zachowana! ✓
```

## Zalety i Wady

### Zalety
✓ **Gwarantowane O(n log n)** - bez degeneracji do O(n²)
✓ **Stabilny** - zachowuje względną kolejność
✓ **Przewidywalny** - wydajność nie zależy od danych
✓ **Równoległy** - łatwo zrównoleglić
✓ **Dobry dla dużych danych** - równomierny dostęp do pamięci
✓ **Zewnętrzny** - świetny dla sortowania na dysku
✓ **Teorytycznie optymalny** - dla sortowania porównaniowego

### Wady
✗ **O(n) pamięci** - wymaga dodatkowej pamięci
✗ **Nie in-place** - nie sortuje w miejscu
✗ **Narzut rekursji** - głębokość log n
✗ **Wolniejszy od Quick Sort** w praktyce (dla małych n)
✗ **Nie adaptywny** - nie wykorzystuje częściowego sortowania

## Zastosowania
- **Sortowanie zewnętrzne** (duże pliki na dysku)
- **Gdy stabilność jest wymagana**
- **Gdy O(n log n) musi być gwarantowane**
- **Linked lists** (bez narzutu pamięci!)
- **Równoległe sortowanie** (paralelizacja)
- **Python** (Timsort - hybrydowy z merge sort)
- **Java** (sortowanie obiektów - stabilność)

## Warianty

### 1. Bottom-Up Merge Sort (iteracyjny)
```pseudocode
// Zamiast rekursji - iteracyjnie scalamy
rozmiar ← 1
while rozmiar < n do {
  for i ← 1 to n step 2*rozmiar do {
    scal(A, i, i+rozmiar-1, min(i+2*rozmiar-1, n))
  }
  rozmiar ← rozmiar * 2
}
```
- Eliminuje rekursję (O(1) pamięć stosu)
- Lepszy dla cache'a
- Używany w implementacjach praktycznych

### 2. Natural Merge Sort
- Wykrywa naturalnie posortowane fragmenty
- Adaptywny - O(n) dla posortowanych
- Bardziej skomplikowany

### 3. In-Place Merge Sort
- Scalanie bez dodatkowej pamięci
- O(1) pamięć, ale O(n log² n) czas
- Rzadko używany (trudny i wolny)

## Porównanie z Quick Sort

| Cecha | Merge Sort | Quick Sort |
|-------|------------|------------|
| Worst Case | O(n log n) ✓ | O(n²) ✗ |
| Average Case | O(n log n) | O(n log n) |
| Pamięć | O(n) ✗ | O(log n) ✓ |
| Stabilny | ✓ | ✗ |
| Adaptywny | ✗ | ✗ |
| Cache-friendly | ✗ | ✓ |
| Praktyczna szybkość | Wolniejszy | Szybszy |

**Wniosek**: 
- **Merge Sort**: gdy stabilność lub gwarancja O(n log n) są ważne
- **Quick Sort**: gdy szybkość i pamięć są ważniejsze

## Optymalizacje

### 1. Hybrydowe z Insertion Sort
```pseudocode
if prawy - lewy <= 15 then {
  InsertionSort(A, lewy, prawy)
  return
}
// Kontynuuj merge sort
```
- Dla małych n insertion sort jest szybszy
- Zmniejsza narzut rekursji

### 2. Timsort (Python)
- Hybrydowy Merge Sort + Insertion Sort
- Wykrywa "runs" (posortowane fragmenty)
- Adaptywny - O(n) dla prawie posortowanych
- Używany w Python, Java (sort obiektów)

### 3. Równoległość
```
Lewa połowa  | Prawa połowa
      ↓      |       ↓
  Thread 1   |   Thread 2
      ↓      |       ↓
   Scalanie (jednowątkowe)
```

## Analiza szczegółowa

Dla n=8:
```
Poziom 0 (dzielenie): 1 operacja
Poziom 1 (dzielenie): 2 operacje
Poziom 2 (dzielenie): 4 operacje
Poziom 3: 8 pojedynczych elementów

Poziom 3 (scalanie): 8 porównań
Poziom 2 (scalanie): 8 porównań
Poziom 1 (scalanie): 8 porównań
Poziom 0 (scalanie): 8 porównań

Łącznie: 3 * 8 = 24 operacje = 8 * log₂(8) = 8 * 3 ✓
```

## Historia i ciekawostki
- **1945**: John von Neumann opracowuje algorytm dla EDVAC
- **Jeden z pierwszych algorytmów komputerowych!**
- **Zewnętrzne sortowanie**: wynaleziony właśnie do tego
- **Stabilność**: była zamierzonym aspektem projektu
- **Równoległość**: naturalnie równoległy algorytm

````
