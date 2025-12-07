````markdown
# Sortowanie Kubełkowe - Wyjaśnienie

## Opis
Sortowanie kubełkowe (Bucket Sort) dzieli zakres wartości na równe "kubełki", przypisuje elementy do odpowiednich kubełków, sortuje każdy kubełek osobno, a następnie łączy wyniki. Efektywny gdy dane są równomiernie rozłożone w pewnym zakresie.

## Złożoność Algorytmu

### Złożoność Czasowa
- **Średnia**: **O(n + k)** gdy dane równomiernie rozłożone
- **Pesymistyczna**: **O(n²)** gdy wszystkie elementy w jednym kubełku
- **Optymistyczna**: **O(n)** gdy każdy element w osobnym kubełku

Gdzie:
- n = liczba elementów
- k = liczba kubełków

### Złożoność Pamięciowa
- **O(n + k)** - kubełki + oryginalna tablica

## Przypadki Szczególne

### Przypadek Optymistyczny
**Równomierne rozłożenie**: [0.1, 0.3, 0.5, 0.7, 0.9]
- Każdy element w osobnym kubełku
- Złożoność: O(n)

### Przypadek Pesymistyczny
**Wszystkie w jednym kubełku**: [0.1, 0.11, 0.12, 0.13]
- Degeneruje do sortowania pojedynczego kubełka
- Złożoność: O(n²) jeśli kubełek sortowany bubble sortem

### Przypadek Średni
**Losowe równomierne**: dane z rozkładu jednostajnego
- Złożoność: O(n)

## Stabilność Sortowania

**Algorytm jest STABILNY** ✓ (jeśli sortowanie kubełków jest stabilne)

**Dlaczego?**
- Elementy trafiają do kubełków w kolejności
- Jeśli sortujemy kubełki stabilnym algorytmem (np. insertion sort)
- Łączenie kubełków zachowuje kolejność

## Zalety i Wady

### Zalety
✓ **O(n) średnio** - liniowy dla równomiernych danych
✓ **Stabilny** (z odpowiednim sortowaniem kubełków)
✓ **Prosty koncept**
✓ **Łatwo zrównoleglić** - każdy kubełek niezależnie
✓ **Dobry dla danych zmiennoprzecinkowych**

### Wady
✗ **Wymaga równomiernego rozkładu** danych
✗ **O(n²) w najgorszym przypadku**
✗ **O(n+k) pamięci** - dodatkowe kubełki
✗ **Wymaga znajomości zakresu** wartości
✗ **Nie in-place**

## Zastosowania
- **Dane zmiennoprzecinkowe** z zakresu [0, 1)
- **Równomiernie rozłożone dane**
- **Sortowanie zewnętrzne** (duże zbiory)
- **Przetwarzanie równoległe**
- **Preprocessing** przed innymi algorytmami

## Dobór liczby kubełków

```
Optymalnie: k = n (liczba kubełków = liczba elementów)

Zbyt mało kubełków: kubełki przepełnione → wolne
Zbyt dużo kubełków: marnowanie pamięci → wolne

Praktycznie: k = n/5 do k = n
```

## Algorytm sortowania kubełków

Najczęściej stosowane:
1. **Insertion Sort** - dobry dla małych kubełków
2. **Quick Sort** - gdy kubełki większe
3. **Rekurencyjnie Bucket Sort** - dla równomiernych danych

## Porównanie

| Cecha | Bucket Sort | Counting Sort | Radix Sort |
|-------|-------------|---------------|------------|
| Złożoność średnia | O(n) | O(n+k) | O(d·n) |
| Typ danych | Rzeczywiste | Całkowite | Całkowite |
| Rozkład danych | Równomierny | Dowolny | Dowolny |
| Pamięć | O(n+k) | O(n+k) | O(n+k) |
| Stabilny | ✓ | ✓ | ✓ |

## Optymalizacje

### 1. Dynamiczne kubełki
Używaj linked list zamiast tablic - oszczędność pamięci.

### 2. Adaptywny wybór k
```pseudocode
k ← max(1, n / średnia_wielkość_kubełka)
```

### 3. Hybrydowy
Dla małych kubełków użyj Insertion Sort, dla dużych Quick Sort.

````
