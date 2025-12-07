````markdown
# Stos - Odwracanie Tekstu

```pseudocode
algorithm OdwrocTekst(tekst, n) {
  read(n)
  S ← NowyStack()
  
  for i ← 1 to n do {
    read(tekst[i])
    S.PUSH(tekst[i])
  }
  
  write("Odwrocony tekst: ")
  i ← 1
  
  while S.EMPTY() == 0 do {
    tekst[i] ← S.POP()
    write(tekst[i])
    i ← i + 1
  }
}
```

Złożoność: O(n) czasowa, O(n) pamięciowa

````
