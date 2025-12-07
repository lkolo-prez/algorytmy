````markdown
# Sortowanie przez Indeksowanie - Wyjaśnienie

## Opis
Sortowanie przez indeksowanie (Index Sort, Indirect Sort) nie zmienia oryginalnej tablicy, ale tworzy tablicę indeksów, która wskazuje na elementy w posortowanej kolejności. Przydatne gdy:
- Elementy są duże i kosztowne do przesuwania
- Chcemy zachować oryginalną kolejność
- Potrzebujemy wielu różnych porządków sortowania

## Strategia Rozwiązania

### Idea Algorytmu
1. Utwórz tablicę indeksów: Indeksy[i] = i dla i = 1..n
2. Sortuj tablicę indeksów porównując A[Indeksy[i]] z A[Indeksy[j]]
3. Wypisz elementy w kolejności: A[Indeksy[1]], A[Indeksy[2]], ..., A[Indeksy[n]]

### Krok po kroku
```
Tablica A: [40, 10, 30, 20]

Krok 1: Inicjalizacja indeksów
  Indeksy: [1, 2, 3, 4]

Krok 2: Sortowanie indeksów (używając selection sort)
  Porównujemy A[Indeksy[i]], nie Indeksy[i]!
  
  i=1: min A[Indeksy[2]]=10, zamień Indeksy[1]↔Indeksy[2]
       Indeksy: [2, 1, 3, 4]
       
  i=2: min A[Indeksy[4]]=20, zamień Indeksy[2]↔Indeksy[4]
       Indeksy: [2, 4, 3, 1]
       
  i=3: min A[Indeksy[3]]=30, bez zamiany
       Indeksy: [2, 4, 3, 1]

Krok 3: Wynik
  A[Indeksy[1]] = A[2] = 10
  A[Indeksy[2]] = A[4] = 20
  A[Indeksy[3]] = A[3] = 30
  A[Indeksy[4]] = A[1] = 40
  
  Posortowana kolejność: [10, 20, 30, 40]
  Oryginalna A nadal: [40, 10, 30, 20]
```

## Złożoność Algorytmu

### Złożoność Czasowa
**Zależy od użytego algorytmu sortowania!**

Implementacja z Selection Sort (jak w zadaniu):
- **Zawsze**: **O(n²)**

Ale możemy użyć dowolnego algorytmu:
- Quick Sort: O(n log n) średnio
- Merge Sort: O(n log n) zawsze
- Heap Sort: O(n log n) zawsze

**Dodatkowy koszt**: pośrednie odwołanie A[Indeksy[i]]
- Nieznaczny narzut czasowy
- Słabsza lokalność cache

### Złożoność Pamięciowa
- **O(n)** - tablica indeksów
- **Nie modyfikujemy oryginalnej tablicy**

## Przypadki Szczególne

Zależą od użytego algorytmu sortowania.

Dla Selection Sort:
- **Optymistyczny**: O(n²)
- **Pesymistyczny**: O(n²)
- **Zawsze taka sama złożoność**

## Stabilność Sortowania

**Zależy od użytego algorytmu!**

**Selection Sort**: niestabilny
**Insertion Sort**: stabilny
**Merge Sort**: stabilny

**W naszej implementacji (Selection Sort)**: **NIESTABILNY** ✗

## Zalety i Wady

### Zalety
✓ **Zachowuje oryginalną tablicę** - nie modyfikuje danych
✓ **Efektywny dla dużych obiektów** - sortuje tylko indeksy (4-8 bajtów)
✓ **Wiele porządków sortowania** - możemy stworzyć wiele tablic indeksów
✓ **Dostęp do oryginalnych pozycji** - wiemy skąd pochodzi element
✓ **Permutacja** - tablica indeksów to permutacja

### Wady
✗ **O(n) dodatkowej pamięci** - tablica indeksów
✗ **Wolniejszy dostęp** - pośrednie odwołanie A[Indeksy[i]]
✗ **Gorsza lokalność cache** - skoki po pamięci
✗ **Nie zmienia oryginalnej tablicy** - może być wadą jeśli chcemy

