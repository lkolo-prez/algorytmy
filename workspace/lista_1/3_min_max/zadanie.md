# Minimum i Maksimum

```pseudocode
algorithm MinMax(A, n) {
  read(n)
  
  for i ← 1 to n do {
    read(A[i])
  }
  
  min ← A[1]
  max ← A[1]
  
  for i ← 2 to n do {
    if A[i] < min then {
      min ← A[i]
    }
    
    if A[i] > max then {
      max ← A[i]
    }
  }
  
  write("Minimum = ", min, ", Maksimum = ", max)
}
```

Złożoność: O(n) czasowa, O(n) pamięciowa
