````markdown
# Sortowanie przez Wstawianie Połówkowe

```pseudocode
algorithm WyszukiwanieBinarne(A, item, low, high) {
  if high <= low then {
    if item > A[low] then {
      return low + 1
    } else {
      return low
    }
  }
  
  mid ← (low + high) / 2
  
  if item == A[mid] then {
    return mid + 1
  }
  
  if item > A[mid] then {
    return WyszukiwanieBinarne(A, item, mid + 1, high)
  }
  
  return WyszukiwanieBinarne(A, item, low, mid - 1)
}

algorithm SortowaniePolowkowe(A, n) {
  read(n)
  
  for i ← 1 to n do {
    read(A[i])
  }
  
  for i ← 2 to n do {
    klucz ← A[i]
    pos ← WyszukiwanieBinarne(A, klucz, 1, i - 1)
    j ← i - 1
    
    while j >= pos do {
      A[j + 1] ← A[j]
      j ← j - 1
    }
    
    A[pos] ← klucz
  }
  
  write("Posortowana tablica:")
  for i ← 1 to n do {
    write(A[i], " ")
  }
}
```

Złożoność: O(n²) czasowa, O(log n) pamięciowa (rekursja)

````
