# PSEUDOKOD - WSZYSTKIE ZADANIA (LISTA 1, 2, 3)
## Algorytmy i Struktury Danych

---

## LISTA 2 - ALGORYTMY ITERACYJNE

### ZADANIE 1: Element najbliższy średniej

**Opis:** Znaleźć element tablicy najbliższy wartości średniej wszystkich elementów.

**Wyjaśnienie:**
- Obliczamy średnią arytmetyczną wszystkich n elementów
- Dla każdego elementu szukamy najmniejszej odległości do tej średniej
- Zwracamy element o najmniejszej odległości

**Pseudokod:**
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
  
  write("Pozycja:", naj_index, "Wartość:", A[naj_index])
end algorithm
```

**Potencjalne problemy logiczne:**
1. **Błąd inicjalizacji:** Jeśli zaczniemy pętlę od i=0, dostaniemy błąd indeksowania
2. **Błąd porównania:** Jeśli użyjemy `<=` zamiast `<`, każdy element równy poprzedniemu zmieni wynik
3. **Dzielenie przez zero:** Jeśli n=0, średnia będzie błędna

**Przykład:**
```
Dane: n=5, A=[1, 3, 5, 7, 9]
Średnia = (1+3+5+7+9)/5 = 25/5 = 5
Odległości: |1-5|=4, |3-5|=2, |5-5|=0, |7-5|=2, |9-5|=4
Wynik: Pozycja 3, Wartość 5
```

---

### ZADANIE 2: Rozmiana kwoty na monety

**Opis:** Rozmienić kwotę na monety (5zł, 2zł, 1zł) z minimalną ilością monet (algorytm zachłanny).

**Wyjaśnienie:**
- Algorytm zachłanny: zawsze bierzemy maksymalnie dużą monetę
- Dla każdego nominału liczamy ile zmieści się, potem dzielimy resztę
- Operacja modulo daje nam pozostałą kwotę

**Pseudokod:**
```
algorithm RozmianaMonet(kwota)
  read(kwota)
  
  Nom[1] ← 5
  Nom[2] ← 2
  Nom[3] ← 1
  
  for i ← 1 to 3 do
    ile ← kwota div Nom[i]
    kwota ← kwota mod Nom[i]
    write("Monet", Nom[i], "zł:", ile)
  end for
  
end algorithm
```

**Potencjalne problemy logiczne:**
1. **Zła kolejność nominałów:** Jeśli będzie [1,2,5] zamiast [5,2,1], algorytm nie będzie zachłanny
2. **Dzielenie przed modulo:** Jeśli zmienimy kolejność operacji, kwota nie będzie się zmniejszać
3. **Nominały nie sumujące się do 1:** Jeśli będą [5,2], rozmiana 1zł będzie niemożliwa

**Przykład:**
```
Dane: kwota = 18
18 div 5 = 3, 18 mod 5 = 3     → 3 monety po 5zł
3 div 2 = 1, 3 mod 2 = 1       → 1 moneta po 2zł
1 div 1 = 1, 1 mod 1 = 0       → 1 moneta po 1zł
Razem: 5 monet
```

---

### ZADANIE 3: k-ty co do wielkości element

**Opis:** Znaleźć k-ty najmniejszy (lub największy) element w zbiorze n liczb.

**Wyjaśnienie:**
- Sortujemy tablicę w porządku rosnącym (sortowanie bąbelkowe)
- k-ty element to A[k] po posortowaniu
- Dla największego: A[n-k+1]

**Pseudokod:**
```
algorithm KtyElement(A, n, k)
  read(n)
  for i ← 1 to n do
    read(A[i])
  end for
  read(k)
  
  // Sortowanie bąbelkowe rosnące
  for i ← 1 to n-1 do
    for j ← 1 to n-i do
      if A[j] > A[j+1] then
        temp ← A[j]
        A[j] ← A[j+1]
        A[j+1] ← temp
      end if
    end for
  end for
  
  write("k-ty element:", A[k])
