# Wieże Hanoi

```pseudocode
algorithm WiezeHanoi(n, zrodlo, cel, pomocniczy) {
  read(n)
  WiezeRek(n, 1, 3, 2)
}

algorithm WiezeRek(n, zrodlo, cel, pomocniczy) {
  if n = 1 then {
    write("Przenieś krążek z ", zrodlo, " na ", cel)
  } else {
    WiezeRek(n - 1, zrodlo, pomocniczy, cel)
    write("Przenieś krążek z ", zrodlo, " na ", cel)
    WiezeRek(n - 1, pomocniczy, cel, zrodlo)
  }
}
```

Złożoność: O(2^n - 1) czasowa, O(n) pamięciowa (stos rekursji)
