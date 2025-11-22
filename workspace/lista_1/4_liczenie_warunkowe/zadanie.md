# Liczenie Elementów Spełniających Warunek

```pseudocode
algorithm LiczenieWarunkowe(A, n, k) {
  read(n, k)
  
  for i ← 1 to n do {
    read(A[i])
  }
  
  licznik ← 0
  
  for i ← 1 to n do {
    if A[i] > k then {
      licznik ← licznik + 1
    }
  }
  
  write("Liczba elementów > ", k, ": ", licznik)
}
```

Złożoność: O(n) czasowa, O(n) pamięciowa