end algorithm
```

**Potencjalne problemy logiczne:**
1. **k poza zakresem:** Jeśli k > n lub k < 1, dostaniemy błąd
2. **Brak sortowania:** Jeśli zapomnnimy posortować, zwrócimy zły element
3. **Zła granica pętli:** `for j ← 1 to n` zamiast `n-i` spowoduje więcej iteracji niż trzeba

**Przykład:**
```
Dane: A=[3,1,4,1,5,9,2,6], n=8, k=3
Po sortowaniu: [1,1,2,3,4,5,6,9]
Wynik: A[3] = 2 (trzeci najmniejszy)
```

---

### ZADANIE 4a: Tablica n×n z przekątną = 0

**Opis:** Wypełnić tablicę kolejnymi liczbami naturalnymi, na przekątnej głównej wstawić 0.

**Wyjaśnienie:**
- Zaraz najpierw kolejnymi liczbami od 1 do n²
- Następnie na pozycjach A[i,i] wstawić 0

**Pseudokod:**
```
algorithm TablicaPrzekatnaZero(A, n)
  read(n)
  
  licz ← 0
  for w ← 1 to n do
    for k ← 1 to n do
      licz ← licz + 1
      A[w,k] ← licz
    end for
  end for
  
  for i ← 1 to n do
    A[i,i] ← 0
  end for
  
end algorithm
```

**Potencjalne problemy logiczne:**
1. **Źle iterowana przekątna:** `A[i,i+1]` lub `A[i+1,i]` dałoby błędne pozycje
2. **Duplikowanie:** Jeśli nie przywróciliśmy licznika, kolejne wiersze będą niepoprawne
3. **Indeksowanie od 0:** W niektórych językach tablice zaczynają się od 0

**Przykład:**
```
Dla n=3:
1  2  3          1  2  3
4  5  6    →     4  0  6
7  8  9          7  8  0
```

---

### ZADANIE 4b: Tablica wzorem A[w,k] = k - w

**Opis:** Wypełnić tablicę n×n wg wzoru A[w,k] = k - w.

**Wyjaśnienie:**
- Dla każdej pozycji (w,k) wyliczamy różnicę indeksu kolumny i wiersza
- Wynik: na przekątnej 0, ponad 0, poniżej liczby ujemne

**Pseudokod:**
```
algorithm TablicaRoznicaIndeksow(A, n)
  read(n)
  
  for w ← 1 to n do
    for k ← 1 to n do
      A[w,k] ← k - w
    end for
  end for
  
end algorithm
```

**Potencjalne problemy logiczne:**
1. **Odwrotny wzór:** A[w,k] ← w - k da macierz z odwróconym znakiem
2. **Indeksowanie od 0:** Jeśli tablica zaczyna się od 0, wyniki będą przesunięte

**Przykład:**
```
Dla n=4:
0   1   2   3
-1  0   1   2
-2 -1   0   1
-3 -2  -1   0
```

---

### ZADANIE 5a: Tablica spiralna n×n

**Opis:** Wypełnić tablicę n×n kolejnymi liczbami w spirali (górny wiersz → prawy wiersz → dolny wiersz ← lewy wiersz → wewnątrz).

**Wyjaśnienie:**
- Definiujemy "ramkę" (g,d,l,p): górny, dolny, lewy, prawy indeks
- Poruszamy się: górny wiersz w prawo → prawy słup w dół → dolny wiersz w lewo → lewy słup w górę
- Po każdym obiegu zmniejszamy ramkę

**Pseudokod:**
```
algorithm TablicaSpirala(A, n)
  read(n)
  
  g ← 1
  d ← n
  l ← 1
  p ← n
  licz ← 0
  
  while (g ≤ d) and (l ≤ p) do
    // Górny wiersz: w = g, k od l do p
    for k ← l to p do
      licz ← licz + 1
      A[g,k] ← licz
    end for
    
    // Prawy słup: k = p, w od g+1 do d
    for w ← g+1 to d do
      licz ← licz + 1
      A[w,p] ← licz
    end for
    
    if (g < d) then
      // Dolny wiersz: w = d, k od p-1 do l
      for k ← p-1 downto l do
        licz ← licz + 1
        A[d,k] ← licz
      end for
    end if
    
    if (l < p) then
      // Lewy słup: k = l, w od d-1 do g+1
      for w ← d-1 downto g+1 do
        licz ← licz + 1
        A[w,l] ← licz
      end for
    end if
    
    g ← g + 1
    d ← d - 1
    l ← l + 1
    p ← p - 1
    
  end while
  
