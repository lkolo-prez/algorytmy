````markdown
# Sortowanie przez Wstawianie Połówkowe - Wyjaśnienie

## Opis
Sortowanie przez wstawianie połówkowe (Binary Insertion Sort) jest ulepszoną wersją zwykłego sortowania przez wstawianie. Zamiast liniowego przeszukiwania posortowanej części tablicy, używa wyszukiwania binarnego do znalezienia właściwej pozycji dla wstawianego elementu. Redukuje to liczbę porównań, ale nie eliminuje konieczności przesuwania elementów.

## Dane Wejściowe
- **n**: liczba elementów tablicy (n > 0)
- **A[1..n]**: tablica n liczb do posortowania

## Wynik
**A[1..n]**: tablica posortowana rosnąco

## Strategia Rozwiązania

### Idea Algorytmu
1. Podobnie jak w zwykłym insertion sort, dzielimy tablicę na część posortowaną i nieposortowaną
2. Dla każdego elementu z części nieposortowanej:
   - Użyj wyszukiwania binarnego do znalezienia pozycji wstawienia w części posortowanej
   - Przesuń elementy w prawo od tej pozycji
   - Wstaw element na znalezioną pozycję

### Wyszukiwanie binarne
Zamiast liniowego porównywania od końca, używamy podejścia "dziel i zwyciężaj":
- Sprawdzamy środkowy element
- Jeśli klucz jest większy, szukamy w prawej połowie
- Jeśli klucz jest mniejszy, szukamy w lewej połowie
- Powtarzamy aż znajdziemy właściwą pozycję

### Krok po kroku
```
Początkowa tablica: [5, 2, 4, 6, 1, 3]

i=2, klucz=2:
  Wyszukiwanie binarne w [5]: pozycja=1
  Przesuń: [_, 5, 4, 6, 1, 3]
  Wstaw:   [2, 5, 4, 6, 1, 3]

i=3, klucz=4:
  Wyszukiwanie binarne w [2,5]: pozycja=2
  Przesuń: [2, _, 5, 6, 1, 3]
  Wstaw:   [2, 4, 5, 6, 1, 3]

i=4, klucz=6:
  Wyszukiwanie binarne w [2,4,5]: pozycja=4
  Bez przesunięcia: [2, 4, 5, 6, 1, 3]

i=5, klucz=1:
  Wyszukiwanie binarne w [2,4,5,6]: pozycja=1
  Przesuń: [_, 2, 4, 5, 6, 3]
  Wstaw:   [1, 2, 4, 5, 6, 3]

i=6, klucz=3:
  Wyszukiwanie binarne w [1,2,4,5,6]: pozycja=3
  Przesuń: [1, 2, _, 4, 5, 6]
  Wstaw:   [1, 2, 3, 4, 5, 6]
```

## Złożoność Algorytmu

### Złożoność Czasowa
- **Porównania**: O(n log n)
  - Wyszukiwanie binarne: O(log n)
  - Dla n elementów: O(n log n)
  - **To jest poprawa względem O(n²) porównań w zwykłym insertion sort**

- **Przesunięcia**: O(n²)
  - W najgorszym przypadku każdy element wymaga przesunięcia wszystkich poprzednich
  - **To nadal O(n²)**

- **Całkowita złożoność**: **O(n²)**
  - Dominują przesunięcia, nie porównania
  - Algorytm jest szybszy w praktyce, ale asymptotycznie taki sam

### Przypadki szczegółowe:
- **Pesymistyczna (Worst Case)**: O(n²)
  - Tablica posortowana malejąco
  - Każdy element wymaga maksymalnych przesunięć

- **Optymistyczna (Best Case)**: O(n log n)
  - Tablica już posortowana
  - Zero przesunięć, tylko porównania binarne

- **Średnia (Average Case)**: O(n²)
  - Około połowy elementów wymaga przesunięć

### Złożoność Pamięciowa
- **O(log n)** - przez rekurencyjne wyszukiwanie binarne
- Można zredukować do O(1) używając iteracyjnej wersji wyszukiwania binarnego

## Przypadki Szczególne

### Przypadek Optymistyczny
**Tablica posortowana rosnąco**: [1, 2, 3, 4, 5]
- Złożoność: O(n log n)
- Wyszukiwanie binarne: n log n porównań
- Przesunięcia: 0
- **To lepsza od zwykłego insertion sort O(n)**

