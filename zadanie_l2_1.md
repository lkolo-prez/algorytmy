# LISTA 2 - ZADANIE 1
## Element najbliższy średniej

### Opis
Znaleźć element tablicy A[1..n], który ma wartość najbliższą średniej arytmetycznej wszystkich elementów.

### Wyjaśnienie
1. Wczytaj n elementów do tablicy
2. Oblicz sumę wszystkich elementów
3. Oblicz średnią: `srednia ← suma / n`
4. Przejedź po wszystkich elementach szukając tego, który ma najmniejszą odległość od średniej
5. Zapamiętaj jego indeks i odległość
6. Zwróć element o najmniejszej odległości

### Pseudokod

```
algorithm NajblizszySredniej(A, n)
  read(n)
  for i ← 1 to n do
    read(A[i])
  end for
  
  suma ← 0
  for i ← 1 to n do
    suma ← suma + A[i]
  end for
  
  srednia ← suma / n
  
  naj_index ← 1
  naj_roznica ← abs(A[1] - srednia)
  
  for i ← 2 to n do
    roznica ← abs(A[i] - srednia)
    if roznica < naj_roznica then
      naj_roznica ← roznica
      naj_index ← i
    end if
  end for
  
  write("Pozycja:", naj_index)
  write("Wartość:", A[naj_index])
end algorithm
```

### Potencjalne problemy logiczne

1. **Inicjalizacja od i=0 zamiast i=1**
   - Problem: Błąd indeksowania (tablice zaczynają się od 1)
   - Rozwiązanie: Zawsze zaczynać `for i ← 1`

2. **Użycie `<=` zamiast `<` w porównaniu**
   - Problem: Gdy kilka elementów ma taką samą odległość, wynik zmienia się losowo
   - Rozwiązanie: Użyć `<` aby zawsze wybrać pierwszy taki element

3. **Dzielenie przez zero gdy n=0**
   - Problem: Średnia będzie undefined/błąd
   - Rozwiązanie: Sprawdzić warunek `if n > 0` przed dzieleniem

4. **Zapomniana inicjalizacja `naj_roznica`**
   - Problem: Niezdefiniowana wartość, wszystkie porównania są błędne
   - Rozwiązanie: Zawsze inicjalizować `naj_roznica ← abs(A[1] - srednia)`

5. **Pętla szukająca zaczyna od i=1 zamiast i=2**
   - Problem: Porównujemy element z sobą samym
   - Rozwiązanie: Rozmawiać pętlę od `i ← 2` bo A[1] już jest zainicjalizowany

### Przykład 1

**Dane:**
- n = 5
- A = [1, 3, 5, 7, 9]

**Obliczenia:**
- suma = 1 + 3 + 5 + 7 + 9 = 25
- średnia = 25 / 5 = 5
- odległości: |1-5|=4, |3-5|=2, |5-5|=0, |7-5|=2, |9-5|=4
- najmniejsza: 0 na pozycji 3

**Wynik:** Pozycja 3, Wartość 5

---

### Przykład 2

**Dane:**
- n = 4
- A = [2, 4, 6, 8]

**Obliczenia:**
- suma = 2 + 4 + 6 + 8 = 20
- średnia = 20 / 4 = 5
- odległości: |2-5|=3, |4-5|=1, |6-5|=1, |8-5|=3
- najmniejsza: 1 (pierwszy raz na pozycji 2)

**Wynik:** Pozycja 2, Wartość 4

---

### Przykład 3 (liczby ujemne)

**Dane:**
- n = 5
- A = [-10, -5, 0, 5, 10]

**Obliczenia:**
- suma = -10 + (-5) + 0 + 5 + 10 = 0
- średnia = 0 / 5 = 0
- odległości: |-10-0|=10, |-5-0|=5, |0-0|=0, |5-0|=5, |10-0|=10
- najmniejsza: 0 na pozycji 3

**Wynik:** Pozycja 3, Wartość 0

---

### Złożoność czasowa
- **O(n)** - przchodzimy tablicę trzy razy: wczytywanie, suma, szukanie

### Złożoność pamięciowa
- **O(n)** - przechowujemy tablicę A[1..n]

### Uwagi
- Działar na liczbach całkowitych i zmiennoprzecinkowych
- Gdy kilka elementów ma tę samą odległość, zwracamy pierwszy z nich
- Algorytm zawsze zwraca dokładnie jeden wynik
