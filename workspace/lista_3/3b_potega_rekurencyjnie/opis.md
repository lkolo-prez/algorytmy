# Potęga - Rekurencyjnie - Wyjaśnienie

## Opis
Algorytm oblicza a^n za pomocą rekursji. Każde wołanie zmniejsza wykładnik o 1.

## Dane Wejściowe
- **a**: podstawa
- **n**: wykładnik (n ≥ 0)

## Wynik
**a^n**

## Warunek Bazowy
- PotegaRek(a, 0) = 1

## Rekursja
- PotegaRek(a, n) = a × PotegaRek(a, n-1)

## Przykład
```
PotegaRek(2, 4)
= 2 × PotegaRek(2, 3)
= 2 × (2 × PotegaRek(2, 2))
= 2 × (2 × (2 × PotegaRek(2, 1)))
= 2 × (2 × (2 × (2 × PotegaRek(2, 0))))
= 2 × (2 × (2 × (2 × 1)))
= 16
```

## Zastosowania
- Edukacyjny przykład rekursji
- Modelowanie wzrostu potęgowego
- Teoria algorytmów

## Uwagi
- **Szybka potęgowanie**: dla dużych n lepiej "dziel i zwyciężaj" O(log n)
- **Stos**: może się przepełnić dla dużych n
