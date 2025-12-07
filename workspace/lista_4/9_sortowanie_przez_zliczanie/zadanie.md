````markdown
# Sortowanie przez Zliczanie

```pseudocode
algorithm SortowaniePrzezZliczanie(A, n) {
  read(n)
  
  for i ← 1 to n do {
    read(A[i])
  }
  
  max_val ← A[1]
  min_val ← A[1]
  
  for i ← 2 to n do {
    if A[i] > max_val then {
      max_val ← A[i]
    }
    if A[i] < min_val then {
      min_val ← A[i]
    }
  }
  
  zakres ← max_val - min_val + 1
  
  for i ← 0 to zakres - 1 do {
    Count[i] ← 0
  }
  
  for i ← 1 to n do {
    Count[A[i] - min_val] ← Count[A[i] - min_val] + 1
  }
  
  for i ← 1 to zakres - 1 do {
    Count[i] ← Count[i] + Count[i - 1]
  }
  
  for i ← n downto 1 do {
    Output[Count[A[i] - min_val]] ← A[i]
    Count[A[i] - min_val] ← Count[A[i] - min_val] - 1
  }
  
  for i ← 1 to n do {
    A[i] ← Output[i]
  }
  
  write("Posortowana tablica:")
  for i ← 1 to n do {
    write(A[i], " ")
  }
}
```

Złożoność: O(n + k) czasowa, O(n + k) pamięciowa, gdzie k - zakres wartości

````
