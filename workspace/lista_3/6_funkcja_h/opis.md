# Funkcja h(n) - Wyjaśnienie

## Opis
Funkcja h(n) reprezentuje minimalną liczbę ruchów potrzebnych do przeniesienia krążka n lub liczbę bitów w reprezentacji binarnej n.

## Definicja
- h(0) = 0
- h(1) = 1
- h(n) = h(n/2), jeśli n jest parzyste
- h(n) = h((n+1)/2) + h((n-1)/2) + 1, jeśli n jest nieparzyste

## Wartości Początkowe
- h(0) = 0
- h(1) = 1
- h(2) = 1
- h(3) = 2
- h(4) = 1
- h(5) = 2
- h(6) = 2
- h(7) = 3

## Zastosowania
- Teoria informatyki
- Analiza algorytmów
- Problemy optymalizacyjne

## Uwagi
- **Memoizacja**: znacznie przyspieszenia obliczenia
- **Wzór**: h(n) = liczba jedynek w reprezentacji binarnej n (dla parzystych)