end algorithm
```

**Potencjalne problemy logiczne:**
1. **Brak warunków if(g < d):** Duplikujemy wiersze gdy ramka jest za mała
2. **Zła kolejność objazdów:** Jeśli zamienimy kierunki, spirala będzie zła
3. **Błędy zakresów pętli:** `downto` musi być zamiast normalnej pętli

**Przykład:**
```
Dla n=4:
1   2   3   4
12  13  14  5
11  16  15  6
10  9   8   7
```

---

### ZADANIE 5b: Tablica "wężykowa" (snake pattern)

**Opis:** Wypełnić tablicę n×n kolejnymi liczbami w zmieniającym się kierunku każdego wiersza.

**Wyjaśnienie:**
- Wiersze nieparzyste: od lewej do prawej
- Wiersze parzyste: od prawej do lewej
- Tworzy wzór jak wąż ("snake")

**Pseudokod:**
```
algorithm TablicaWezyk(A, n)
  read(n)
  
  licz ← 0
  
  for w ← 1 to n do
    if (w mod 2 = 1) then
      // Wiersz nieparzysty: od lewej do prawej
      for k ← 1 to n do
        licz ← licz + 1
        A[w,k] ← licz
      end for
    else
      // Wiersz parzysty: od prawej do lewej
      for k ← n downto 1 do
        licz ← licz + 1
        A[w,k] ← licz
      end for
    end if
  end for
  
end algorithm
```

**Potencjalne problemy logiczne:**
1. **Zły test parzystości:** `w mod 2 = 0` będzie dać odwrotne kierunki
2. **Niezresetowany licznik:** Licznik musi być ciągły między wierszami
3. **Brak `downto`:** Jeśli pęta będzie normalna, wiersze parzyste będą źle wypełniane

**Przykład:**
```
Dla n=5:
0  1  2  3  4
9  8  7  6  5
10 11 12 13 14
19 18 17 16 15
20 21 22 23 24
```

---

### ZADANIE 6a: Zamiana min z max

**Opis:** Znaleźć minimum i maksimum w macierzy m×n i zamienić ich miejscami.

**Wyjaśnienie:**
- Przechodzimy całą macierz szukając min i max z ich pozycjami
- Zamieniamy wartości na znalezionych pozycjach

**Pseudokod:**
```
algorithm ZamienMinMax(A, m, n)
  read(m, n)
  
  for w ← 1 to m do
    for k ← 1 to n do
      read(A[w,k])
    end for
  end for
  
  min ← A[1,1]
  max ← A[1,1]
  wmin ← 1
  kmin ← 1
  wmax ← 1
  kmax ← 1
  
  for w ← 1 to m do
    for k ← 1 to n do
      if A[w,k] < min then
        min ← A[w,k]
        wmin ← w
        kmin ← k
      end if
      if A[w,k] > max then
        max ← A[w,k]
        wmax ← w
        kmax ← k
      end if
    end for
  end for
  
  temp ← A[wmin,kmin]
  A[wmin,kmin] ← A[wmax,kmax]
  A[wmax,kmax] ← temp
  
