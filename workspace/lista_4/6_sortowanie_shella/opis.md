````markdown
# Sortowanie metodą Shella (Malejących Przyrostów) - Wyjaśnienie

## Opis
Sortowanie Shella (Shell Sort) jest uogólnieniem sortowania przez wstawianie. Algorytm porównuje elementy oddalone od siebie o pewien odstęp (gap), zamiast tylko sąsiadujące. Odstęp ten jest stopniowo zmniejszany aż do 1, kiedy algorytm staje się zwykłym insertion sort - ale wtedy tablica jest już prawie posortowana. Opracowany przez Donalda Shella w 1959 roku.

## Dane Wejściowe
- **n**: liczba elementów tablicy (n > 0)
- **A[1..n]**: tablica n liczb do posortowania

## Wynik
**A[1..n]**: tablica posortowana rosnąco

## Strategia Rozwiązania

### Idea Algorytmu
1. Zacznij od dużego odstępu (gap), np. n/2
2. Sortuj elementy oddalone o gap (insertion sort z krokiem gap)
3. Zmniejsz gap (np. gap = gap/2)
4. Powtarzaj aż gap = 1
5. Dla gap = 1 wykonaj zwykły insertion sort (ale tablica już prawie posortowana!)

### Dlaczego to działa?
**Problem insertion sort**: małe elementy na końcu poruszają się powoli (po 1 pozycji)
**Rozwiązanie Shell sort**: duże odstępy przenoszą małe elementy szybko na początek

### Krok po kroku
```
Tablica: [35, 33, 42, 10, 14, 19, 27, 44]  (n=8)

Gap = 4:
  Sortuj [35, 14], [33, 19], [42, 27], [10, 44]
  Wynik: [14, 19, 27, 10, 35, 33, 42, 44]

Gap = 2:
  Sortuj [14, 27, 35, 42], [19, 10, 33, 44]
  Wynik: [14, 10, 27, 19, 35, 33, 42, 44]

Gap = 1:
  Zwykły insertion sort
  Wynik: [10, 14, 19, 27, 33, 35, 42, 44]
```

## Złożoność Algorytmu

### Złożoność Czasowa - ZALEŻY OD SEKWENCJI GAP!

**Sekwencja Shella (n/2, n/4, ..., 1)**:
- **Pesymistyczna**: O(n²)
- **Średnia**: O(n^(3/2)) lub O(n log² n)
- Nie najlepsza sekwencja!

**Sekwencja Hibbarda (2^k - 1: 1, 3, 7, 15, 31, ...)**:
- **Pesymistyczna**: O(n^(3/2))
- Lepsza niż Shella

**Sekwencja Sedgewicka (najlepsza znana)**:
- **Średnia**: O(n^(4/3))
- **Pesymistyczna**: O(n^(4/3))

**Sekwencja Pratt**:
- **Pesymistyczna**: O(n log² n)

### Złożoność Pamięciowa
- **O(1)** - sortowanie w miejscu

### Uwaga
Dokładna złożoność Shell Sort **nie jest w pełni znana** - to nadal otwarty problem w informatyce!

## Przypadki Szczególne

### Przypadek Optymistyczny
**Tablica posortowana**: [1, 2, 3, 4, 5]
- Zależy od sekwencji gap
- Dla gap = n/2, n/4, ..., 1:
  - Każdy gap wymaga O(n) operacji
  - Łącznie: O(n log n)

### Przypadek Pesymistyczny
**Tablica odwrotnie posortowana**: [5, 4, 3, 2, 1]
- Dla sekwencji Shella: O(n²)
- Dla sekwencji Sedgewicka: O(n^(4/3))

## Stabilność Sortowania

**Algorytm jest NIESTABILNY** ✗

**Dlaczego?**
Elementy oddalone o gap mogą być zamieniane, co narusza względną kolejność równych elementów.

