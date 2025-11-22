# Fibonacci

```pseudocode
algorithm FibonacciIteracyjnie(n) {
  read(n)
  
  if n ≤ 0 then {
    write("Błąd: n musi być > 0")
  } else {
    if n = 1 or n = 2 then {
      write("Fibonacci(", n, ") = 1")
    } else {
      a ← 1
      b ← 1
      
      for i ← 3 to n do {
        c ← a + b
        a ← b
        b ← c
      }
      
      write("Fibonacci(", n, ") = ", b)
    }
  }
}

algorithm FibonacciRekurencyjnie(n) {
  read(n)
  wynik ← FibRek(n)
  write("Fibonacci(", n, ") = ", wynik)
}

algorithm FibRek(n) {
  if n ≤ 0 then {
    return 0
  }
  
  if n = 1 or n = 2 then {
    return 1
  } else {
    return FibRek(n - 1) + FibRek(n - 2)
  }
}
```

Złożoność: Iteracyjnie O(n), Rekurencyjnie O(2^n)