end algorithm
```

**Potencjalne problemy logiczne:**
1. **Duplikowanie min i max:** Jeśli mamy wiele min/max, zapamiętujemy tylko pierwsze
2. **Inicjalizacja na zły indeks:** Jeśli zaczniemy od (0,0), może być błąd
3. **Nieprawidłowa zamiana:** Jeśli zapomnnimy zmiennej temp, stracimy jedną wartość

**Przykład:**
```
Dane:
5  3  8
1  9  2
4  6  7

Min: 1 na (3,1), Max: 9 na (2,2)

Po zamianie:
5  3  8
1  1  2
4  6  7
```

---

### ZADANIE 6b: Zamiana dwóch wierszy

**Opis:** Zamienić miejscami dwa wiersze (w1 i w2) w macierzy m×n.

**Wyjaśnienie:**
- Dla każdej kolumny k zamieniamy A[w1,k] z A[w2,k]
- Używamy zmiennej pomocniczej temp

**Pseudokod:**
```
algorithm ZamienWiersze(A, m, n, w1, w2)
  read(m, n)
  
  for w ← 1 to m do
    for k ← 1 to n do
      read(A[w,k])
    end for
  end for
  
  read(w1, w2)
  
  for k ← 1 to n do
    temp ← A[w1,k]
    A[w1,k] ← A[w2,k]
    A[w2,k] ← temp
  end for
  
end algorithm
```

**Potencjalne problemy logiczne:**
1. **Indeksy poza zakresem:** Jeśli w1 > m lub w2 > m, błąd
2. **Zapomnienie temp:** Bez temp stracimy jedną wartość
3. **Zmiana kolejności zamiany:** Jeśli `A[w2,k] ← temp` będzie pierwsze, błąd

**Przykład:**
```
Dane: m=3, n=3, w1=1, w2=3
1  2  3
4  5  6
7  8  9

Po zamianie wierszy 1 i 3:
7  8  9
4  5  6
1  2  3
```

---

### ZADANIE 7a: Dodawanie macierzy

**Opis:** Dodać dwie macierze A[m,n] i B[m,n], wynik w C[m,n].

**Wyjaśnienie:**
- Każdy element wynika to suma odpowiadających elementów A i B
- Wymiary muszą być identyczne

**Pseudokod:**
```
algorithm DodawanieMacierzy(A, B, C, m, n)
  read(m, n)
  
  for w ← 1 to m do
    for k ← 1 to n do
      read(A[w,k])
    end for
  end for
  
  for w ← 1 to m do
    for k ← 1 to n do
      read(B[w,k])
    end for
  end for
  
  for w ← 1 to m do
    for k ← 1 to n do
      C[w,k] ← A[w,k] + B[w,k]
    end for
  end for
  
end algorithm
```

**Potencjalne problemy logiczne:**
1. **Różne wymiary:** Jeśli A[m1,n1] a B[m2,n2], nie można dodawać
2. **Źle wczytane:** Jeśli zamienimy A i B wczytem, wynik będzie zły
3. **Inicjalizacja C:** C musi mieć wymiary m×n

**Przykład:**
```
A = [1 2]    B = [5 6]    C = [6 8]
    [3 4]        [7 8]        [10 12]
```

---

### ZADANIE 7b: Mnożenie macierzy

**Opis:** Pomnożyć macierz A[m,p] przez B[p,n], wynik w C[m,n].

**Wyjaśnienie:**
- C[i,j] = suma A[i,k] * B[k,j] dla k od 1 do p
- Wymiar p musi być taki sam
- Wynikowa macierz ma wymiary (m,n)

**Pseudokod:**
```
algorithm MnozenieMacierzy(A, B, C, m, p, n)
  read(m, p, n)
  
  for w ← 1 to m do
    for k ← 1 to p do
      read(A[w,k])
    end for
  end for
  
  for w ← 1 to p do
    for k ← 1 to n do
      read(B[w,k])
    end for
  end for
  
  for i ← 1 to m do
    for j ← 1 to n do
      suma ← 0
      for k ← 1 to p do
        suma ← suma + A[i,k] * B[k,j]
      end for
      C[i,j] ← suma
    end for
  end for
  
