# Palindrom - Rekurencyjnie - Wyjaśnienie

## Opis
Algorytm sprawdza czy tablica (lub string) jest palindromem za pomocą rekursji. Palindrom to sekwencja, która czyta się tak samo do przodu i do tyłu.

## Dane Wejściowe
- **n**: liczba elementów
- **A[1..n]**: tablica do sprawdzenia (liczby lub znaki)

## Wynik
Komunikat czy tablica jest palindromem

## Strategi Rekurencyjna
1. Sprawdź czy element na lewo = element na prawo
2. Jeśli tak, rekursywnie sprawdź wewnętrzną część
3. Jeśli nie, to nie palindrom
4. Warunek bazowy: gdy lewo ≥ prawo, to palindrom

## Przykłady
```
[1, 2, 3, 2, 1] - TAK (palindrom)
[1, 2, 2, 2, 1] - TAK
[1, 2, 3, 4, 5] - NIE
"racecar" - TAK
"hello" - NIE
```

## Zastosowania
- Sprawdzanie palindromów w słowach
- Zamienianie i walidacja danych
- Algorytmy kompresji
- Bioinformatyka (sekwencje DNA)

## Uwagi
- **Zlixoność**: O(n) w najgorszym przypadku
- **Case-sensitive**: "Aba" ≠ "aba" (większość języków)
- **Spacje i znaki**: zwykle ignoruje się przy sprawdzeniu fraz
- **Liczby**: algorytm działa dla tablic liczb równie dobrze
