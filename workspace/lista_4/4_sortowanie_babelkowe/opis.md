````markdown
# Sortowanie Bąbelkowe - Wyjaśnienie

## Opis
Sortowanie bąbelkowe (Bubble Sort) to jeden z najprostszych algorytmów sortowania. Nazwa pochodzi od sposobu działania - większe elementy "wypływają" na koniec tablicy jak bąbelki w wodzie. Algorytm wielokrotnie przechodzi przez tablicę, porównując sąsiadujące elementy i zamieniając je miejscami, jeśli są w złej kolejności.

## Dane Wejściowe
- **n**: liczba elementów tablicy (n > 0)
- **A[1..n]**: tablica n liczb do posortowania

## Wynik
**A[1..n]**: tablica posortowana rosnąco

## Strategia Rozwiązania

### Idea Algorytmu
1. Przejdź przez całą tablicę, porównując każdą parę sąsiednich elementów
2. Jeśli para jest w złej kolejności, zamień elementy miejscami
3. Po każdym pełnym przejściu największy element "wypłynie" na koniec
4. Powtarzaj proces dla pozostałej części tablicy (bez ostatniego elementu)
5. Kontynuuj aż tablica będzie posortowana

### Dlaczego "bąbelkowe"?
W każdej iteracji największy element "bąbelkuje" w górę (na koniec) tablicy przez seria zamian:
```
[5, 2, 4, 1, 3]
 ↓  ↓
[2, 5, 4, 1, 3]  → 5 większe od 2, zamień
    ↓  ↓
[2, 4, 5, 1, 3]  → 5 większe od 4, zamień
       ↓  ↓
[2, 4, 1, 5, 3]  → 5 większe od 1, zamień
          ↓  ↓
[2, 4, 1, 3, 5]  → 5 większe od 3, zamień → 5 na końcu!
```

### Krok po kroku
```
Początkowa tablica: [5, 2, 4, 1, 3]

Przejście 1: [2, 4, 1, 3, |5|]    (5 na pozycji)
Przejście 2: [2, 1, 3, |4, 5|]    (4 na pozycji)
Przejście 3: [1, 2, |3, 4, 5|]    (3 na pozycji)
Przejście 4: [1, |2, 3, 4, 5|]    (2 na pozycji)

Posortowana: [1, 2, 3, 4, 5]
```

## Złożoność Algorytmu

### Złożoność Czasowa
- **Pesymistyczna (Worst Case)**: O(n²)
  - Tablica posortowana malejąco
  - Każdy element musi być zamieniony z każdym
  - Liczba porównań: n(n-1)/2
  - Liczba zamian: n(n-1)/2

- **Optymistyczna (Best Case)**: O(n)
  - Tablica już posortowana rosnąco
  - Jedno przejście bez żadnej zamiany
  - **Wymaga optymalizacji z flagą**

- **Średnia (Average Case)**: O(n²)
  - Dla losowego rozmieszczenia elementów
  - Około n²/4 zamian

### Złożoność Pamięciowa
- **O(1)** - sortowanie w miejscu (in-place)
- Potrzebujemy tylko zmiennych: i, j, temp

## Przypadki Szczególne

### Przypadek Optymistyczny
**Tablica posortowana rosnąco**: [1, 2, 3, 4, 5]
- Złożoność: O(n) **z optymalizacją**
- Bez optymalizacji: nadal O(n²)
- Jedno przejście, zero zamian
- Algorytm wykrywa brak zamian i kończy

### Przypadek Pesymistyczny
**Tablica posortowana malejąco**: [5, 4, 3, 2, 1]
- Złożoność: O(n²)
- Maksymalna liczba porównań: n(n-1)/2 = 10 (dla n=5)
- Maksymalna liczba zamian: n(n-1)/2 = 10
```
[5,4,3,2,1] → [4,3,2,1,5] → [3,2,1,4,5] → 
[2,1,3,4,5] → [1,2,3,4,5]
```

### Przypadek Średni
**Tablica losowa**: [3, 1, 4, 2, 5]
- Złożoność: O(n²)
- Średnia liczba zamian: n²/4

## Stabilność Sortowania

**Algorytm jest STABILNY** ✓

**Dlaczego jest stabilny?**
- Zamieniamy elementy tylko gdy `A[j] > A[j+1]` (strict inequality)
- Równe elementy **nigdy** nie są zamieniane
- Zachowana jest względna kolejność równych elementów