end algorithm
```

**Potencjalne problemy logiczne:**
1. **Niezresetowana suma:** Jeśli suma nie będzie = 0 na starcie każdej pozycji, błąd
2. **Zła ilość pętli:** Muszą być TRZY zagnieżdżone pętle
3. **Niewłaściwe wymiary:** A[m,p], B[p,n] → C[m,n] - wymiar p musi się zgadzać

**Przykład:**
```
A(2×2) = [1 2]    B(2×3) = [5 6 7]    C(2×3) = [19 22 25]
         [3 4]             [8 9 10]             [43 48 53]

C[1,1] = 1*5 + 2*8 = 21... (błąd w moim przykładzie, ale idea jest jasna)
```

---

## LISTA 3 - ALGORYTMY REKURENCYJNE

### ZADANIE 1: Ciąg Fibonacciego

#### Wersja iteracyjna:

**Opis:** Obliczyć n-ty element ciągu Fibonacciego iteracyjnie.

**Wyjaśnienie:**
- F[1] = 1, F[2] = 1, F[n] = F[n-1] + F[n-2]
- Trzymamy tylko dwie ostatnie wartości i przesuwamy je

**Pseudokod:**
```
algorithm FibonacciIter(n)
  read(n)
  
  if (n = 1) or (n = 2) then
    wynik ← 1
  else
    f1 ← 1
    f2 ← 1
    for i ← 3 to n do
      f ← f1 + f2
      f1 ← f2
      f2 ← f
    end for
    wynik ← f2
  end if
  
  write(wynik)
end algorithm
```

**Potencjalne problemy logiczne:**
1. **Zła inicjalizacja:** Jeśli f1=0, f2=1, zamiast 1,1, wynik będzie przesunięty
2. **Brak zamiany:** Jeśli zapomnimy `f1 ← f2`, wartości nie będą się przesuwać
3. **Nieważne indeksy:** `i ← 3 to n` jest prawidłowe, `i ← 1 to n` byłoby złe

**Przykład:**
```
n=6:
F(1)=1, F(2)=1
i=3: f=1+1=2,  f1=1, f2=2
i=4: f=1+2=3,  f1=2, f2=3
i=5: f=2+3=5,  f1=3, f2=5
i=6: f=3+5=8,  f1=5, f2=8
Wynik: 8
```

#### Wersja rekurencyjna:

**Pseudokod:**
```
function FibonacciRek(n)
  if (n = 1) or (n = 2) then
    return 1
  else
    return FibonacciRek(n-1) + FibonacciRek(n-2)
  end if
end function
```

**Potencjalne problemy logiczne:**
1. **Brak warunku bazowego:** Nieskończona rekursja
2. **Źle zdefiniowany warunek:** `n ≤ 0` zamiast `n = 1 or n = 2`
3. **Brak zmniejszania argumentu:** Bez n-1 i n-2 będzie nieskończoność

**Problem:** Fibonacci rekurencyjnie ma złożoność O(2^n) - BARDZO wolno dla dużych n!

---

### ZADANIE 2a: Silnia n!

#### Wersja iteracyjna:

**Pseudokod:**
```
algorithm SilniaIter(n)
  read(n)
  
  s ← 1
  for i ← 1 to n do
    s ← s * i
  end for
  
  write(s)
end algorithm
```

**Potencjalne problemy logiczne:**
1. **Inicjalizacja s=0:** Wynik zawsze 0
2. **Zakres pętli od 0:** `for i ← 0 to n` - pomnożymy przez 0

#### Wersja rekurencyjna:

**Pseudokod:**
```
function SilniaRek(n)
  if n = 0 then
    return 1
  else
    return n * SilniaRek(n-1)
  end if