**Przykład niestabilności:**
```
[(4,a), (2,b), (4,c), (2,d), (1,e)] (n=5)

Gap = 2:
  Porównaj indeksy: [1,3,5] i [2,4]
  (4,a) z (4,c): bez zamiany
  (4,c) z (1,e): zamień → [(4,a), (2,b), (1,e), (2,d), (4,c)]
                                                         ↑
                          (4,c) przeskoczyło (4,a)!

Gap = 1:
  Insertion sort: [(1,e), (2,b), (2,d), (4,c), (4,a)]
                                         ↑      ↑
                  (4,c) przed (4,a) - niestabilne!
```

## Zalety i Wady

### Zalety
✓ Szybszy niż proste algorytmy O(n²) dla większości danych
✓ Prosty do implementacji
✓ Sortowanie w miejscu (O(1) pamięci)
✓ Adaptywny - działa dobrze na prawie posortowanych danych
✓ Brak degeneracji do O(n²) (dla dobrych sekwencji)
✓ Efektywny dla średnich rozmiarów danych (n < 5000)

### Wady
✗ Nie jest stabilny
✗ Złożoność zależy od wyboru sekwencji gap
✗ Suboptymalne O(n log n) dla dobrych algorytmów
✗ Trudno zrównoleglić
✗ Nie ma gwarancji O(n log n)

## Sekwencje Gap

### 1. Sekwencja Shella (oryginalna)
```
gap[k] = n / 2^k
Przykład: n=100 → [50, 25, 12, 6, 3, 1]
```
- Najprostsza
- O(n²) w najgorszym przypadku

### 2. Sekwencja Hibbard
```
gap[k] = 2^k - 1
Przykład: [1, 3, 7, 15, 31, 63, ...]
```
- O(n^(3/2)) pesymistyczna
- Lepsza od Shella

### 3. Sekwencja Sedgewick
```
gap[k] = 9*4^k - 9*2^k + 1  lub  4^k - 3*2^k + 1
Przykład: [1, 5, 19, 41, 109, ...]
```
- Najlepsza znana sekwencja
- O(n^(4/3)) średnia

### 4. Sekwencja Ciury
```
[1, 4, 10, 23, 57, 132, 301, 701, ...]
```
- Empirycznie najlepsza dla małych n
- Wyznaczona eksperymentalnie

## Zastosowania
- Średnie zbiory danych (1000 < n < 50000)
- Systemy embedded (niski narzut pamięci)
- Gdy quick sort może zdegenerować się
- Algorytmy hybrydowe
- Praktyczne zastosowania gdzie prostota > optymalność

## Porównanie z innymi algorytmami

| Algorytm | Złożoność | Pamięć | Stabilny |
|----------|-----------|--------|----------|
| Shell Sort | O(n^(4/3)) - O(n²) | O(1) | ✗ |
| Insertion Sort | O(n²) | O(1) | ✓ |
| Merge Sort | O(n log n) | O(n) | ✓ |
| Quick Sort | O(n log n) śr. | O(log n) | ✗ |
| Heap Sort | O(n log n) | O(1) | ✗ |

**Wniosek**: Shell Sort to "złoty środek" - lepszy od O(n²), prostszy od O(n log n).

## Optymalizacje

### 1. Dobór sekwencji gap
Użyj sekwencji Sedgewicka lub Ciury zamiast n/2.

### 2. Przełączanie na Insertion Sort
Gdy gap=1, użyj zoptymalizowanego insertion sort.

### 3. Hybrydowe podejście
- Użyj Shell Sort dla małych partycji w Quick Sort
- Komplementarne do Introsort

## Historia
- **1959**: Donald Shell publikuje algorytm
- **1963**: Pierwsza analiza przez Papernova i Stasevich
- **2001**: Ciura znajduje empirycznie najlepszą sekwencję dla małych n
- **Dziś**: Nadal używany w praktyce, zwłaszcza w systemach embedded

## Ciekawostki
1. **Otwarty problem**: Dokładna złożoność dla wielu sekwencji gap jest nieznana!
2. **Rekord**: Sekwencja Pratt gwarantuje O(n log² n), ale w praktyce wolniejsza
3. **Linux kernel**: Używa wariantu Shell Sort w niektórych miejscach
4. **uClibc**: Implementacja `qsort()` używa Shell Sort dla małych n

````
