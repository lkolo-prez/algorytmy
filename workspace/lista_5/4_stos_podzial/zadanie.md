````markdown
# Stos - Podział na Parzyste i Nieparzyste

```pseudocode
algorithm PodzielStosParzysteNieparzyste(S) {
  Sparzyste ← NowyStack()
  Snieparzyste ← NowyStack()
  
  while S.EMPTY() == 0 do {
    element ← S.POP()
    
    if element % 2 == 0 then {
      Sparzyste.PUSH(element)
      write(element, " -> stos parzystych")
    } else {
      Snieparzyste.PUSH(element)
      write(element, " -> stos nieparzystych")
    }
  }
  
  write("Stos parzystych:")
  while Sparzyste.EMPTY() == 0 do {
    write(Sparzyste.POP())
  }
  
  write("Stos nieparzystych:")
  while Snieparzyste.EMPTY() == 0 do {
    write(Snieparzyste.POP())
  }
}
```

Złożoność: O(n) czasowa, O(n) pamięciowa

````