### Przypadek Pesymistyczny
**Tablica posortowana malejąco**: [5, 4, 3, 2, 1]
- Złożoność: O(n²)
- Wyszukiwanie binarne: n log n porównań
- Przesunięcia: n²/2 (każdy element na początek)

### Przypadek Średni
**Tablica losowa**: [3, 1, 4, 2, 5]
- Złożoność: O(n²)
- Wyszukiwanie binarne: n log n porównań
- Przesunięcia: około n²/4

## Stabilność Sortowania

**Algorytm jest STABILNY** ✓

**Dlaczego jest stabilny?**
- Wyszukiwanie binarne znajduje **pierwszą** pozycję dla elementu
- Równe elementy nie są zamieniane miejscami
- Implementacja musi zwracać pozycję **za** ostatnim równym elementem

**Przykład stabilności:**
```
Wejście:  [(3,a), (1,b), (3,c), (2,d)]

i=2, (1,b): pozycja=1 → [(1,b), (3,a), (3,c), (2,d)]
i=3, (3,c): pozycja=3 → [(1,b), (3,a), (3,c), (2,d)]
i=4, (2,d): pozycja=2 → [(1,b), (2,d), (3,a), (3,c)]

Wyjście: [(1,b), (2,d), (3,a), (3,c)]
```
Zauważ: (3,a) przed (3,c) - kolejność zachowana!

## Zalety i Wady

### Zalety
✓ Mniej porównań niż zwykły insertion sort: O(n log n) vs O(n²)
✓ Stabilny
✓ Sortowanie w miejscu (jeśli iteracyjne wyszukiwanie binarne)
✓ Lepszy dla dużych elementów z kosztownymi porównaniami
✓ Online - może sortować dane w miarę napływania

### Wady
✗ Nadal O(n²) przez przesunięcia
✗ Bardziej skomplikowany niż zwykły insertion sort
✗ Przewaga widoczna tylko gdy porównania są kosztowne
✗ O(log n) pamięci dla rekurencyjnej wersji
✗ W praktyce często nie szybszy od zwykłego insertion sort dla małych n

## Zastosowania
- Gdy porównania są bardzo kosztowne (np. długie stringi, złożone obiekty)
- Małe do średnich zbiory danych
- Prawie posortowane dane
- Gdy stabilność jest wymagana
- Systemy embedded (wersja iteracyjna)

## Porównanie z innymi algorytmami

### vs Insertion Sort
- **Binary**: O(n log n) porównań, O(n²) przesunięć
- **Klasyczny**: O(n²) porównań, O(n²) przesunięć
- **Wniosek**: Binary lepszy gdy porównania są kosztowne

### vs Merge Sort
- **Binary Insertion**: O(n²), O(1) lub O(log n) pamięci, stabilny
- **Merge Sort**: O(n log n), O(n) pamięci, stabilny
- **Wniosek**: Merge Sort lepszy dla dużych zbiorów

### vs Quick Sort
- **Binary Insertion**: stabilny, deterministyczny
- **Quick Sort**: szybszy średnio, niestabilny, O(n²) worst case
- **Wniosek**: Często używane razem - Quick Sort z Binary Insertion dla małych partycji

## Optymalizacje

1. **Iteracyjne wyszukiwanie binarne**:
   - Eliminuje rekursję
   - Redukcja pamięci do O(1)
   
2. **Hybrydowe sortowanie**:
   - Timsort używa insertion sort dla małych fragmentów
   - Introsort przełącza się na insertion sort dla małych partycji
   
3. **Sentinel**:
   - Podobnie jak w zwykłym insertion sort

## Analiza empiryczna

Dla n=1000:
- **Porównania**:
  - Binary Insertion: ~10,000 (n log n)
  - Zwykły Insertion: ~250,000 (n²/2)
  - **Redukcja: 96%**
  
- **Przesunięcia**: 
  - Oba: ~250,000 (n²/2)
  - **Bez zmian**

**Wniosek**: Jeśli porównania są 25x droższe niż przesunięcia, algorytmy są równie szybkie. Jeśli bardziej - Binary Insertion wygrywa.

````
