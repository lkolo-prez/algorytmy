# LISTA 3 - ZADANIE 5
## Funkcja h(n) - Rekurencyjnie zdefiniowana

### Opis
Obliczyć wartość funkcji h(n) zdefiniowanej rekurencyjnie. Funkcja typowo definiowana jako:
- h(0) = 1 (lub inna wartość bazowa)
- h(n) = h(n-1) + 2×h(n-2) lub inna zależność

### UWAGA!
Dokładne sformułowanie zadania z PDF nie jest dostępne. Poniżej pokazuję szablonowe rozwiązanie dla typowego przypadku. Jeśli w PDF jest inna definicja, należy zastosować swoją funkcję zamiast wzoru poniżej.

---

### Przykładowa funkcja: h(n) = h(n-1) + 2×h(n-2)

**Przypadki bazowe:**
- h(0) = 1
- h(1) = 1

**Przypadek rekurencyjny:** h(n) = h(n-1) + 2×h(n-2)

### Pseudokod rekurencyjny

```
algorithm hRekurencyjnie(n)
  
  if (n = 0) then
    return 1
  else if (n = 1) then
    return 1
  else
    return hRekurencyjnie(n-1) + 2 × hRekurencyjnie(n-2)
  end if
  
end algorithm
```

### Pseudokod iteracyjny (z memoizacją)

```
algorithm hIteracyjnie(n)
  
  if (n = 0) then
    return 1
  else if (n = 1) then
    return 1
  else
    a ← 1  // h(0)
    b ← 1  // h(1)
    
    for i ← 2 to n do
      c ← b + 2 × a
      a ← b
      b ← c
    end for
    
    return b
  end if
  
end algorithm
```

---

### Przykłady

**Przykład 1: n=0**
- h(0) = 1 (bazowy)
- Wynik: 1

**Przykład 2: n=1**
- h(1) = 1 (bazowy)
- Wynik: 1

**Przykład 3: n=2**
- h(2) = h(1) + 2×h(0) = 1 + 2×1 = 3
- Wynik: 3

**Przykład 4: n=3**
- h(3) = h(2) + 2×h(1) = 3 + 2×1 = 5
- Wynik: 5

**Przykład 5: n=4**
- h(4) = h(3) + 2×h(2) = 5 + 2×3 = 11
- Wynik: 11

**Przykład 6: n=5**
- h(5) = h(4) + 2×h(3) = 11 + 2×5 = 21
- Wynik: 21

---

### Tablica wartości

| n | h(n) | Obliczenie |
|---|------|-----------|
| 0 | 1 | bazowy |
| 1 | 1 | bazowy |
| 2 | 3 | 1 + 2×1 |
| 3 | 5 | 3 + 2×1 |
| 4 | 11 | 5 + 2×3 |
| 5 | 21 | 11 + 2×5 |
| 6 | 43 | 21 + 2×11 |
| 7 | 85 | 43 + 2×21 |

---

### Drzewo rekurencji (n=4)

```
h(4)
├─ h(3)
│  ├─ h(2)
│  │  ├─ h(1) = 1
│  │  └─ h(0) = 1
│  │  → h(2) = 3
│  ├─ h(1) = 1
│  → h(3) = 5
├─ h(2)
│  ├─ h(1) = 1
│  └─ h(0) = 1
│  → h(2) = 3
→ h(4) = 11
```

---

### Potencjalne problemy logiczne

1. **Błędy w przypadkach bazowych**
   - Problem: h(0)=0 zamiast h(0)=1
   - Wynik: Wszystkie wartości przesunięte
   - Rozwiązanie: Sprawdzić warunki bazowe z treścią zadania

2. **Zła rekurencja**
   - Problem: h(n-1) + h(n-2) zamiast h(n-1) + 2×h(n-2)
   - Wynik: Zupełnie inny ciąg
   - Rozwiązanie: Dokładnie zgodnie z definicją

3. **Brak memoizacji w rekurencji**
   - Problem: Rekurencyjna wersja bez cache
   - Wynik: Bardzo wolno dla dużych n
   - Rozwiązanie: Użyć iteracyjnej lub memoizacji

4. **Brak warunku bazowego**
   - Problem: `if (n > 1)...`
   - Wynik: Nieskończona rekurencja
   - Rozwiązanie: Oba warunki bazowe: n=0 i n=1

5. **Brak obsługi ujemnych n**
   - Problem: Dla n<0 nieskończona rekurencja
   - Wynik: Stack Overflow
   - Rozwiązanie: Sprawdzić n >= 0 na początku

### Złożoność

**Rekurencyjna:**
- **Czasowa: O(2^n)** - bez memoizacji, wykładnicza!
- **Pamięciowa: O(n)** - głęb. stosu

**Iteracyjna:**
- **Czasowa: O(n)** - jedna pętla
- **Pamięciowa: O(1)** - tylko zmienne

---

### Memoizacja rekurencji

```
algorithm hRekurencyjnieMemo(n)
  static memo[...] ← {-1}
  
  if (memo[n] ≠ -1) then
    return memo[n]
  end if
  
  if (n = 0) then
    result ← 1
  else if (n = 1) then
    result ← 1
  else
    result ← hRekurencyjnieMemo(n-1) + 2×hRekurencyjnieMemo(n-2)
  end if
  
  memo[n] ← result
  return result
  
end algorithm
```

Z memoizacją: O(n) zamiast O(2^n)!

---

### Porównanie wersji

| Aspekt | Rekurencyjna | Iteracyjna |
|--------|------------|-----------|
| Czytelność | Wyższa | Niższa |
| Wydajność | Bardzo niska | Szybka |
| Pamięć | O(n) | O(1) |
| Stack Overflow | Tak, dla dużych n | Nigdy |

---

### Uwagi

- **WAŻNE:** Dokładna definicja funkcji h(n) z PDF powinna być zastosowana
- Jeśli inne warunki bazowe, zmień h(0) i h(1)
- Jeśli inna rekurencja, zmień wzór
- Iteracyjna wersja zawsze preferowana w praktyce
- Memoizacja ratuje rekurencję dla większych n

---

### Zastosowanie

- Różne funkcje rekurencyjne w matematyce
- Sekwencje liczb naturalnych
- Dynamiczne programowanie
- Analiza algorytmów rekurencyjnych

### Do poprawy w swoim rozwiązaniu

Jeśli definicja z PDF jest inna, np.:
- h(n) = 3×h(n-1) - h(n-2)
- h(0) = 2, h(1) = 5
- itd.

Zamień odpowiednio w pseudokodzie i przykładach!

