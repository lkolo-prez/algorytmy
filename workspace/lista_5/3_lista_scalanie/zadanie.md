````markdown
# Scalanie Dwóch Posortowanych List

```pseudocode
algorithm ScalListy(lista1, lista2) {
  if lista1 == NULL then {
    return lista2
  }
  
  if lista2 == NULL then {
    return lista1
  }
  
  wynik ← NULL
  
  if lista1->item <= lista2->item then {
    wynik ← lista1
    wynik->next ← ScalListy(lista1->next, lista2)
  } else {
    wynik ← lista2
    wynik->next ← ScalListy(lista1, lista2->next)
  }
  
  return wynik
}

algorithm ScalListyIteracyjnie(lista1, lista2) {
  if lista1 == NULL then {
    return lista2
  }
  if lista2 == NULL then {
    return lista1
  }
  
  if lista1->item <= lista2->item then {
    wynik ← lista1
    ogon ← lista1
    lista1 ← lista1->next
  } else {
    wynik ← lista2
    ogon ← lista2
    lista2 ← lista2->next
  }
  
  while lista1 != NULL and lista2 != NULL do {
    if lista1->item <= lista2->item then {
      ogon->next ← lista1
      ogon ← lista1
      lista1 ← lista1->next
    } else {
      ogon->next ← lista2
      ogon ← lista2
      lista2 ← lista2->next
    }
  }
  
  if lista1 != NULL then {
    ogon->next ← lista1
  } else {
    ogon->next ← lista2
  }
  
  write("Listy scalone")
  return wynik
}
```

Złożoność: O(n+m) czasowa, O(1) pamięciowa (iteracyjnie), O(n+m) (rekurencyjnie)

````