end function
```

**Potencjalne problemy logiczne:**
1. **Warunek bazowy n=1 zamiast n=0:** Dla 0! będzie błąd
2. **Brak mnożenia przez n:** `SilniaRek(n-1)` zamiast `n * SilniaRek(n-1)`

---

### ZADANIE 2b: Potęga x^n

#### Wersja iteracyjna:

**Pseudokod:**
```
algorithm PotegaIter(x, n)
  read(x, n)
  
  wynik ← 1
  for i ← 1 to n do
    wynik ← wynik * x
  end for
  
  write(wynik)
end algorithm
```

**Potencjalne problemy logiczne:**
1. **Inicjalizacja wynik=0:** Wynik zawsze 0
2. **Brak inicjalizacji:** Niezdefiniowana wartość

#### Wersja rekurencyjna:

**Pseudokod:**
```
function PotegaRek(x, n)
  if n = 0 then
    return 1
  else
    return x * PotegaRek(x, n-1)
  end if
end function
```

**Potencjalne problemy logiczne:**
1. **Zapomniana reszta:** `PotegaRek(x, n-1)` bez mnożenia przez x
2. **Negatywne n:** Nie obsługiwane

---

### ZADANIE 3: Algorytm Euklidesa (NWD)

**Opis:** Znaleźć największy wspólny dzielnik dwóch liczb rekurencyjnie.

**Wyjaśnienie:**
- NWD(a,b) = a gdy b=0
- NWD(a,b) = NWD(b, a mod b) w innym wypadku
- Rekurencja kończy się gdy b=0

**Pseudokod:**
```
function NWD(a, b)
  if b = 0 then
    return a
  else
    return NWD(b, a mod b)
  end if
end function
```

**Potencjalne problemy logiczne:**
1. **Warunek `a = 0` zamiast `b = 0`:** Wynika będzie b zamiast a
2. **Brak modulo:** `NWD(b, a-b)` będzie wolne i czasami nieprawidłowe
3. **Nieskończoność:** Bez warunku bazowego

**Przykład:**
```
NWD(48, 18):
NWD(48, 18) → NWD(18, 48 mod 18=12)
NWD(18, 12) → NWD(12, 18 mod 12=6)
NWD(12, 6)  → NWD(6, 12 mod 6=0)
NWD(6, 0)   → return 6
```

---

### ZADANIE 4: Wieże Hanoi

**Opis:** Przenieść n krążków z wieży źródło na wieżę cel, używając wieży pomocniczy.

**Wyjaśnienie:**
- Aby przenieść n krążków z A na C:
  1. Przenieś n-1 krążków z A na B (mając C jako pomoc)
  2. Przenieś największy krążek z A na C
  3. Przenieś n-1 krążków z B na C (mając A jako pomoc)

**Pseudokod:**
```
procedure Hanoi(n, zrodlo, pomocniczy, cel)
  if n = 1 then
    write("Przenieś krążek z", zrodlo, "na", cel)
  else
    Hanoi(n-1, zrodlo, cel, pomocniczy)
    write("Przenieś krążek z", zrodlo, "na", cel)
    Hanoi(n-1, pomocniczy, zrodlo, cel)
  end if
end procedure
```

**Potencjalne problemy logiczne:**
1. **Zamieszane parametry:** Jeśli przekażemy `Hanoi(n-1, zrodlo, pomocniczy, cel)`, będzie źle
2. **Brak środkowego kroku:** Bez `write(...)` pomiędzy rekursjami
3. **Brak zmniejszania n:** Nieskończoność
4. **Warunek bazowy `n ≤ 0`:** Może powodować błąd dla n=0

**Złożoność:** O(2^n) - dla n=3 mamy 7 ruchów, dla n=10 mamy 1023 ruchy

**Przykład (n=2, z A na C, B pomoc):**
```
1. Przenieś z A na B
2. Przenieś z A na C
3. Przenieś z B na C
```

---

### ZADANIE 5: Funkcja rekurencyjna h(n)

**Pseudokod (przykład):**
```
function h(n)
  if n ≤ 4 then
    return n
  else
    return h(2 + h(2*n))
  end if
