# Usuwanie Duplikatów

```pseudocode
algorithm UsuwanieDuplikatow(A, n) {
  read(n)
  
  for i ← 1 to n do {
    read(A[i])
  }
  
  licznik ← 1
  
  for i ← 2 to n do {
    znaleziono ← false
    
    for j ← 1 to licznik do {
      if A[i] = A[j] then {
        znaleziono ← true
      }
    }
    
    if not znaleziono then {
      licznik ← licznik + 1
      A[licznik] ← A[i]
    }
  }
  
  for i ← 1 to licznik do {
    write(A[i], " ")
  }
}
```

Złożoność: O(n²) czasowa, O(n) pamięciowa
