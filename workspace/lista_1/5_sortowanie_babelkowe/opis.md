# Sortowanie Bąbelkowe - Wyjaśnienie

## Opis
Sortowanie bąbelkowe to najprostszy algorytm sortujący. Polega na wielokrotnym przeglądaniu tablicy i zamianie sąsiednich elementów, jeśli są w niewłaściwej kolejności. Największe elementy "bąbelkują" na koniec tablicy.

## Dane Wejściowe
- **n**: liczba elementów tablicy (n ≥ 1)
- **A[1..n]**: tablica n liczb do posortowania

## Wynik
**A[1..n]**: tablica posortowana rosnąco

## Strategia Rozwiązania

### Kroki Algorytmu
1. Wczytaj n i elementy tablicy A
2. Pętla zewnętrzna: powtarzaj n-1 razy
3. Pętla wewnętrzna: przeglądaj tablicę i zamień sąsiednie elementy jeśli A[j] > A[j+1]
4. Po każdej iteracji pętli zewnętrznej największy element jest na swoim miejscu
5. Wypisz posortowaną tablicę

## Przykład

### Dane Wejściowe
```
n = 5
A = [5, 2, 8, 1, 9]
```

### Przebieg Sortowania
```
Start:      [5, 2, 8, 1, 9]

Iteracja 1: [2, 5, 8, 1, 9]  → zamiana 5 i 2
            [2, 5, 1, 8, 9]  → zamiana 8 i 1
            [2, 5, 1, 8, 9]  → porównanie 8 i 9

Iteracja 2: [2, 5, 1, 8, 9]
            [2, 1, 5, 8, 9]  → zamiana 5 i 1

Iteracja 3: [1, 2, 5, 8, 9]

Iteracja 4: [1, 2, 5, 8, 9]

Wynik:      [1, 2, 5, 8, 9]
```

## Zastosowania
- Dydaktyczne (nauka algorytmów sortowania)
- Sortowanie małych danych (n < 50)
- Sortowanie niemal posortowanych danych
- Gdy pamięć jest bardziej limitująca niż czas

## Uwagi
- **Wada**: bardzo wolne dla dużych danych (O(n²))
- **Zaleta**: prosty do implementacji, sortuje w miejscu
- **Optymalizacja**: można dodać flagę aby przerwać jeśli tablica jest już posortowana
- **Wariant 2-przebiegowy**: pętle można przeplotać lepiej dla cache'a
- **Stabilne**: równe elementy zachowują oryginalną kolejność
