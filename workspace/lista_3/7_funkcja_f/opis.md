# Funkcja F(y,z) - Rosyjski Chłopek - Wyjaśnienie

## Opis
Algorytm "Rosyjski Chłopek" (Egyptian Multiplication) oblicza iloczyn y×z. Nazwa pochodzi od metody mnożenia używanej w starożytnym Egipcie.

## Dane Wejściowe
- **y, z**: liczby całkowite dodatnie

## Wynik
**y × z**: iloczyn liczb y i z

## Zasada
- Jeśli y parzyste: F(y,z) = F(y/2, z×2)
- Jeśli y nieparzyste: F(y,z) = z + F(y-1, z)
- Warunek bazowy: F(1,z) = z

## Przykład
```
F(13, 7)
= 7 + F(12, 7)
= 7 + F(6, 14)
= 7 + F(3, 28)
= 7 + 28 + F(2, 28)
= 7 + 28 + F(1, 56)
= 7 + 28 + 56
= 91 = 13 × 7
```

## Zastosowania
- Historia algorytmów
- Edukacyjne
- Sztuczna inteligencja
- Obliczanie na starych komputerach (bez mnożenia)

## Uwagi
- **Wersja iteracyjna**: bardziej efektywna (mniej rekursji)
- **Złożoność**: O(log y) - proporcjonalnie do liczby bitów
- **Alternatywa**: zwykłe mnożenie tez O(1) na współczesnych komputerach
