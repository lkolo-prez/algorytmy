# K-ty Co do Wielkości Element

```pseudocode
algorithm KtyElement(A, n, k) {
  read(n, k)
  
  for i ← 1 to n do {
    read(A[i])
  }
  
  for i ← 1 to n - 1 do {
    for j ← 1 to n - i do {
      if A[j] > A[j + 1] then {
        temp ← A[j]
        A[j] ← A[j + 1]
        A[j + 1] ← temp
      }
    }
  }
  
  if k ≥ 1 and k ≤ n then {
    write("K-ty element (k=", k, "): ", A[k])
  } else {
    write("Błąd: k poza zakresem")
  }
}
```

Złożoność: O(n²) czasowa, O(n) pamięciowa
