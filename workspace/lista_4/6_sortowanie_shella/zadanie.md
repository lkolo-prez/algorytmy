````markdown
# Sortowanie metodą Shella (Malejących Przyrostów)

```pseudocode
algorithm SortowanieShella(A, n) {
  read(n)
  
  for i ← 1 to n do {
    read(A[i])
  }
  
  gap ← n / 2
  
  while gap > 0 do {
    for i ← gap + 1 to n do {
      temp ← A[i]
      j ← i
      
      while j > gap and A[j - gap] > temp do {
        A[j] ← A[j - gap]
        j ← j - gap
      }
      
      A[j] ← temp
    }
    
    gap ← gap / 2
  }
  
  write("Posortowana tablica:")
  for i ← 1 to n do {
    write(A[i], " ")
  }
}
```

Złożoność: O(n²) czasowa (pesymistyczna), O(n log n) średnia, O(1) pamięciowa

````
