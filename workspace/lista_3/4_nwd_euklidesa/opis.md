# NWD Euklidesa - Wyjaśnienie

## Opis
Algorytm Euklidesa oblicza Największy Wspólny Dzielnik (NWD) dwóch liczb. Opiera się na obserwacji że NWD(a,b) = NWD(b, a mod b).

## Dane Wejściowe
- **a, b**: liczby całkowite dodatnie

## Wynik
**NWD**: największy wspólny dzielnik liczb a i b

## Definicja
NWD(a, b) to największa liczba, która dzieli zarówno a jak i b.

## Zasada Euklidesa
NWD(a, b) = NWD(b, a mod b) dopóki b ≠ 0

## Przykład
```
NWD(48, 18)
= NWD(18, 12)   bo 48 mod 18 = 12
= NWD(12, 6)    bo 18 mod 12 = 6
= NWD(6, 0)     bo 12 mod 6 = 0
= 6              bo wynik to a gdy b = 0
```

## Zastosowania
- Upraszczanie ułamków
- Kryptografia RSA
- Teoria liczb
- Algorytmy

## Uwagi
- **Szybkość**: O(log min(a,b)) - bardzo szybkie
- **Wersje**: iteracyjna i rekurencyjna działają tak samo szybko
- **Najmniejsza wspólna wielokrotność**: LCM(a,b) = (a×b) / NWD(a,b)
