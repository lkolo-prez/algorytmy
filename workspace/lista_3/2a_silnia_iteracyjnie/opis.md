# Silnia - Iteracyjnie - Wyjaśnienie

## Opis
Algorytm oblicza silnię liczby n iteracyjnie. Silnia n! = n × (n-1) × (n-2) × ... × 2 × 1, z warunkiem że 0! = 1.

## Dane Wejściowe
- **n**: liczba całkowita nieujemna (n ≥ 0)

## Wynik
**n!**: silnia liczby n

## Definicja
- 0! = 1
- 1! = 1
- n! = n × (n-1)! dla n > 1

## Przykład
- 5! = 5 × 4 × 3 × 2 × 1 = 120
- 0! = 1
- 10! = 3 628 800

## Zastosowania
- Kombinatoryka
- Teoria prawdopodobieństwa
- Analiza permutacji
- Szeregi potęgowe
- Algorytmy sortujące

## Uwagi
- **Wymóg**: n ≥ 0
- **Wzrost**: silnia rośnie bardzo szybko (15! ≈ 1.3 miliarda)
- **Overflow**: dla n > 20 może dojść do przepełnienia
- **Złożoność**: O(n) iteracji
