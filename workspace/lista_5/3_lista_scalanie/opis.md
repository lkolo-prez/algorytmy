````markdown
# Scalanie Posortowanych List - Wyjaśnienie

## Opis
Scalanie dwóch posortowanych list jednokierunkowych w jedną posortowaną listę. Algorytm podobny do fazy scalania w Merge Sort. Można zaimplementować rekurencyjnie lub iteracyjnie.

## Strategia

### Podejście rekurencyjne
1. Przypadek bazowy: jeśli jedna lista pusta → zwróć drugą
2. Porównaj głowy obu list
3. Mniejsza głowa staje się początkiem wyniku
4. Rekurencyjnie scal resztę

### Podejście iteracyjne  
1. Wybierz mniejszą głowę jako początek wyniku
2. Iteracyjnie porównuj elementy z obu list
3. Dołączaj mniejszy do wyniku
4. Gdy jedna lista się skończy → dołącz resztę drugiej

## Złożoność
- **Czasowa**: O(n + m) gdzie n, m to długości list
- **Pamięciowa**: 
  - Rekurencyjnie: O(n + m) - stos rekursji
  - Iteracyjnie: O(1) - tylko wskaźniki

## Przykład
```
Lista1: 1 → 3 → 5
Lista2: 2 → 4 → 6

Krok 1: 1 < 2 → wynik: 1
Krok 2: 3 > 2 → wynik: 1 → 2
Krok 3: 3 < 4 → wynik: 1 → 2 → 3
Krok 4: 5 > 4 → wynik: 1 → 2 → 3 → 4
Krok 5: 5 < 6 → wynik: 1 → 2 → 3 → 4 → 5
Krok 6: dołącz resztę: 1 → 2 → 3 → 4 → 5 → 6
```

## Stabilność
Algorytm jest **stabilny** - zachowuje względną kolejność równych elementów.

## Zastosowania
- Merge Sort dla list
- Scalanie wyników z wielu źródeł
- K-way merge
- Zewnętrzne sortowanie

## Optymalizacja
Iteracyjne podejście jest lepsze:
- Brak narzutu rekursji
- Brak ryzyka stack overflow
- O(1) pamięci zamiast O(n)

````
