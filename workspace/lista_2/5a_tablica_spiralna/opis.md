# Tablica Spiralna - Wyjaśnienie

## Opis
Algorytm wypełnia macierz n×n liczbami 1 do n² w porządku spiralnym od zewnątrz do wewnątrz. Ruch przebiega: prawo-dół-lewo-góra, potem zacieśnia się spirala.

## Dane Wejściowe
- **n**: wymiar macierzy (n×n)

## Wynik
**A[1..n][1..n]**: macierz wypełniona spiralnie

## Strategia Rozwiązania

### Kroki Algorytmu
1. Wczytaj n
2. Zainicjalizuj granice: gora=1, dol=n, lewa=1, prawa=n
3. Dopóki są niezapełnione elementy:
   - Wypełnij prawą krawędź (od góry do dołu)
   - Wypełnij dolny rząd (od prawej do lewej)
   - Wypełnij lewą krawędź (od dołu do góry)
   - Wypełnij górny rząd (od lewej do prawej)
   - Zacieśnij granice
4. Wypisz macierz

## Przykład

### Dane Wejściowe
```
n = 4
```

### Przebieg Spirali
```
Krok 1 - Prawa krawędź:
[1, _, _, _]
[2, _, _, _]
[3, _, _, _]
[4, _, _, _]

Krok 2 - Dolny rząd:
[1, _, _, _]
[_, _, _, _]
[_, _, _, _]
[4, 7, 8, 9]

... (kompletny przebieg)

Wynik:
[1,  2,  3,  4]
[12, 13, 14, 5]
[11, 16, 15, 6]
[10, 9,  8,  7]
```

## Zastosowania
- Generowanie testowych macierzy
- Przetwarzanie obrazów (skanowanie spiralne)
- Algorytmy labiryntu
- Problemy optymalizacyjne
- Grafika komputerowa

## Uwagi
- **Kierunek**: prawo → dół → lewo → góra (spirala)
- **Złożoność**: O(n²) - każde pole wypełniane raz
- **Warianty**: spirala do wewnątrz lub na zewnątrz
- **Macierze prostokątne**: algorytm działa dla m×n
- **Liczby**: od 1 do n²
