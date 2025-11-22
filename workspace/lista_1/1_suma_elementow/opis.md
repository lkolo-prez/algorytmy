# Suma Elementów Tablicy - Wyjaśnienie

## Opis
Algorytm oblicza sumę wszystkich elementów zawartych w tablicy A[1..n]. Jest to jedna z najprostszych operacji na tablicach i stanowi podstawę dla wielu zaawansowanych algorytmów (średnia, wariancja, itp.).

## Dane Wejściowe
- **n**: liczba elementów tablicy (n > 0)
- **A[1..n]**: tablica n liczb całkowitych lub rzeczywistych

## Wynik
**suma**: suma wszystkich elementów tablicy

## Strategia Rozwiązania

### Kroki Algorytmu
1. Wczytaj liczbę elementów n
2. Wczytaj n elementów do tablicy A
3. Zainicjalizuj zmienną `suma ← 0`
4. Przejdź przez wszystkie elementy (pętla od 1 do n)
5. Dla każdego elementu A[i] dodaj go do sumy: `suma ← suma + A[i]`
6. Wypisz wynik

## Przykład

### Dane Wejściowe
```
n = 4
A = [10, 25, 15, 20]
```

### Przebieg Algorytmu
| Iteracja | i | A[i] | suma |
|----------|---|------|------|
| Start | - | - | 0 |
| 1 | 1 | 10 | 10 |
| 2 | 2 | 25 | 35 |
| 3 | 3 | 15 | 50 |
| 4 | 4 | 20 | **70** |

### Wynik
```
Suma = 70
```

## Zastosowania
- Obliczanie średniej arytmetycznej (suma / n)
- Obliczanie sumy warunkowej (elementy spełniające warunek)
- Sprawdzanie właściwości arytmetycznych tablicy
- Podstawa dla operacji macierzowych
- Algorytmy statystyczne (wariancja, odchylenie standardowe)

## Uwagi
- **Złożoność:** O(n) czasowa - każdy element musi być odwiedzony raz
- **Pamięć:** O(n) na przechowywanie tablicy + O(1) na zmienne robocze
- **Edge case'i:**
  - Tablica pusta (n = 0) → suma = 0
  - Liczby ujemne → algorytm działa poprawnie
  - Przepełnienie: dla bardzo dużych sum może dojść do przekroczenia zakresu typu
