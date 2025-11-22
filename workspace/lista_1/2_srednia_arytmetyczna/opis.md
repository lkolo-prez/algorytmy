# Średnia Arytmetyczna - Wyjaśnienie

## Opis
Algorytm oblicza średnią arytmetyczną wszystkich elementów tablicy. Średnia arytmetyczna to suma wszystkich elementów podzielona przez liczbę elementów.

## Dane Wejściowe
- **n**: liczba elementów tablicy (n > 0)
- **A[1..n]**: tablica n liczb

## Wynik
**srednia**: średnia arytmetyczna wszystkich elementów

## Strategia Rozwiązania

### Kroki Algorytmu
1. Wczytaj liczbę elementów n
2. Wczytaj n elementów do tablicy A
3. Oblicz sumę wszystkich elementów (identycznie jak w zadaniu 1)
4. Podziel sumę przez n: `srednia ← suma / n`
5. Wypisz wynik

## Przykład

### Dane Wejściowe
```
n = 5
A = [10, 20, 30, 40, 50]
```

### Przebieg
- Suma = 10 + 20 + 30 + 40 + 50 = 150
- Średnia = 150 / 5 = 30

### Wynik
```
Średnia = 30
```

## Zastosowania
- Statystyka i analiza danych
- Oceny uczniów
- Średnie temperatury
- Średni czas przetwarzania
- Analizy finansowe (średni zysk, strata)

## Uwagi
- **Wymaga n > 0** aby uniknąć dzielenia przez zero
- **Typ danych**: rezultat może być liczba zmiennoprzecinkowa
- **Precyzja**: dla bardzo dużych sum może dojść do zaokrąglenia
- **Optymalizacja**: można obliczyć średnią "online" bez przechowywania wszystkich wartości
