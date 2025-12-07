````markdown
# Sortowanie przez Proste Wstawianie - Wyjaśnienie

## Opis
Sortowanie przez proste wstawianie (Insertion Sort) jest jednym z najprostszych algorytmów sortowania. Działa podobnie do sposobu, w jaki większość ludzi sortuje karty do gry - bierzemy kolejne elementy i wstawiamy je w odpowiednie miejsce w już posortowanej części tablicy.

## Dane Wejściowe
- **n**: liczba elementów tablicy (n > 0)
- **A[1..n]**: tablica n liczb do posortowania

## Wynik
**A[1..n]**: tablica posortowana rosnąco

## Strategia Rozwiązania

### Idea Algorytmu
1. Dzielimy tablicę na dwie części: posortowaną (na początku tylko A[1]) i nieposortowaną
2. W każdej iteracji bierzemy pierwszy element z części nieposortowanej (klucz)
3. Porównujemy klucz z elementami części posortowanej od końca
4. Przesuwamy większe elementy w prawo, aby zrobić miejsce dla klucza
5. Wstawiamy klucz we właściwe miejsce

### Krok po kroku
```
Początkowa tablica: [5, 2, 4, 6, 1, 3]

i=2, klucz=2:  [2, 5, 4, 6, 1, 3]
i=3, klucz=4:  [2, 4, 5, 6, 1, 3]
i=4, klucz=6:  [2, 4, 5, 6, 1, 3]
i=5, klucz=1:  [1, 2, 4, 5, 6, 3]
i=6, klucz=3:  [1, 2, 3, 4, 5, 6]
```

## Złożoność Algorytmu

### Złożoność Czasowa
- **Pesymistyczna (Worst Case)**: O(n²)
  - Występuje gdy tablica jest posortowana malejąco
  - Każdy element musi być porównany ze wszystkimi poprzednimi
  - Liczba porównań: 1 + 2 + 3 + ... + (n-1) = n(n-1)/2

- **Optymistyczna (Best Case)**: O(n)
  - Występuje gdy tablica jest już posortowana rosnąco
  - Każdy element wymaga tylko jednego porównania
  - Nie wykonujemy żadnych przesunięć

- **Średnia (Average Case)**: O(n²)
  - Dla losowego rozmieszczenia elementów
  - Około połowa elementów wymaga przesunięć

### Złożoność Pamięciowa
- **O(1)** - sortowanie w miejscu (in-place)
- Potrzebujemy tylko stałej liczby zmiennych pomocniczych (klucz, i, j)

## Przypadki Szczególne

### Przypadek Optymistyczny
**Tablica posortowana rosnąco**: [1, 2, 3, 4, 5]
- Złożoność: O(n)
- Każdy element jest już na właściwym miejscu
- Wykonujemy tylko n-1 porównań, zero przesunięć

### Przypadek Pesymistyczny
**Tablica posortowana malejąco**: [5, 4, 3, 2, 1]
- Złożoność: O(n²)
- Każdy element musi być przesunięty na początek
- Maksymalna liczba porównań i przesunięć

### Przypadek Średni
**Tablica losowa**: [3, 1, 4, 2, 5]
- Złożoność: O(n²)
- Niektóre elementy wymagają przesunięć, inne nie

## Stabilność Sortowania

**Algorytm jest STABILNY** ✓

**Stabilność** oznacza, że elementy o równych kluczach zachowują swoją względną kolejność z tablicy wejściowej.

**Dlaczego jest stabilny?**
- Warunek w pętli while: `A[j] > klucz` (strict inequality)
- Element jest przesuwany tylko gdy jest **ściśle większy** od klucza
- Równe elementy nie są zamieniane miejscami

**Przykład stabilności:**
```
Wejście:  [(3,a), (1,b), (3,c), (2,d)]
Wyjście:  [(1,b), (2,d), (3,a), (3,c)]
```
Zauważ, że (3,a) występuje przed (3,c) w obu przypadkach.

## Zalety i Wady

### Zalety
✓ Prosty do zrozumienia i implementacji
✓ Wydajny dla małych zbiorów danych (n < 50)
✓ Wydajny dla prawie posortowanych tablic
✓ Stabilny
✓ Sortowanie w miejscu (O(1) pamięci)
✓ Online - może sortować dane w miarę ich napływania

### Wady
✗ Nieefektywny dla dużych zbiorów (O(n²))
✗ Nie wykorzystuje równoległości
✗ Dużo operacji przesuwania elementów

## Zastosowania
- Sortowanie małych zbiorów danych
- Sortowanie prawie posortowanych danych
- Jako część algorytmów hybrydowych (np. w Timsort)
- Gdy potrzebujemy algorytmu online
- Systemy embedded z ograniczoną pamięcią

## Optymalizacje
1. **Binary Insertion Sort**: Użycie wyszukiwania binarnego do znalezienia pozycji wstawienia (redukuje porównania do O(n log n), ale przesunięcia pozostają O(n²))
2. **Sentinel**: Dodanie wartownika na początku tablicy eliminuje sprawdzanie j >= 1
3. **Shell Sort**: Uogólnienie insertion sort używające sekwencji przyrostów

## Porównanie z innymi algorytmami
- **vs Bubble Sort**: Insertion Sort jest szybszy (mniej zamian)
- **vs Selection Sort**: Podobna złożoność, ale Insertion Sort lepszy dla prawie posortowanych
- **vs Quick Sort**: Quick Sort szybszy dla dużych danych, Insertion Sort lepszy dla małych

````