## Zastosowania

### 1. Duże obiekty
```
struct Person {
  char name[100];
  char address[200];
  char other[500];
};  // 800 bajtów!

Zamiast przesuwać 800 bajtów, przesuwamy 4-bajtowe indeksy.
```

### 2. Wiele kryteriów sortowania
```
// Ta sama tablica osób:
Indeksy_Wiek[i]    - sortowanie po wieku
Indeksy_Nazwisko[i] - sortowanie po nazwisku
Indeksy_Miasto[i]  - sortowanie po mieście

// Oryginalna tablica niezmieniona!
```

### 3. Ranking/Permutacja
```
Wyniki zawodów: [85, 92, 78, 95]
Indeksy po sortowaniu: [4, 2, 1, 3]

Ranking:
  1. miejsce: zawodnik 4 (95 pkt)
  2. miejsce: zawodnik 2 (92 pkt)
  3. miejsce: zawodnik 1 (85 pkt)
  4. miejsce: zawodnik 3 (78 pkt)
```

### 4. Bazy danych
- Indeksy w bazach danych działają podobnie
- Sortowanie bez kopiowania całych rekordów

### 5. Operacje statystyczne
```
// Mediana bez modyfikowania oryginalnych danych
Posortuj indeksy
mediana = A[Indeksy[n/2]]
// A nadal w oryginalnej kolejności
```

## Porównanie z sortowaniem normalnym

| Cecha | Sortowanie normalne | Sortowanie przez indeksy |
|-------|---------------------|--------------------------|
| Modyfikuje A | ✓ | ✗ |
| Pamięć | O(1) (in-place) | O(n) |
| Szybkość | Szybsze | Wolniejsze (~10-20%) |
| Duże obiekty | Wolne (kopiowanie) | Szybkie (małe indeksy) |
| Wiele sortowań | Niemożliwe | Możliwe |

## Optymalizacje

### 1. Użyj lepszego algorytmu
```pseudocode
// Zamiast O(n²) Selection Sort:
QuickSortIndices(Indeksy, A, 1, n)  // O(n log n)
```

### 2. Materializacja (rearranging)
Po posortowaniu indeksów, przestaw A według Indeksy:
```pseudocode
for i ← 1 to n do {
  B[i] ← A[Indeksy[i]]
}
A ← B
```
Potem dostęp sekwencyjny bez pośrednictwa.

### 3. Cache-aware
Minimalizuj skoki po pamięci przez grupowanie dostępów.

## Przykład praktyczny: Sortowanie studentów

```
struct Student {
  int id;
  char name[50];
  float gpa;
  char address[100];
};

Student students[1000];  // 160 KB danych!

// Zamiast przesuwać 160 bajtów/student:
int indices[1000];  // 4 KB tylko!

// Sortuj indeksy:
sort_indices_by_gpa(indices, students, 1000);

// Wypisz posortowanych:
for i ← 1 to 1000 do {
  print(students[indices[i]])
}

// students[] nadal w oryginalnej kolejności!
```

## Związek z permutacjami

Tablica indeksów to **permutacja** {1, 2, ..., n}:
```
Indeksy = [3, 1, 4, 2]

Znaczenie:
  - 1. pozycja w posortowanej → 3. element oryginalnej
  - 2. pozycja w posortowanej → 1. element oryginalnej
  - 3. pozycja w posortowanej → 4. element oryginalnej
  - 4. pozycja w posortowanej → 2. element oryginalnej
```

To jest **odwrotna permutacja** (inverse permutation)!

## Ciekawostki
1. **Bazy danych**: Wszystkie indeksy DB działają na tej zasadzie
2. **NumPy/MATLAB**: Funkcje `argsort()` zwracają indeksy
3. **Ranking**: Bardzo naturalne dla rankingów i statystyk porządkowych
4. **Stabilność**: Może być stabilny lub nie, zależy od algorytmu

````
