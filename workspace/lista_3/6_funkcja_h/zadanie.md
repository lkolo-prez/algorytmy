# Funkcja h(n)

```pseudocode
algorithm FunkcjaH(n) {
  read(n)
  wynik ← HRek(n)
  write("h(", n, ") = ", wynik)
}

algorithm HRek(n) {
  if n = 0 then {
    return 0
  } else {
    if n = 1 then {
      return 1
    } else {
      if n mod 2 = 0 then {
        return HRek(n div 2)
      } else {
        return HRek((n + 1) div 2) + HRek((n - 1) div 2) + 1
      }
    }
  }
}
```

Złożoność: O(n) czasowa (z memoizacją), O(log n) pamięciowa
