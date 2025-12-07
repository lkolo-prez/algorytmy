````markdown
# Lista Jednokierunkowa - Usuwanie Elementu

```pseudocode
algorithm UsunElement(lista, wartosc) {
  read(wartosc)
  
  if lista == NULL then {
    write("Lista pusta")
    return NULL
  }
  
  if lista->item == wartosc then {
    temp ← lista
    lista ← lista->next
    write("Usunieto ", wartosc, " z poczatku")
    return lista
  }
  
  aktualny ← lista
  
  while aktualny->next != NULL do {
    if aktualny->next->item == wartosc then {
      temp ← aktualny->next
      aktualny->next ← aktualny->next->next
      write("Usunieto ", wartosc)
      return lista
    }
    aktualny ← aktualny->next
  }
  
  write("Nie znaleziono ", wartosc)
  return lista
}
```

Złożoność: O(n) czasowa, O(1) pamięciowa

````
