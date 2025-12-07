````markdown
# Maksimum w Tablicy - Dziel i Zwyciężaj

```pseudocode
algorithm MaximumDzielZwyciezaj(A, lewy, prawy) {
  if lewy == prawy then {
    return A[lewy]
  }
  
  if prawy == lewy + 1 then {
    if A[lewy] > A[prawy] then {
      return A[lewy]
    } else {
      return A[prawy]
    }
  }
  
  srodek ← (lewy + prawy) / 2
  
  max_lewy ← MaximumDzielZwyciezaj(A, lewy, srodek)
  max_prawy ← MaximumDzielZwyciezaj(A, srodek + 1, prawy)
  
  if max_lewy > max_prawy then {
    return max_lewy
  } else {
    return max_prawy
  }
}

algorithm ZnajdzMax(A, n) {
  read(n)
  
  for i ← 1 to n do {
    read(A[i])
  }
  
  maksimum ← MaximumDzielZwyciezaj(A, 1, n)
  
  write("Maksimum: ", maksimum)
  return maksimum
}
```

Złożoność: O(n) czasowa, O(log n) pamięciowa (stos rekursji)

````
