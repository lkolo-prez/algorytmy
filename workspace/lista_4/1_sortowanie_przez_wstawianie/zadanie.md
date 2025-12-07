````markdown
# Sortowanie przez Proste Wstawianie

```pseudocode
algorithm SortowaniePrzezWstawianie(A, n) {
  read(n)
  
  for i ← 1 to n do {
    read(A[i])
  }
  
  for i ← 2 to n do {
    klucz ← A[i]
    j ← i - 1
    
    while j >= 1 and A[j] > klucz do {
      A[j + 1] ← A[j]
      j ← j - 1
    }
    
    A[j + 1] ← klucz
  }
  
  write("Posortowana tablica:")
  for i ← 1 to n do {
    write(A[i], " ")
  }
}
```

Złożoność: O(n²) czasowa (pesymistyczna), O(n) (optymistyczna), O(1) pamięciowa

````
