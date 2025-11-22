# Palindrom - Rekurencyjnie

```pseudocode
algorithm PalindomRek(A, n) {
  read(n)
  
  for i ← 1 to n do {
    read(A[i])
  }
  
  if CzyPalindromeRek(A, 1, n) then {
    write("To jest palindrom")
  } else {
    write("To nie jest palindrom")
  }
}

algorithm CzyPalindromeRek(A, lewo, prawo) {
  if lewo ≥ prawo then {
    return true
  } else {
    if A[lewo] = A[prawo] then {
      return CzyPalindromeRek(A, lewo + 1, prawo - 1)
    } else {
      return false
    }
  }
}
```

Złożoność: O(n) czasowa, O(n) pamięciowa (stos rekursji)