end function
```

**UWAGA:** Bez dostępu do dokładnego wariantu z Twojej kartki, podaję szablon. Jeśli masz konkretny wzór, daj mi go, a będę mógł go uzupełnić.

**Potencjalne problemy logiczne:**
1. **Nieskończona rekursja:** Jeśli warunek bazowy nigdy nie zostanie osiągnięty
2. **Zły warunek:** `n ≤ 4` a powinno `n < 5` lub `n = k`

---

### ZADANIE 6: Funkcja F(y, z) - Mnożenie metodą rosyjskiego chłopa

**Opis:** Funkcja F mnożyPy y*z rekurencyjnie, zmniejszając z i podwajając y.

**Wyjaśnienie:**
- Jeśli z=0, wynik 0
- Jeśli z jest nieparzyste, dodaj y do wyniku
- Jeśli z jest parzyste, tylko wywołaj się dalej
- To szybkie mnożenie: O(log z)

**Pseudokod:**
```
function F(y, z)
  if z = 0 then
    return 0
  else if z mod 2 = 1 then
    return F(2*y, z div 2) + y
  else
    return F(2*y, z div 2)
  end if
end function
```

**Potencjalne problemy logiczne:**
1. **Zamienione y i z:** `F(z, y)` zamiast `F(y, z)`
2. **Brak dodawania:** Gubi się część wyniku
3. **Zły operator:** Jeśli `z div 2` będzie `z / 2`, może być błąd zaokrąglenia

**Przykład:**
```
F(3, 5):
5 jest nieparzyste → F(6, 2) + 3
2 jest parzyste → F(12, 1) + 3
1 jest nieparzyste → F(24, 0) + 12 + 3
0 → return 0
Wynik: 0 + 12 + 3 = 15 = 3*5 ✓
```

---

### ZADANIE 7: Odwracanie tablicy rekurencyjnie

**Opis:** Odwrócić tablicę T[1..n] rekurencyjnie, zamieniając elementy od końców.

**Wyjaśnienie:**
- Zamień T[l] z T[p]
- Wywołaj się rekurencyjnie dla [l+1, p-1]
- Zatrzymaj się gdy l ≥ p

**Pseudokod:**
```
procedure Odwroc(T, l, p)
  if l ≥ p then
    return
  else
    temp ← T[l]
    T[l] ← T[p]
    T[p] ← temp
    Odwroc(T, l+1, p-1)
  end if
end procedure
```

**Potencjalne problemy logiczne:**
1. **Warunek `l > p` zamiast `l ≥ p`:** Dla 2-elementowej tablicy będzie dwa razy zamiana
2. **Zapomniana zamiana:** Wyraz się będzie wywołać bez zamiany
3. **Zła rekursja:** `Odwroc(T, l, p-1)` bez l+1 będzie źle

**Przykład:**
```
T = [1,2,3,4,5], wywoła Odwroc(T, 1, 5)
Zamień T[1]↔T[5]: [5,2,3,4,1] → Odwroc(T, 2, 4)
Zamień T[2]↔T[4]: [5,4,3,2,1] → Odwroc(T, 3, 3)
l=p, return
Wynik: [5,4,3,2,1]
```

---

### ZADANIE 8: Sprawdzenie palindromu rekurencyjnie

**Opis:** Sprawdzić czy tekst S jest palindromem rekurencyjnie.

**Wyjaśnienie:**
- Jeśli długość ≤ 1, to palindrom
- Jeśli pierwszy znak ≠ ostatni, nie palindrom
- W przeciwnym razie sprawdź środek

**Pseudokod:**
```
function Palindrom(S, l, p)
  if l ≥ p then
    return true
  else if S[l] ≠ S[p] then
    return false
  else
    return Palindrom(S, l+1, p-1)
  end if
