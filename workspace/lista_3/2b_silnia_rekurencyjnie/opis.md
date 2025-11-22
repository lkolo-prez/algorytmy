# Silnia - Rekurencyjnie - Wyjaśnienie

## Opis
Algorytm oblicza silnię liczby n za pomocą rekursji. Każde wołanie zmniejsza n o 1 aż do warunku bazowego (n=0 lub n=1).

## Dane Wejściowe
- **n**: liczba całkowita nieujemna (n ≥ 0)

## Wynik
**n!**: silnia liczby n

## Warunek Bazowy
- SilniaRek(0) = 1
- SilniaRek(1) = 1

## Rekursja
SilniaRek(n) = n × SilniaRek(n-1)

## Przykład
```
SilniaRek(5)
= 5 × SilniaRek(4)
= 5 × (4 × SilniaRek(3))
= 5 × (4 × (3 × SilniaRek(2)))
= 5 × (4 × (3 × (2 × SilniaRek(1))))
= 5 × (4 × (3 × (2 × 1)))
= 120
```

## Zastosowania
- Edukacyjny przykład rekursji
- Modelowanie rzeczywistych procesów rekurencyjnych
- Teoria algorytmów

## Uwagi
- **Stos rekursji**: rośnie z każdym wołaniem
- **Limit**: głębia rekursji może spowodować stack overflow
- **Porównanie z iteracyjną**: wolniejsza, więcej pamięci, ale elegancka
- **Optymalizacja**: tail recursion elimination
