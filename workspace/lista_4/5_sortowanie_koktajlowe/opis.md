````markdown
# Sortowanie przez Wstrząsanie (Koktajlowe) - Wyjaśnienie

## Opis
Sortowanie koktajlowe (Cocktail Sort, Cocktail Shaker Sort, Bidirectional Bubble Sort) to udoskonalona wersja sortowania bąbelkowego. Różnica polega na tym, że algorytm działa w obu kierunkach - najpierw przesuwa największe elementy w prawo, potem najmniejsze w lewo. To dwukierunkowe podejście eliminuje problem "żółwi" (małe elementy na końcu tablicy poruszające się powoli).

## Dane Wejściowe
- **n**: liczba elementów tablicy (n > 0)
- **A[1..n]**: tablica n liczb do posortowania

## Wynik
**A[1..n]**: tablica posortowana rosnąco

## Strategia Rozwiązania

### Idea Algorytmu
1. **Przejście w prawo**: Przesuń największy element na koniec (jak bubble sort)
2. **Przejście w lewo**: Wróć i przesuń najmniejszy element na początek
3. Zmniejsz zakres (zwiększ `start`, zmniejsz `koniec`)
4. Powtarzaj aż nie będzie więcej zamian

### Problem "żółwi" w Bubble Sort
```
[2, 3, 4, 5, 1]

Bubble Sort:
Przejście 1: [2,3,4,1,5] (1 przesuwa się tylko o 1)
Przejście 2: [2,3,1,4,5] (1 przesuwa się tylko o 1)
Przejście 3: [2,1,3,4,5] (1 przesuwa się tylko o 1)
Przejście 4: [1,2,3,4,5] (1 przesuwa się tylko o 1)
→ 4 przejścia!

Cocktail Sort:
Prawo:  [2,3,4,1,5] (5 na miejsce)
Lewo:   [1,2,3,4,5] (1 od razu na początek!)
→ 1 przejście!
```

### Krok po kroku
```
Początkowa: [5, 1, 4, 2, 8, 0, 2]

Runda 1 (prawo): [1,5,4,2,0,2,|8|]
Runda 1 (lewo):  [|0|,1,5,4,2,|2,8|]
Runda 2 (prawo): [0,|1,4,2,|5,2,8|]
Runda 2 (lewo):  [0,1,|2,4,|2,5,8|]
Runda 3 (prawo): [0,1,2,|2,4|,5,8]
Runda 3 (lewo):  [0,1,2,|2,4|,5,8] (bez zamian - koniec)

Posortowana: [0,1,2,2,4,5,8]
```

## Złożoność Algorytmu

### Złożoność Czasowa
- **Pesymistyczna (Worst Case)**: O(n²)
  - Podobnie jak bubble sort
  - Tablica posortowana odwrotnie
  
- **Optymistyczna (Best Case)**: O(n)
  - Tablica już posortowana
  - Jedno przejście w prawo i lewo bez zamian
  
- **Średnia (Average Case)**: O(n²)
  - Jednak **lepszy stały współczynnik** niż bubble sort
  - W praktyce ~2x szybszy od bubble sort

### Złożoność Pamięciowa
- **O(1)** - sortowanie w miejscu

## Przypadki Szczególne

### Przypadek Optymistyczny
**Tablica posortowana**: [1, 2, 3, 4, 5]
- Złożoność: O(n)
- Jedno przejście w prawo: bez zamian
- Przejście w lewo: nie wykonuje się (flaga zamieniono=0)

### Przypadek Pesymistyczny
**Tablica odwrotnie posortowana**: [5, 4, 3, 2, 1]
- Złożoność: O(n²)
- Podobnie jak bubble sort
- Jednak w praktyce ~2x szybszy

### Przypadek z "żółwiami"
**Mały element na końcu**: [2, 3, 4, 5, 1]
- **Bubble Sort**: 4 przejścia
- **Cocktail Sort**: 2 przejścia (lub nawet 1)
- **Przewaga cocktail sort jest wyraźna!**

