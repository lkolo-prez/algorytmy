#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interpreter Pseudokodu - Wykonuje algorytmy zgodne ze składnią Mariusza Sobola
Wspiera debugowanie, śledzenie zmiennych, wykonanie krok po kroku
"""

import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from dataclasses import dataclass, field


@dataclass
class ExecutionContext:
    """Kontekst wykonania algorytmu"""
    variables: Dict[str, Any] = field(default_factory=dict)
    arrays: Dict[str, List[Any]] = field(default_factory=dict)
    algorithms: Dict[str, Tuple[List[str], List[str]]] = field(default_factory=dict)  # nazwa -> (parametry, kod)
    call_stack: List[str] = field(default_factory=list)
    step_count: int = 0
    max_steps: int = 10000
    debug_mode: bool = False
    input_values: List[str] = field(default_factory=list)
    input_index: int = 0
    output: List[str] = field(default_factory=list)


class PseudocodeInterpreter:
    """Interpreter dla pseudokodu"""
    
    def __init__(self, debug_mode: bool = False, max_steps: int = 10000):
        self.context = ExecutionContext(debug_mode=debug_mode, max_steps=max_steps)
        
    def parse_algorithm(self, code: str) -> Tuple[str, List[str], List[str]]:
        """
        Parsuj definicję algorytmu
        Returns: (nazwa, parametry, linie_kodu)
        """
        lines = code.strip().split('\n')
        
        # Znajdź definicję algorytmu
        alg_pattern = r'algorithm\s+(\w+)\s*\((.*?)\)\s*\{'
        for i, line in enumerate(lines):
            match = re.match(alg_pattern, line.strip())
            if match:
                name = match.group(1)
                params = [p.strip() for p in match.group(2).split(',') if p.strip()]
                
                # Zbierz linie kodu (bez pierwszej i ostatniej linii z nawiasami)
                code_lines = []
                brace_count = 0
                in_algorithm = False
                
                for j in range(i, len(lines)):
                    line = lines[j]
                    if '{' in line:
                        brace_count += line.count('{')
                        in_algorithm = True
                        if j > i:  # Nie dodawaj pierwszej linii
                            code_lines.append(line)
                    elif '}' in line:
                        brace_count -= line.count('}')
                        if brace_count == 0:
                            break
                        code_lines.append(line)
                    elif in_algorithm:
                        code_lines.append(line)
                
                return name, params, code_lines
        
        raise ValueError("Nie znaleziono definicji algorytmu")
    
    def parse_all_algorithms(self, code: str) -> Dict[str, Tuple[List[str], List[str]]]:
        """
        Parsuj wszystkie algorytmy z kodu
        Returns: dict {nazwa: (parametry, linie_kodu)}
        """
        algorithms = {}
        lines = code.strip().split('\n')
        
        alg_pattern = r'algorithm\s+(\w+)\s*\((.*?)\)\s*\{'
        i = 0
        while i < len(lines):
            match = re.match(alg_pattern, lines[i].strip())
            if match:
                name = match.group(1)
                params = [p.strip() for p in match.group(2).split(',') if p.strip()]
                
                # Zbierz linie kodu
                code_lines = []
                brace_count = 0
                in_algorithm = False
                
                for j in range(i, len(lines)):
                    line = lines[j]
                    if '{' in line:
                        brace_count += line.count('{')
                        in_algorithm = True
                        if j > i:
                            code_lines.append(line)
                    elif '}' in line:
                        brace_count -= line.count('}')
                        if brace_count == 0:
                            i = j + 1
                            break
                        code_lines.append(line)
                    elif in_algorithm:
                        code_lines.append(line)
                
                algorithms[name] = (params, code_lines)
            else:
                i += 1
        
        return algorithms
    
    def set_input(self, values: List[Any]):
        """Ustaw wartości wejściowe do wczytania przez read()"""
        self.context.input_values = [str(v) for v in values]
        self.context.input_index = 0
    
    def read_value(self) -> str:
        """Wczytaj wartość z listy input"""
        if self.context.input_index >= len(self.context.input_values):
            raise RuntimeError("Brak wartości wejściowych do wczytania")
        value = self.context.input_values[self.context.input_index]
        self.context.input_index += 1
        return value
    
    def write_value(self, *values):
        """Wypisz wartość"""
        output_str = ' '.join(str(v) for v in values)
        self.context.output.append(output_str)
        if self.context.debug_mode:
            print(f"📤 OUTPUT: {output_str}")
    
    def evaluate_expression(self, expr: str) -> Any:
        """
        Ewaluuj wyrażenie matematyczne/logiczne
        Obsługuje zmienne, tablice, operatory, wywołania funkcji
        """
        expr = expr.strip()
        
        # Usuń białe znaki wokół operatorów
        expr = re.sub(r'\s+', ' ', expr)
        
        # Obsługa wywołań algorytmów (np. ObliczSilnie(5))
        func_call_pattern = r'(\w+)\s*\(([^)]*)\)'
        func_matches = list(re.finditer(func_call_pattern, expr))
        
        for match in reversed(func_matches):  # Od tyłu, żeby nie zepsuć indeksów
            func_name = match.group(1)
            args_str = match.group(2)
            
            # Sprawdź czy to nie jest wbudowana funkcja Pythona
            if func_name in {'int', 'float', 'str', 'len', 'abs', 'min', 'max', 'sum'}:
                continue
            
            # Sprawdź czy to zdefiniowany algorytm
            if func_name in self.context.algorithms:
                # Ewaluuj argumenty
                args = []
                if args_str.strip():
                    for arg in args_str.split(','):
                        args.append(self.evaluate_expression(arg.strip()))
                
                # Wywołaj algorytm
                result = self.call_algorithm(func_name, args)
                
                # Zastąp wywołanie wynikiem
                expr = expr[:match.start()] + str(result) + expr[match.end():]
        
        # Zamień operatory pseudokodu na Python
        expr = expr.replace('≤', '<=').replace('≥', '>=').replace('≠', '!=')
        expr = expr.replace('·', '*').replace('^', '**')
        expr = expr.replace(' mod ', ' % ')
        expr = expr.replace(' div ', ' // ')
        expr = expr.replace(' and ', ' and ').replace(' or ', ' or ').replace(' not ', ' not ')
        
        # Zamień = na == w kontekście porównania (ale nie w przypisaniu)
        # Jeśli = jest otoczone spacjami lub w wyrażeniu warunkowym, to porównanie
        expr = re.sub(r'(\w+)\s*=\s*(\w+)', r'\1 == \2', expr)
        expr = re.sub(r'(\w+)\s*=\s*(-?\d+)', r'\1 == \2', expr)
        
        # Obsługa tablic - A[i] -> arrays['A'][i-1] (indeksowanie od 1)
        def replace_array_access(match):
            arr_name = match.group(1)
            indices = match.group(2)
            
            # Obsługa tablic 2D: A[i, j]
            if ',' in indices:
                idx_parts = indices.split(',')
                i_expr = self.evaluate_expression(idx_parts[0].strip())
                j_expr = self.evaluate_expression(idx_parts[1].strip())
                return f"self.context.arrays['{arr_name}'][{i_expr}-1][{j_expr}-1]"
            else:
                idx_expr = self.evaluate_expression(indices.strip())
                return f"self.context.arrays['{arr_name}'][{idx_expr}-1]"
        
        expr = re.sub(r'(\w+)\[([^\]]+)\]', replace_array_access, expr)
        
        # Zamień zmienne na wartości z kontekstu
        def replace_variable(match):
            var_name = match.group(0)
            if var_name in self.context.variables:
                return str(self.context.variables[var_name])
            return var_name
        
        # Zmienne (ale nie słowa kluczowe Python)
        keywords = {'and', 'or', 'not', 'True', 'False', 'None'}
        expr = re.sub(r'\b([a-zA-Z_]\w*)\b', 
                     lambda m: replace_variable(m) if m.group(0) not in keywords else m.group(0), 
                     expr)
        
        try:
            # Bezpieczna ewaluacja
            result = eval(expr, {"__builtins__": {}}, {"self": self})
            return result
        except Exception as e:
            raise RuntimeError(f"Błąd ewaluacji wyrażenia '{expr}': {e}")
    
    def execute_assignment(self, line: str):
        """Wykonaj przypisanie: zmienna ← wartość"""
        match = re.match(r'(\w+)\s*←\s*(.+)', line)
        if not match:
            return False
        
        var_name = match.group(1)
        expr = match.group(2)
        
        value = self.evaluate_expression(expr)
        self.context.variables[var_name] = value
        
        if self.context.debug_mode:
            print(f"  {var_name} ← {value}")
        
        return True
    
    def execute_array_assignment(self, line: str):
        """Wykonaj przypisanie do tablicy: A[i] ← wartość"""
        match = re.match(r'(\w+)\[([^\]]+)\]\s*←\s*(.+)', line)
        if not match:
            return False
        
        arr_name = match.group(1)
        index_expr = match.group(2)
        value_expr = match.group(3)
        
        # Obsługa 2D
        if ',' in index_expr:
            idx_parts = index_expr.split(',')
            i = int(self.evaluate_expression(idx_parts[0].strip()))
            j = int(self.evaluate_expression(idx_parts[1].strip()))
            value = self.evaluate_expression(value_expr)
            
            # Upewnij się, że tablica istnieje
            if arr_name not in self.context.arrays:
                self.context.arrays[arr_name] = []
            
            # Rozszerz tablicę jeśli potrzeba (indeksowanie od 1)
            while len(self.context.arrays[arr_name]) < i:
                self.context.arrays[arr_name].append([])
            while len(self.context.arrays[arr_name][i-1]) < j:
                self.context.arrays[arr_name][i-1].append(0)
            
            self.context.arrays[arr_name][i-1][j-1] = value
        else:
            index = int(self.evaluate_expression(index_expr))
            value = self.evaluate_expression(value_expr)
            
            # Upewnij się, że tablica istnieje
            if arr_name not in self.context.arrays:
                self.context.arrays[arr_name] = []
            
            # Rozszerz tablicę jeśli potrzeba (indeksowanie od 1)
            while len(self.context.arrays[arr_name]) < index:
                self.context.arrays[arr_name].append(0)
            
            self.context.arrays[arr_name][index-1] = value
        
        if self.context.debug_mode:
            print(f"  {arr_name}[{index_expr}] ← {value}")
        
        return True
    
    def execute_read(self, line: str):
        """Wykonaj wczytanie: read(zmienna) lub read(A[i])"""
        # Sprawdź czy to tablica
        array_match = re.match(r'read\((\w+)\[([^\]]+)\]\)', line.strip())
        if array_match:
            arr_name = array_match.group(1)
            index_expr = array_match.group(2)
            value_str = self.read_value()
            
            # Próba konwersji na int/float
            try:
                if '.' in value_str:
                    value = float(value_str)
                else:
                    value = int(value_str)
            except ValueError:
                value = value_str
            
            # Przypisz do tablicy
            index = int(self.evaluate_expression(index_expr))
            
            if arr_name not in self.context.arrays:
                self.context.arrays[arr_name] = []
            
            while len(self.context.arrays[arr_name]) < index:
                self.context.arrays[arr_name].append(0)
            
            self.context.arrays[arr_name][index-1] = value
            
            if self.context.debug_mode:
                print(f"📥 READ: {arr_name}[{index}] ← {value}")
            
            return True
        
        # Zwykła zmienna
        match = re.match(r'read\((\w+)\)', line.strip())
        if not match:
            return False
        
        var_name = match.group(1)
        value_str = self.read_value()
        
        # Próba konwersji na int/float
        try:
            if '.' in value_str:
                value = float(value_str)
            else:
                value = int(value_str)
        except ValueError:
            value = value_str
        
        self.context.variables[var_name] = value
        
        if self.context.debug_mode:
            print(f"📥 READ: {var_name} ← {value}")
        
        return True
    
    def execute_write(self, line: str):
        """Wykonaj wypisanie: write(wartość, ...)"""
        match = re.match(r'write\((.+)\)', line.strip())
        if not match:
            return False
        
        args_str = match.group(1)
        
        # Parsuj argumenty (mogą być stringi w cudzysłowach lub wyrażenia)
        values = []
        current = ""
        in_string = False
        
        for char in args_str:
            if char == '"':
                in_string = not in_string
            elif char == ',' and not in_string:
                values.append(current.strip())
                current = ""
                continue
            current += char
        
        if current.strip():
            values.append(current.strip())
        
        # Ewaluuj każdy argument
        output_values = []
        for val in values:
            if val.startswith('"') and val.endswith('"'):
                output_values.append(val[1:-1])  # String literal
            else:
                output_values.append(self.evaluate_expression(val))
        
        self.write_value(*output_values)
        return True
    
    def execute_lines(self, lines: List[str], start: int = 0, end: Optional[int] = None) -> Optional[Any]:
        """
        Wykonaj linie kodu
        Returns: wartość return (jeśli wystąpi) lub None
        """
        if end is None:
            end = len(lines)
        
        i = start
        while i < end:
            # Sprawdź limit kroków
            self.context.step_count += 1
            if self.context.step_count > self.context.max_steps:
                raise RuntimeError(f"Przekroczono limit kroków ({self.context.max_steps}). Prawdopodobnie nieskończona pętla!")
            
            line = lines[i].strip()
            
            # Pomiń puste linie, komentarze i zamykające nawiasy
            if not line or line.startswith('//') or line == '}':
                i += 1
                continue
            
            if self.context.debug_mode:
                print(f"[Krok {self.context.step_count}] {line}")
            
            # Return
            if line.startswith('return '):
                expr = line[7:].strip()
                value = self.evaluate_expression(expr)
                if self.context.debug_mode:
                    print(f"  ↩️  return {value}")
                return value
            
            # Read
            if self.execute_read(line):
                i += 1
                continue
            
            # Write
            if self.execute_write(line):
                i += 1
                continue
            
            # Array assignment
            if self.execute_array_assignment(line):
                i += 1
                continue
            
            # Variable assignment
            if self.execute_assignment(line):
                i += 1
                continue
            
            # If statement
            if line.startswith('if '):
                condition_match = re.match(r'if\s+(.+?)\s+then\s*\{', line)
                if condition_match:
                    condition = condition_match.group(1)
                    
                    # Znajdź bloki then i else
                    then_start = i + 1
                    then_end, else_start, else_end = self.find_if_blocks(lines, i)
                    
                    # Ewaluuj warunek
                    if self.evaluate_expression(condition):
                        result = self.execute_lines(lines, then_start, then_end)
                        if result is not None:
                            return result
                    elif else_start is not None:
                        result = self.execute_lines(lines, else_start, else_end)
                        if result is not None:
                            return result
                    
                    # Przeskocz do końca if-else
                    i = else_end if else_end else then_end
                    continue
            
            # For loop
            if line.startswith('for '):
                loop_match = re.match(r'for\s+(\w+)\s*←\s*(.+?)\s+to\s+(.+?)(?:\s+step\s+(.+?))?\s+do\s*\{', line)
                if loop_match:
                    var = loop_match.group(1)
                    start_val = int(self.evaluate_expression(loop_match.group(2)))
                    end_val = int(self.evaluate_expression(loop_match.group(3)))
                    step = int(self.evaluate_expression(loop_match.group(4))) if loop_match.group(4) else 1
                    
                    # Znajdź koniec pętli
                    loop_end = self.find_block_end(lines, i)
                    
                    # Wykonaj pętlę
                    for val in range(start_val, end_val + 1, step):
                        self.context.variables[var] = val
                        result = self.execute_lines(lines, i + 1, loop_end)
                        if result is not None:
                            return result
                    
                    i = loop_end
                    continue
            
            # While loop
            if line.startswith('while '):
                condition_match = re.match(r'while\s+(.+?)\s+do\s*\{', line)
                if condition_match:
                    condition = condition_match.group(1)
                    loop_end = self.find_block_end(lines, i)
                    
                    # Wykonuj pętlę dopóki warunek jest prawdziwy
                    while self.evaluate_expression(condition):
                        result = self.execute_lines(lines, i + 1, loop_end)
                        if result is not None:
                            return result
                    
                    i = loop_end
                    continue
            
            # Nieznana instrukcja
            raise RuntimeError(f"Nieznana instrukcja: {line}")
        
        return None
    
    def find_block_end(self, lines: List[str], start: int) -> int:
        """Znajdź koniec bloku (dopasowany })"""
        brace_count = 0
        for i in range(start, len(lines)):
            line = lines[i]
            brace_count += line.count('{')
            brace_count -= line.count('}')
            if brace_count == 0:
                return i + 1
        return len(lines)
    
    def find_if_blocks(self, lines: List[str], start: int) -> Tuple[int, Optional[int], int]:
        """
        Znajdź bloki then i else
        Returns: (then_end, else_start, else_end)
        """
        brace_count = 0
        in_then = True
        then_end = None
        else_start = None
        
        for i in range(start, len(lines)):
            line = lines[i].strip()
            
            if '{' in line:
                brace_count += line.count('{')
            
            if '}' in line:
                brace_count -= line.count('}')
                
                if brace_count == 0:
                    if in_then:
                        then_end = i
                        # Sprawdź czy jest else
                        if i + 1 < len(lines) and 'else' in lines[i + 1]:
                            in_then = False
                            else_start = i + 2  # Pomiń linię z 'else {'
                            brace_count = 1  # Rozpocznij liczenie dla else
                        else:
                            return then_end, None, then_end
                    else:
                        return then_end, else_start, i
        
        return then_end or len(lines), else_start, len(lines)
    
    def call_algorithm(self, name: str, args: List[Any]) -> Optional[Any]:
        """
        Wywołaj zdefiniowany algorytm
        
        Args:
            name: Nazwa algorytmu
            args: Argumenty wywołania
        
        Returns:
            Wartość zwrócona przez algorytm
        """
        if name not in self.context.algorithms:
            raise RuntimeError(f"Nie znaleziono algorytmu: {name}")
        
        param_names, code_lines = self.context.algorithms[name]
        
        if len(args) != len(param_names):
            raise RuntimeError(f"Błędna liczba argumentów dla {name}: oczekiwano {len(param_names)}, otrzymano {len(args)}")
        
        # Zapisz kontekst zmiennych (dla rekurencji)
        saved_vars = self.context.variables.copy()
        
        # Ustaw parametry
        for param_name, arg_value in zip(param_names, args):
            self.context.variables[param_name] = arg_value
        
        if self.context.debug_mode:
            print(f"📞 WYWOŁANIE: {name}({', '.join(str(a) for a in args)})")
        
        # Wykonaj algorytm
        result = self.execute_lines(code_lines)
        
        # Przywróć kontekst zmiennych
        self.context.variables = saved_vars
        
        if self.context.debug_mode:
            print(f"↩️  POWRÓT: {name} → {result}")
        
        return result
    
    def run(self, code: str, params: List[Any] = None, input_values: List[Any] = None) -> Optional[Any]:
        """
        Uruchom algorytm
        
        Args:
            code: Kod pseudokodu
            params: Wartości parametrów
            input_values: Wartości do wczytania przez read()
        
        Returns:
            Wartość zwrócona przez algorytm (jeśli jest return)
        """
        # Parsuj wszystkie algorytmy
        all_algorithms = self.parse_all_algorithms(code)
        if not all_algorithms:
            raise ValueError("Nie znaleziono żadnego algorytmu")
        
        # Zapisz wszystkie algorytmy w kontekście
        self.context.algorithms = all_algorithms
        
        # Uruchom pierwszy algorytm (główny)
        main_name = list(all_algorithms.keys())[0]
        param_names, code_lines = all_algorithms[main_name]
        
        if self.context.debug_mode:
            print(f"\n{'='*60}")
            print(f"🚀 URUCHOMIENIE: {main_name}({', '.join(param_names)})")
            if len(all_algorithms) > 1:
                print(f"📚 Zdefiniowane algorytmy: {', '.join(all_algorithms.keys())}")
            print(f"{'='*60}\n")
        
        # Ustaw parametry
        if params:
            for param_name, param_value in zip(param_names, params):
                self.context.variables[param_name] = param_value
                if self.context.debug_mode:
                    print(f"📌 {param_name} = {param_value}")
        
        # Ustaw input
        if input_values:
            self.set_input(input_values)
        
        # Wykonaj kod
        result = self.execute_lines(code_lines)
        
        if self.context.debug_mode:
            print(f"\n{'='*60}")
            print(f"✅ ZAKOŃCZONO")
            print(f"{'='*60}")
            print(f"📊 Kroki: {self.context.step_count}")
            print(f"📤 Output: {self.context.output}")
            if result is not None:
                print(f"↩️  Return: {result}")
        
        return result
    
    def get_output(self) -> List[str]:
        """Pobierz zapisany output"""
        return self.context.output


def main():
    """Uruchom interpreter z pliku"""
    if len(sys.argv) < 2:
        print("Użycie: python interpreter.py <plik.md> [--debug] [--input val1,val2,...]")
        print("\nPrzykład:")
        print("  python interpreter.py workspace/suma.md --input 5,1,2,3,4,5")
        return
    
    file_path = Path(sys.argv[1])
    debug_mode = '--debug' in sys.argv
    
    # Parsuj input
    input_values = []
    for arg in sys.argv:
        if arg.startswith('--input='):
            input_str = arg.split('=', 1)[1]
            input_values = input_str.split(',')
    
    # Wczytaj kod
    if not file_path.exists():
        print(f"❌ Plik nie istnieje: {file_path}")
        return
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Wyodrębnij blok ```pseudocode
    match = re.search(r'```pseudocode\s*\n(.*?)\n```', content, re.DOTALL)
    if not match:
        print("❌ Nie znaleziono bloku ```pseudocode w pliku")
        return
    
    code = match.group(1)
    
    # Uruchom interpreter
    try:
        interpreter = PseudocodeInterpreter(debug_mode=debug_mode)
        result = interpreter.run(code, input_values=input_values)
        
        # Wypisz output
        if not debug_mode:
            for line in interpreter.get_output():
                print(line)
        
        if result is not None and not debug_mode:
            print(f"Return: {result}")
            
    except Exception as e:
        print(f"❌ BŁĄD: {e}")
        import traceback
        if debug_mode:
            traceback.print_exc()


if __name__ == "__main__":
    main()
