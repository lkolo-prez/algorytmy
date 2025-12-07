````markdown
# Stos - Uporządkowanie Rosnąco

```pseudocode
algorithm UporzadkujStos(S) {
  P ← NowyStack()
  
  while S.EMPTY() == 0 do {
    temp ← S.POP()
    
    while P.EMPTY() == 0 and P.TOP() > temp do {
      S.PUSH(P.POP())
    }
    
    P.PUSH(temp)
  }
  
  while P.EMPTY() == 0 do {
    S.PUSH(P.POP())
  }
  
  write("Stos uporzadkowany (rosnaco od dna)")
}

algorithm TOP(S) {
  if S.EMPTY() == 1 then {
    return NULL
  }
  element ← S.POP()
  S.PUSH(element)
  return element
}
```

Złożoność: O(n²) czasowa, O(n) pamięciowa

````