### Przypadek z "królikami"
**Duży element na początku**: [5, 1, 2, 3, 4]
- **Bubble Sort**: 1 przejście (króliki szybko "wypływają")
- **Cocktail Sort**: 1 przejście
- **Brak różnicy**

## Stabilność Sortowania

**Algorytm jest STABILNY** ✓

**Dlaczego?**
- Zamiany tylko gdy `A[i] > A[i+1]` (strict inequality)
- W obu kierunkach używamy strict inequality
- Równe elementy zachowują kolejność

**Przykład:**
```
[(3,a), (1,b), (3,c), (2,d)]

Prawo: [(1,b), (3,a), (2,d), (3,c)]
Lewo:  [(1,b), (2,d), (3,a), (3,c)]
       ↑ (3,a) przed (3,c) - stabilność zachowana!
```

## Zalety i Wady

### Zalety
✓ Lepszy od bubble sort (~2x szybszy w praktyce)
✓ Rozwiązuje problem "żółwi"
✓ Stabilny
✓ Sortowanie w miejscu (O(1) pamięci)
✓ Wykrywa posortowane dane (O(n))
✓ Prosty do zrozumienia

### Wady
✗ Nadal O(n²) - nie zmienia asymptotycznej złożoności
✗ Wolniejszy od insertion sort
✗ Bardziej skomplikowany niż bubble sort
✗ Rzadko używany w praktyce
✗ Dwa razy więcej kodu niż bubble sort

## Zastosowania
- Edukacja (pokazanie optymalizacji bubble sort)
- Dane z małymi elementami na końcu lub dużymi na początku
- Bardzo małe zbiory danych
- Gdy stabilność jest wymagana a pamięć ograniczona

## Porównanie z Bubble Sort

### Bubble Sort - problem "żółwi":
```
[99, 98, 97, 1]  → 1 musi "przejść" przez wszystkie elementy
Przejście 1: [98, 97, 1, |99|]
Przejście 2: [97, 1, |98, 99|]
Przejście 3: [1, |97, 98, 99|]
→ 3 przejścia
```

### Cocktail Sort - brak problemu:
```
[99, 98, 97, 1]
Prawo: [98, 97, 1, |99|]
Lewo:  [|1|, 98, 97, |99|]
Prawo: [1, |97, 98|, 99]
Lewo:  [1, |97, 98|, 99] (bez zmian - koniec)
→ mniej operacji!
```

## Optymalizacje

### 1. Zapamiętywanie ostatniej zamiany
```pseudocode
ostatnia_zamiana_prawo ← 0
ostatnia_zamiana_lewo ← 0

// W pętli prawo:
if zamieniono then
  ostatnia_zamiana_prawo ← i
  
// Ustawiamy koniec na ostatnią zamianę
koniec ← ostatnia_zamiana_prawo
```
Redukuje liczbę porównań.

### 2. Wczesne zakończenie
Jeśli obie pętle (prawo i lewo) nie wykonują żadnej zamiany, kończymy.

## Warianty

### Comb Sort
- Uogólnienie cocktail sort z przeskokami (gap)
- Lepsze O(n log n) w praktyce
- Bardziej skomplikowany

### Odd-Even Sort
- Porównuje naprzemiennie pary nieparzyste i parzyste
- Dobrze się równoległości
- Podobna wydajność

## Analiza empiryczna

Dla n=1000, tablica losowa:
- **Bubble Sort**: ~500,000 operacji
- **Cocktail Sort**: ~250,000 operacji (~2x szybszy)
- **Insertion Sort**: ~125,000 operacji (~2x szybszy od cocktail)
- **Quick Sort**: ~10,000 operacji (~50x szybszy od cocktail)

## Kiedy używać?

**Cocktail Sort lepszy od Bubble Sort gdy:**
- Małe elementy są na końcu tablicy
- Chcemy pokazać optymalizację bubble sort

**Ale w większości przypadków lepiej użyć:**
- **Insertion Sort**: podobna prostota, lepsza wydajność
- **Merge/Quick Sort**: dla większych danych

````