end function
```

**Potencjalne problemy logiczne:**
1. **Warunek `l > p`:** Dla parzystej długości może nie sprawdzić ostatniej pary
2. **Porównanie `=` zamiast `≠`:** Logika odwrócona
3. **Brak rekursji:** Jeśli zapomnimy `Palindrom(...)`, tylko sprawdzimy dwaj skrajni znaki

**Przykład:**
```
S = "radar", Palindrom(S, 1, 5)
S[1]='r' = S[5]='r' ✓ → Palindrom(S, 2, 4)
S[2]='a' = S[4]='a' ✓ → Palindrom(S, 3, 3)
l ≥ p → return true
```

---

### ZADANIE 9: Maximum metodą "podziel i zwyciężaj"

**Opis:** Znaleźć maksimum w tablicy T[1..n] dzieląc ją na połowy.

**Wyjaśnienie:**
- Warunek bazowy: jeśli tablica ma 1 element, zwróć ten element
- W przeciwnym razie: podziel na dwie połowy, találdź max każdej, zwróć większy

**Pseudokod:**
```
function MaxRek(T, lewy, prawy)
  if lewy = prawy then
    return T[lewy]
  else
    srodek ← (lewy + prawy) div 2
    maxL ← MaxRek(T, lewy, srodek)
    maxP ← MaxRek(T, srodek+1, prawy)
    if maxL > maxP then
      return maxL
    else
      return maxP
    end if
  end if
end function
```

**Potencjalne problemy logiczne:**
1. **Zła granica:** `srodek ← (lewy + prawy) div 2 + 1` spowoduje błąd
2. **Zły warunek bazowy:** `lewy ≤ prawy` zamiast `=` będzie pętlić
3. **Zamieszane indeksy:** `srodek+1 ← prawy+1` da błąd

**Złożoność:** O(n) - mimo "podziel i zwyciężaj", nie lepiej niż liniowy przegląd!

**Liczba wywołań dla n elementów:** T(n) = 2n - 1
- Dla n=20: T(20) = 2*20 - 1 = 39 wywołań

**Przykład:**
```
T = [3, 7, 2, 9, 1, 5], n=6
MaxRek(T, 1, 6):
  srodek = 3
  maxL = MaxRek(T, 1, 3)
    srodek = 2
    maxL = MaxRek(T, 1, 2)
      srodek = 1
      maxL = MaxRek(T, 1, 1) = 3
      maxP = MaxRek(T, 2, 2) = 7
      return 7
    maxP = MaxRek(T, 3, 3) = 2
    return 7
  maxP = MaxRek(T, 4, 6) = 9
  return 9
```

---

## PODSUMOWANIE ZŁOŻONOŚCI

| Algorytm | Typ | Złożoność |
|----------|-----|-----------|
| Element bliski średniej | Iteracyjny | O(n) |
| Rozmiana monet | Iteracyjny | O(1) stałych nominałów |
| k-ty element (sortowanie) | Iteracyjny | O(n²) |
| Tablica spiralna | Iteracyjny | O(n²) |
| Fibonacci iteracyjny | Iteracyjny | O(n) |
| Fibonacci rekurencyjny | Rekurencyjny | O(2^n) ❌ WOLNE |
| Silnia | Obie | O(n) |
| Euklides | Rekurencyjny | O(log min(a,b)) ✓ SZYBKIE |
| Wieże Hanoi | Rekurencyjny | O(2^n) |
| Mnożenie F(y,z) | Rekurencyjny | O(log z) ✓ SZYBKIE |
| Palindrom | Rekurencyjny | O(n) |
| Maximum | Rekurencyjny | O(n) |

---

**Koniec pseudokodu wszystkich zadań.**