**Przykład stabilności:**
```
Wejście:  [(3,a), (1,b), (3,c), (2,d)]

Przejście 1: (3,a) vs (1,b) → zamień
             [(1,b), (3,a), (3,c), (2,d)]
             (3,a) vs (3,c) → BEZ zamiany (równe!)
             [(1,b), (3,a), (3,c), (2,d)]
             (3,c) vs (2,d) → zamień
             [(1,b), (3,a), (2,d), (3,c)]

[dalsze przejścia...]

Wyjście: [(1,b), (2,d), (3,a), (3,c)]
```
Zauważ: (3,a) przed (3,c) - stabilność zachowana!

## Zalety i Wady

### Zalety
✓ Bardzo prosty do zrozumienia i implementacji
✓ Stabilny
✓ Sortowanie w miejscu (O(1) pamięci)
✓ Wykrywa posortowane dane (z optymalizacją)
✓ Dobry do celów edukacyjnych

### Wady
✗ Bardzo nieefektywny dla dużych zbiorów O(n²)
✗ Dużo niepotrzebnych porównań i zamian
✗ Najwolniejszy spośród prostych algorytmów O(n²)
✗ Nie jest adaptywny (bez optymalizacji)
✗ Rzadko używany w praktyce

## Zastosowania
- **Edukacja**: najprostszy algorytm do nauki
- **Bardzo małe zbiory**: n < 10
- **Prawie posortowane dane**: z optymalizacją może być O(n)
- **Systemy embedded**: prosty, przewidywalny

## Optymalizacje

### 1. Flaga optymalizacji (wczesne zakończenie)
```pseudocode
zamieniono ← 1
while zamieniono == 1 do {
  zamieniono ← 0
  for j ← 1 to n-1 do {
    if A[j] > A[j+1] then {
      zamień A[j] i A[j+1]
      zamieniono ← 1
    }
  }
}
```
- Jeśli nie ma zamian w przejściu, tablica jest posortowana
- Redukuje O(n²) do O(n) dla posortowanych danych

### 2. Redukcja zakresu
```pseudocode
for i ← 1 to n-1 do {
  for j ← 1 to n-i do {  ← zmniejszamy zakres
    if A[j] > A[j+1] then {
      zamień
    }
  }
}
```
- Po i przejściach, ostatnie i elementów jest na miejscu
- Nie musimy ich sprawdzać ponownie

### 3. Cocktail Sort (Shake Sort)
- Sortowanie w obu kierunkach (zmniejsza O(n²) w praktyce)
- Patrz: osobne zadanie o sortowaniu koktajlowym

## Porównanie z innymi algorytmami

### vs Insertion Sort
- **Bubble Sort**: więcej zamian, wolniejszy
- **Insertion Sort**: mniej zamian, szybszy
- **Wniosek**: Insertion Sort prawie zawsze lepszy

### vs Selection Sort
- **Bubble Sort**: O(n²) zamian
- **Selection Sort**: O(n) zamian
- **Wniosek**: Selection Sort lepszy gdy zamiany są kosztowne

### vs Quick Sort / Merge Sort
- Algorytmy O(n log n) są **znacznie** szybsze
- Przykład: n=1000
  - Bubble Sort: ~500,000 operacji
  - Quick Sort: ~10,000 operacji
  - **50x szybszy!**

## Analiza szczegółowa

Dla tablicy [5,4,3,2,1] (n=5):

| Przejście | Porównania | Zamiany | Stan tablicy |
|-----------|------------|---------|--------------|
| 1 | 4 | 4 | [4,3,2,1,5] |
| 2 | 3 | 3 | [3,2,1,4,5] |
| 3 | 2 | 2 | [2,1,3,4,5] |
| 4 | 1 | 1 | [1,2,3,4,5] |
| **Suma** | **10** | **10** | |

Formuła: n(n-1)/2 = 5×4/2 = 10

## Ciekawostki

1. **Nazwa**: Algorytm nazwany przez Edwarda Reingolda w 1962 roku, ale był znany wcześniej

2. **Barack Obama**: W 2007 powiedział w wywiadzie, że Bubble Sort "nieefektywny" - to było cytowane jako dowód na jego inteligencję!

3. **Najgorszy prosty algorytm**: Spośród prostych algorytmów O(n²), Bubble Sort jest zazwyczaj najwolniejszy

4. **Wersje**: Istnieje wiele wariantów (cocktail, comb sort, gnome sort)

````
