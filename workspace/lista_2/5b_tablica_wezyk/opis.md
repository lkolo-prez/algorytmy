# Tablica Wężykowa (Snake Pattern) - Wyjaśnienie

## Opis
Algorytm wypełnia macierz n×n liczbami 1 do n² w porządku "wężykowym". Wiersze nieparzyste idą od lewej do prawej, parzyste od prawej do lewej, tworząc wzór ścieżki węża.

## Dane Wejściowe
- **n**: wymiar macierzy (n×n)

## Wynik
**A[1..n][1..n]**: macierz wypełniona wężykowa

## Strategia Rozwiązania

### Kroki Algorytmu
1. Wczytaj n
2. Zainicjalizuj licznik = 1
3. Dla każdego wiersza i:
   - Jeśli i jest nieparzyste: idź od lewej do prawej
   - Jeśli i jest parzyste: idź od prawej do lewej
   - Wypełnij wartościami licznik, licznik+1, ...
4. Wypisz macierz

## Przykład

### Dane Wejściowe
```
n = 4
```

### Przebieg Wypełniania
```
Wiersz 1 (nieparzysty):  1  2  3  4   (← lewa do prawej)
Wiersz 2 (parzysty):     8  7  6  5   (← prawa do lewej)
Wiersz 3 (nieparzysty):  9  10 11 12  (← lewa do prawej)
Wiersz 4 (parzysty):     16 15 14 13  (← prawa do lewej)

Wynik:
[1,  2,  3,  4]
[8,  7,  6,  5]
[9,  10, 11, 12]
[16, 15, 14, 13]
```

## Zastosowania
- Przetwarzanie obrazów (skanowanie liniowe)
- Drukowanie drukarkami z przesunięciem
- Urządzenia z czytaniem wężykowym
- Algoritmy labiryntu
- Paddy code / barcode scanning

## Uwagi
- **Wzór**: natychmiast widoczny "wąż" w macierzy
- **Złożoność**: O(n²) - każde pole raz
- **Modulo 2**: sprawdzenie parzystości wiersza
- **Kierunek**: najpierw prawo, potem lewo, potem prawo...
- **Liczby**: sekwencyjne 1 do n²
