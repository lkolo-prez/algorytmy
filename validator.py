#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VALIDATOR PSEUDOKODU - Algorytmy i Struktury Danych
Weryfikuje pseudokod pod kątem zgodności z definicją Mariusza Sobola (składnia {})

Użycie:
    python validator.py lista_1/1_suma_elementow/zadanie.md
    python validator.py lista_*/*/zadanie.md
    python validator.py --all
"""

import re
import sys
import os
from pathlib import Path

# KOLORY DO TERMINALA
class Colors:
    OK = '\033[92m'      # Zielony
    FAIL = '\033[91m'    # Czerwony
    WARN = '\033[93m'    # Żółty
    INFO = '\033[94m'    # Niebieski
    RESET = '\033[0m'    # Reset
    BOLD = '\033[1m'     # Bold


class PseudocodeValidator:
    """Validator pseudokodu wg definicji Sobola - składnia z {}"""
    
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.content = ""
        self.pseudocode = ""
        self.errors = []
        self.warnings = []
        self.info = []
        
    def read_file(self) -> bool:
        """Wczytaj plik"""
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                self.content = f.read()
            return True
        except FileNotFoundError:
            print(f"{Colors.FAIL}❌ BŁĄD: Plik nie znaleziony: {self.filepath}{Colors.RESET}")
            return False
        except Exception as e:
            print(f"{Colors.FAIL}❌ BŁĄD: {e}{Colors.RESET}")
            return False
    
    def extract_pseudocode(self) -> bool:
        """Wyodrębnij pseudokod między ```pseudocode i ```"""
        pattern = r'```pseudocode\s*\n(.*?)\n```'
        match = re.search(pattern, self.content, re.DOTALL)
        
        if not match:
            self.errors.append("Brak bloku pseudokodu (```pseudocode...```)")
            return False
        
        self.pseudocode = match.group(1)
        return True
    
    def check_structure(self) -> bool:
        """Sprawdzaj strukturę algorytmu - algorithm...{...}"""
        # Sprawdź czy jest algorithm z {
        if not re.search(r'^\s*algorithm\s+\w+\s*\([^)]*\)\s*\{', self.pseudocode, re.MULTILINE):
            self.errors.append("Brak definicji: `algorithm NazwaAlgorytmu(...) {`")
            return False
        else:
            self.info.append("Struktura algorytmu - OK")
        
        # Sprawdź czy NIE MA end algorithm (stary format)
        if re.search(r'end\s+algorithm', self.pseudocode, re.IGNORECASE):
            self.errors.append("Znaleziono zakazane: `end algorithm` - użyj `}` zamiast")
            return False
        
        return True
    
    def check_braces(self) -> bool:
        """Sprawdzaj balans nawiasów klamrowych {}"""
        open_count = self.pseudocode.count('{')
        close_count = self.pseudocode.count('}')
        
        if open_count != close_count:
            self.errors.append(
                f"Niezgodna liczba nawiasów klamrowych: {{ ({open_count}) vs }} ({close_count})"
            )
            return False
        
        if open_count > 0:
            self.info.append(f"Nawiasy klamrowe - OK ({open_count} par)")
        
        return True
    
    def check_forbidden_ends(self) -> bool:
        """Sprawdzaj czy NIE MA zakazanych 'end if/for/while'"""
        forbidden = []
        
        if re.search(r'\bend\s+if\b', self.pseudocode, re.IGNORECASE):
            forbidden.append("end if")
        if re.search(r'\bend\s+for\b', self.pseudocode, re.IGNORECASE):
            forbidden.append("end for")
        if re.search(r'\bend\s+while\b', self.pseudocode, re.IGNORECASE):
            forbidden.append("end while")
        
        if forbidden:
            self.errors.append(
                f"Zakazane składnie (użyj `}}` zamiast): {', '.join(forbidden)}"
            )
            return False
        
        self.info.append("Brak zakazanych `end if/for/while` - OK")
        return True
    
    def check_assignment(self) -> bool:
        """Sprawdzaj przypisania"""
        count = len(re.findall(r'←', self.pseudocode))
        
        # Szukaj złych przypisań - ale ignoruj = w kontekście porównań
        bad_assignments = []
        
        # Sprawdź := (zawsze błąd)
        if re.search(r':=', self.pseudocode):
            bad_assignments.append(":= (zamiast ←)")
        
        # Sprawdź = tylko na początku linii (nie w warunkach if/while)
        # Ignoruj linie z if, while, for, return, read, write
        lines = self.pseudocode.split('\n')
        for line in lines:
            stripped = line.strip()
            # Pomiń linie z warunkami
            if any(stripped.startswith(kw) for kw in ['if ', 'while ', 'for ', 'return ', 'read', 'write', '//', 'algorithm']):
                continue
            # Pomiń puste linie i zamykające nawiasy
            if not stripped or stripped == '}':
                continue
            # Szukaj = jako przypisania (nie porównania)
            if re.search(r'^\s*\w+\s*=\s*', line):
                # Sprawdź czy to nie jest porównanie w kontekście warunku
                if '←' not in line:  # Jeśli nie ma też ←, to prawdopodobnie błąd
                    bad_assignments.append(f"= w linii: {stripped[:50]}")
                    break
        
        if bad_assignments:
            self.errors.append(f"Złe przypisania: {', '.join(bad_assignments)}")
            return False
        
        if count > 0:
            self.info.append(f"Przypisania - OK ({count} znalezionych)")
        
        return True
    
    def check_conditionals(self) -> bool:
        """Sprawdzaj instrukcje warunkowe - if...then {...}"""
        # Szukaj if
        if_count = len(re.findall(r'^\s*if\s+', self.pseudocode, re.MULTILINE))
        
        if if_count > 0:
            # Sprawdź czy są 'then {'
            then_count = len(re.findall(r'\s+then\s*\{', self.pseudocode))
            
            if then_count < if_count:
                self.warnings.append(
                    f"Możliwy błąd: if ({if_count}) vs then {{ ({then_count}) - sprawdź składnię"
                )
            else:
                self.info.append(f"Instrukcje warunkowe - OK ({if_count} znalezione)")
        
        # Sprawdź czy są 'else {'
        else_count = len(re.findall(r'\}\s*else\s*\{', self.pseudocode))
        if else_count > 0:
            self.info.append(f"Bloki else - OK ({else_count} znalezione)")
        
        return True
    
    def check_loops(self) -> bool:
        """Sprawdzaj pętle - for/while...do {...}"""
        # Szukaj for
        for_count = len(re.findall(r'^\s*for\s+\w+\s*←', self.pseudocode, re.MULTILINE))
        
        if for_count > 0:
            for_do_count = len(re.findall(r'\s+do\s*\{', self.pseudocode))
            
            if for_do_count < for_count:
                self.warnings.append(
                    f"Możliwy błąd: for ({for_count}) vs do {{ ({for_do_count})"
                )
            else:
                self.info.append(f"Pętle for - OK ({for_count} znalezione)")
        
        # Szukaj while
        while_count = len(re.findall(r'^\s*while\s+', self.pseudocode, re.MULTILINE))
        
        if while_count > 0:
            self.info.append(f"Pętle while - OK ({while_count} znalezione)")
        
        return True
    
    def check_operators(self) -> bool:
        """Sprawdzaj operatory logiczne"""
        result = True
        
        # Szukaj złych operatorów
        bad_ops = []
        
        if re.search(r'\bAND\b', self.pseudocode):
            bad_ops.append("AND (zamiast and)")
        if re.search(r'\bOR\b', self.pseudocode):
            bad_ops.append("OR (zamiast or)")
        if re.search(r'\bNOT\b', self.pseudocode):
            bad_ops.append("NOT (zamiast not)")
        
        if bad_ops:
            self.errors.append(f"Złe operatory logiczne: {', '.join(bad_ops)}")
            result = False
        
        # Szukaj prawidłowych
        good_and = len(re.findall(r'\band\b', self.pseudocode))
        good_or = len(re.findall(r'\bor\b', self.pseudocode))
        good_not = len(re.findall(r'\bnot\b', self.pseudocode))
        
        if good_and > 0 or good_or > 0 or good_not > 0:
            self.info.append(
                f"Operatory logiczne - OK (and: {good_and}, or: {good_or}, not: {good_not})"
            )
        
        return result
    
    def check_arrays(self) -> bool:
        """Sprawdzaj dostęp do tablic"""
        # Szukaj dostępu do tablic
        array_access = re.findall(r'([A-Z]\[[^\]]+\])', self.pseudocode)
        
        if array_access:
            self.info.append(f"Tablice - OK ({len(array_access)} dostępów)")
            
            # Ostrzeż o indeksowaniu od 0
            if re.search(r'\[0\]', self.pseudocode):
                self.warnings.append(
                    "Możliwy błąd: Indeksowanie od 0 (powinno być od 1)"
                )
                return False
        
        return True
    
    def check_io(self) -> bool:
        """Sprawdzaj operacje we/wy"""
        read_count = len(re.findall(r'read\s*\(', self.pseudocode))
        write_count = len(re.findall(r'write\s*\(', self.pseudocode))
        
        # Szukaj złych funkcji we/wy
        bad_io = []
        if re.search(r'\binput\s*\(', self.pseudocode):
            bad_io.append("input (zamiast read)")
        if re.search(r'\bprint\s*\(', self.pseudocode):
            bad_io.append("print (zamiast write)")
        
        if bad_io:
            self.errors.append(f"Złe funkcje we/wy: {', '.join(bad_io)}")
            return False
        
        if read_count > 0 or write_count > 0:
            self.info.append(f"Operacje we/wy - OK (read: {read_count}, write: {write_count})")
        
        return True
    
    def validate(self) -> bool:
        """Uruchom wszystkie sprawdzenia"""
        if not self.read_file():
            return False
        
        if not self.extract_pseudocode():
            return False
        
        checks = [
            self.check_structure,
            self.check_braces,
            self.check_forbidden_ends,
            self.check_assignment,
            self.check_conditionals,
            self.check_loops,
            self.check_operators,
            self.check_arrays,
            self.check_io
        ]
        
        results = []
        for check in checks:
            try:
                results.append(check())
            except Exception as e:
                self.errors.append(f"BŁĄD SPRAWDZANIA: {check.__name__}: {e}")
                results.append(False)
        
        return all(results)
    
    def print_report(self):
        """Wydrukuj raport"""
        basename = os.path.basename(os.path.dirname(self.filepath))
        filename = os.path.basename(self.filepath)
        print(f"\n{'='*60}")
        print(f"{Colors.BOLD}WALIDACJA: {basename}/{filename}{Colors.RESET}")
        print(f"{'='*60}\n")
        
        # Info (zielone)
        if self.info:
            for msg in self.info:
                print(f"{Colors.OK}✅ {msg}{Colors.RESET}")
        
        # Błędy (czerwone)
        if self.errors:
            print()
            for msg in self.errors:
                print(f"{Colors.FAIL}❌ {msg}{Colors.RESET}")
        
        # Ostrzeżenia (żółte)
        if self.warnings:
            print()
            for msg in self.warnings:
                print(f"{Colors.WARN}⚠️  {msg}{Colors.RESET}")
        
        # Podsumowanie
        print(f"\n{'-'*60}")
        
        if not self.errors and not self.warnings:
            status = f"{Colors.OK}{Colors.BOLD}✅ PRAWIDŁOWY PSEUDOKOD{Colors.RESET}"
            ocena = 100
        elif not self.errors:
            status = f"{Colors.WARN}{Colors.BOLD}⚠️  OSTRZEŻENIA{Colors.RESET}"
            ocena = 80
        else:
            status = f"{Colors.FAIL}{Colors.BOLD}❌ BŁĘDY{Colors.RESET}"
            ocena = max(0, 100 - len(self.errors) * 20)
        
        print(f"STATUS: {status}")
        print(f"Ocena: {ocena}%")
        print(f"{'-'*60}\n")


def main():
    """Główna funkcja"""
    if len(sys.argv) < 2:
        print(f"{Colors.INFO}Użycie:{Colors.RESET}")
        print(f"  python validator.py lista_1/1_suma_elementow/zadanie.md")
        print(f"  python validator.py lista_*/*/zadanie.md")
        print(f"  python validator.py --all")
        sys.exit(1)
    
    if sys.argv[1] == "--all":
        # Zwaliduj wszystkie pliki
        files = sorted(Path('.').glob('lista_*/*/zadanie.md'))
    else:
        # Zwaliduj podane pliki (może być glob)
        import glob
        files = []
        for pattern in sys.argv[1:]:
            files.extend(glob.glob(pattern, recursive=True))
    
    if not files:
        print(f"{Colors.FAIL}❌ Nie znaleziono żadnych plików{Colors.RESET}")
        sys.exit(1)
    
    total_valid = 0
    total_errors = 0
    total_warnings = 0
    
    for filepath in sorted(files):
        validator = PseudocodeValidator(str(filepath))
        
        if validator.validate():
            total_valid += 1
        else:
            total_errors += len(validator.errors)
        
        total_warnings += len(validator.warnings)
        validator.print_report()
    
    # Podsumowanie
    print(f"{'='*60}")
    print(f"{Colors.BOLD}PODSUMOWANIE{Colors.RESET}")
    print(f"{'='*60}")
    print(f"Pliki do walidacji: {len(files)}")
    print(f"{Colors.OK}Prawidłowe: {total_valid}{Colors.RESET}")
    print(f"{Colors.FAIL}Błędy: {total_errors}{Colors.RESET}")
    print(f"{Colors.WARN}Ostrzeżenia: {total_warnings}{Colors.RESET}")
    print(f"{'='*60}\n")
    
    if total_errors > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
