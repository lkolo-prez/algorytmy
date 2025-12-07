````markdown
# Lista Jednokierunkowa - Dodawanie Przed Elementem

```pseudocode
algorithm DodajPrzed(lista, wartosc, cel) {
  read(wartosc)
  read(cel)
  
  nowy ← NowyWezel(wartosc)
  
  if lista == NULL then {
    write("Lista pusta")
    return NULL
  }
  
  if lista->item == cel then {
    nowy->next ← lista
    lista ← nowy
    write("Dodano ", wartosc, " przed ", cel)
    return lista
  }
  
  aktualny ← lista
  
  while aktualny->next != NULL do {
    if aktualny->next->item == cel then {
      nowy->next ← aktualny->next
      aktualny->next ← nowy
      write("Dodano ", wartosc, " przed ", cel)
      return lista
    }
    aktualny ← aktualny->next
  }
  
  write("Nie znaleziono elementu ", cel)
  return lista
}
```

Złożoność: O(n) czasowa, O(1) pamięciowa

````
