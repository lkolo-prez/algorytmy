````markdown
# Implementacja Kolejki przez Dwa Stosy i Stosu przez Dwie Kolejki

```pseudocode
algorithm KolejkaPrzezStosy() {
  S1 ← NowyStack()
  S2 ← NowyStack()
  
  write("Kolejka przez dwa stosy:")
}

algorithm ENQUEUE(S1, S2, element) {
  S1.PUSH(element)
  write("Dodano ", element, " do kolejki")
}

algorithm DEQUEUE(S1, S2) {
  if S2.EMPTY() == 1 then {
    if S1.EMPTY() == 1 then {
      write("Kolejka pusta")
      return NULL
    }
    
    while S1.EMPTY() == 0 do {
      S2.PUSH(S1.POP())
    }
  }
  
  element ← S2.POP()
  write("Pobrано ", element, " z kolejki")
  return element
}

algorithm StosPrzezKolejki() {
  Q1 ← NowyQueue()
  Q2 ← NowyQueue()
  
  write("Stos przez dwie kolejki:")
}

algorithm PUSH_QUEUE(Q1, Q2, element) {
  Q1.PUT(element)
  write("Dodano ", element, " na stos")
}

algorithm POP_QUEUE(Q1, Q2) {
  if Q1.EMPTY() == 1 then {
    write("Stos pusty")
    return NULL
  }
  
  while Q1.EMPTY() == 0 do {
    element ← Q1.GET()
    
    if Q1.EMPTY() == 1 then {
      write("Zdjeto ", element, " ze stosu")
      
      while Q2.EMPTY() == 0 do {
        Q1.PUT(Q2.GET())
      }
      
      return element
    }
    
    Q2.PUT(element)
  }
}
```

Złożoność: 
- Kolejka przez stosy: ENQUEUE O(1), DEQUEUE O(n) najgorsza/O(1) zamortyzowana
- Stos przez kolejki: PUSH O(1), POP O(n)

````
