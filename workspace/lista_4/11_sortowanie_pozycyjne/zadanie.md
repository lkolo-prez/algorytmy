````markdown
# Sortowanie Pozycyjne (Radix Sort)

```pseudocode
algorithm ZnajdzMaksimum(A, n) {
  max_val ← A[1]
  
  for i ← 2 to n do {
    if A[i] > max_val then {
      max_val ← A[i]
    }
  }
  
  return max_val
}

algorithm CountingSortDlaPozycji(A, n, pozycja) {
  for i ← 0 to 9 do {
    Count[i] ← 0
  }
  
  for i ← 1 to n do {
    cyfra ← (A[i] / pozycja) % 10
    Count[cyfra] ← Count[cyfra] + 1
  }
  
  for i ← 1 to 9 do {
    Count[i] ← Count[i] + Count[i - 1]
  }
  
  for i ← n downto 1 do {
    cyfra ← (A[i] / pozycja) % 10
    Output[Count[cyfra]] ← A[i]
    Count[cyfra] ← Count[cyfra] - 1
  }
  
  for i ← 1 to n do {
    A[i] ← Output[i]
  }
}

algorithm SortowaniePozycyjne(A, n) {
  read(n)
  
  for i ← 1 to n do {
    read(A[i])
  }
  
  max_val ← ZnajdzMaksimum(A, n)
  
  pozycja ← 1
  while max_val / pozycja > 0 do {
    CountingSortDlaPozycji(A, n, pozycja)
    pozycja ← pozycja * 10
  }
  
  write("Posortowana tablica:")
  for i ← 1 to n do {
    write(A[i], " ")
  }
}
```

Złożoność: O(d * (n + k)) czasowa, O(n + k) pamięciowa, gdzie d - liczba cyfr

````
