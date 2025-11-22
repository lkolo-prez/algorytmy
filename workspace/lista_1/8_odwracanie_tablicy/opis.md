# Odwracanie Tablicy - Wyjaśnienie

## Opis
Algorytm odwraca kolejność elementów w tablicy. Pierwszy element staje się ostatnim, drugi przedostatnim itd. Zamienia elementy od obu końców tablicy.

## Dane Wejściowe
- **n**: liczba elementów tablicy (n ≥ 1)
- **A[1..n]**: tablica n liczb

## Wynik
**A[1..n]**: tablica z odwróconą kolejnością elementów

## Strategia Rozwiązania

### Kroki Algorytmu
1. Wczytaj n i elementy tablicy A
2. Pętla od i = 1 do n/2:
   - Zamień A[i] z A[n - i + 1]
3. Wypisz odwróconą tablicę

### Wyjaśnienie Indeksów
- Element 1 zamienia się z elementem n
- Element 2 zamienia się z elementem n-1
- ...
- Element i zamienia się z elementem (n - i + 1)
- Pętla zatrzymuje się na połowie, bo każda para jest zamieniania raz

## Przykład

### Dane Wejściowe
```
n = 6
A = [1, 2, 3, 4, 5, 6]
```

### Przebieg Algorytmu
| i | Zamiana | A[i] ↔ A[n-i+1] | Wynik |
|---|---------|---|---|
| Start | - | - | [1, 2, 3, 4, 5, 6] |
| 1 | A[1] ↔ A[6] | 1 ↔ 6 | [6, 2, 3, 4, 5, 1] |
| 2 | A[2] ↔ A[5] | 2 ↔ 5 | [6, 5, 3, 4, 2, 1] |
| 3 | A[3] ↔ A[4] | 3 ↔ 4 | [6, 5, 4, 3, 2, 1] |

### Wynik
```
[6, 5, 4, 3, 2, 1]
```

## Zastosowania
- Odwrócone sortowanie
- Analiza danych (czytanie od tyłu)
- Przetwarzanie stringów (palindrom)
- Przygotowanie danych do operacji matematycznych
- Algorytmy przetwarzania obrazów

## Uwagi
- **Złożoność**: O(n) - pętla przechodzi n/2 razy
- **Pamięć**: O(n) na przechowywanie tablicy, O(1) na zmienne robocze
- **Liczba zamian**: dokładnie n/2
- **Tablica nieparzysta**: środkowy element pozostaje na miejscu
- **Efektywność**: sortowanie w miejscu, nie wymaga dodatkowej tablicy
