# Fibonacci - Wyjaśnienie

## Opis
Algorytm oblicza n-ty wyraz ciągu Fibonacciego. Ciąg Fibonacciego definiuje się jako F(1)=1, F(2)=1, F(n)=F(n-1)+F(n-2) dla n>2.

## Wersje
1. **Iteracyjnie** - pętla for, O(n) czasowa, efektywna
2. **Rekurencyjnie** - funkcja rekurencyjna, O(2^n) czasowa, wolna dla dużych n

## Dane Wejściowe
- **n**: numer wyrazu ciągu (n ≥ 1)

## Wynik
F(n): n-ty wyraz ciągu Fibonacciego

## Ciąg Fibonacciego
F(1) = 1, F(2) = 1, F(3) = 2, F(4) = 3, F(5) = 5, F(6) = 8, F(7) = 13, ...

## Przykład
- Fibonacci(6) = 8
- Fibonacci(10) = 55

## Zastosowania
- Modelowanie wzrostu populacji
- Sztuczna inteligencja
- Analiza algorytmów
- Teoria liczb
- Psychologia i biologia

## Uwagi
- **Iteracyjnie**: preferowana dla n > 30 (szybka, O(n))
- **Rekurencyjnie**: najwolniejsza dla dużych n, ale elegancka
- **Optymalizacja**: memoizacja redukuje do O(n) nawet dla rekurencji
