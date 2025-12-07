````markdown
# Sortowanie przez Proste Wybieranie - Wyjaśnienie

## Opis
Sortowanie przez proste wybieranie (Selection Sort) to algorytm sortowania, który działa przez wielokrotne znajdowanie elementu minimalnego z nieposortowanej części tablicy i umieszczanie go na początku. Algorytm dzieli tablicę na część posortowaną (na początku pustą) i nieposortowaną.

## Dane Wejściowe
- **n**: liczba elementów tablicy (n > 0)
- **A[1..n]**: tablica n liczb do posortowania

## Wynik
**A[1..n]**: tablica posortowana rosnąco

## Strategia Rozwiązania

### Idea Algorytmu
1. Podziel tablicę na część posortowaną (początkowo pustą) i nieposortowaną (cała tablica)
2. W każdej iteracji znajdź minimum w części nieposortowanej
3. Zamień to minimum z pierwszym elementem części nieposortowanej
4. Przesuń granicę części posortowanej o jeden element w prawo
5. Powtarzaj aż cała tablica będzie posortowana

### Krok po kroku
```
Początkowa tablica: [64, 25, 12, 22, 11]

i=1, min=11 (idx=5): [11, 25, 12, 22, 64]
i=2, min=12 (idx=3): [11, 12, 25, 22, 64]
i=3, min=22 (idx=4): [11, 12, 22, 25, 64]
i=4, min=25 (idx=4): [11, 12, 22, 25, 64]

Posortowana: [11, 12, 22, 25, 64]
```

## Złożoność Algorytmu

### Złożoność Czasowa
- **Pesymistyczna (Worst Case)**: O(n²)
- **Optymistyczna (Best Case)**: O(n²)
- **Średnia (Average Case)**: O(n²)

**Uwaga**: Selection Sort ma **zawsze** złożoność O(n²), niezależnie od wejścia!

**Dlaczego zawsze O(n²)?**
- Zewnętrzna pętla: n-1 iteracji
- Wewnętrzna pętla w i-tej iteracji: n-i porównań
- Całkowita liczba porównań: (n-1) + (n-2) + ... + 1 = n(n-1)/2 ≈ n²/2
- Ta liczba jest stała dla każdego wejścia

### Złożoność Pamięciowa
- **O(1)** - sortowanie w miejscu (in-place)
- Potrzebujemy tylko zmiennych: i, j, min_idx, temp

## Przypadki Szczególne

### Przypadek Optymistyczny
**Tablica posortowana rosnąco**: [1, 2, 3, 4, 5]
- Złożoność: **O(n²)** (nie O(n)!)
- Algorytm nadal wykonuje wszystkie porównania
- Mniej zamian (żadnej lub minimalna liczba), ale liczba porównań pozostaje taka sama
- **To odróżnia Selection Sort od Insertion Sort**

### Przypadek Pesymistyczny
**Tablica posortowana malejąco**: [5, 4, 3, 2, 1]
- Złożoność: O(n²)
- Maksymalna liczba zamian (n-1)
- Liczba porównań taka sama jak zawsze

### Przypadek Średni
**Tablica losowa**: [3, 1, 4, 2, 5]
- Złożoność: O(n²)
- Średnia liczba zamian

## Stabilność Sortowania

**Algorytm jest NIESTABILNY** ✗

**Dlaczego nie jest stabilny?**
Zamiany elementów mogą naruszyć względną kolejność równych elementów.

**Przykład niestabilności:**
```
Wejście:  [(4,a), (2,b), (4,c), (1,d)]

i=1: szukamy min → 1 → zamieniamy (4,a) ↔ (1,d)
     [(1,d), (2,b), (4,c), (4,a)]
     
i=2: szukamy min → 2 → bez zamiany
     [(1,d), (2,b), (4,c), (4,a)]
     
i=3: szukamy min → 4 → bez zamiany
     [(1,d), (2,b), (4,c), (4,a)]

Wyjście:  [(1,d), (2,b), (4,c), (4,a)]
```

Zauważ, że (4,a) i (4,c) zmieniły kolejność! Oryginalnie (4,a) było przed (4,c), a teraz jest odwrotnie.

**Stabilna wersja Selection Sort:**
Możliwe jest stworzenie stabilnej wersji, ale wymaga to przesuwania elementów zamiast zamiany, co zwiększa złożoność do O(n²) przestrzennie.

## Zalety i Wady

### Zalety
✓ Prosty do zrozumienia i implementacji
✓ Sortowanie w miejscu (O(1) pamięci)
✓ Minimalna liczba zamian - dokładnie (n-1) zamian
✓ Dobry gdy koszt zamiany jest bardzo wysoki
✓ Wydajność nie zależy od rozkładu danych wejściowych

### Wady
✗ Nieefektywny dla dużych zbiorów (O(n²))
✗ Nie jest stabilny
✗ Zawsze wykonuje O(n²) porównań, nawet dla posortowanych danych
✗ Nie jest adaptywny
✗ Nie nadaje się do sortowania online

## Zastosowania
- Sytuacje gdzie koszt zamiany jest bardzo wysoki (np. sortowanie dużych obiektów)
- Małe zbiory danych
- Gdy zależy nam na minimalnej liczbie zamian
- Systemy z ograniczoną pamięcią
- Edukacja - prosty przykład algorytmu sortowania

## Porównanie z innymi algorytmami

### vs Insertion Sort
- **Selection Sort**: zawsze O(n²), niestabilny, minimalna liczba zamian
- **Insertion Sort**: O(n) dla posortowanych, O(n²) w najgorszym, stabilny
- **Wniosek**: Insertion Sort zazwyczaj lepszy w praktyce

### vs Bubble Sort
- **Selection Sort**: mniej zamian O(n)
- **Bubble Sort**: więcej zamian O(n²)
- **Wniosek**: Selection Sort lepszy gdy zamiany są kosztowne

### vs Quick Sort / Merge Sort
- Algorytmy O(n log n) są znacznie szybsze dla dużych zbiorów
- Selection Sort prostszy, lepszy dla bardzo małych n

## Liczba operacji

Dla tablicy rozmiaru n:
- **Porównania**: n(n-1)/2 ≈ n²/2 (zawsze)
- **Zamiany**: maksymalnie n-1 (minimalna możliwa liczba)
- **Przypisania**: 3(n-1) dla zamian

**Przykład dla n=5:**
- Porównania: 10
- Zamiany: maksymalnie 4

## Optymalizacje

1. **Podwójny Selection Sort (Double Selection Sort)**:
   - W każdej iteracji znajdujemy zarówno minimum jak i maksimum
   - Umieszczamy minimum na początku, maksimum na końcu
   - Redukuje liczbę iteracji o połowę
   - Nadal O(n²)

2. **Heap Sort**:
   - Udoskonalona wersja selection sort używająca kopca
   - Złożoność O(n log n)
   - Bardziej skomplikowana implementacja

````
