# Silnia - Rekurencyjnie

```pseudocode
algorithm SilniaRekurencyjnie(n) {
  read(n)
  
  if n < 0 then {
    write("Błąd: n nie może być ujemne")
  } else {
    wynik ← SilniaRek(n)
    write(n, "! = ", wynik)
  }
}

algorithm SilniaRek(n) {
  if n = 0 or n = 1 then {
    return 1
  } else {
    return n · SilniaRek(n - 1)
  }
}
```

Złożoność: O(n) czasowa, O(n) pamięciowa (stos rekursji)
