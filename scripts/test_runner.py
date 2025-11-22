#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test Runner - Automatyczne testowanie algorytmów pseudokodu
Wczytuje testy z plików JSON (zamiast YAML)
"""

import json
import sys
from pathlib import Path
from interpreter import PseudocodeInterpreter
import re


class TestRunner:
    """Runner dla testów algorytmów"""
    
    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.passed = 0
        self.failed = 0
        
    def load_test_file(self, test_path: Path) -> dict:
        """Wczytaj plik testowy JSON"""
        with open(test_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def load_algorithm(self, algo_path: Path) -> str:
        """Wczytaj algorytm z pliku markdown"""
        with open(algo_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Wyodrębnij blok pseudocode
        match = re.search(r'```pseudocode\s*\n(.*?)\n```', content, re.DOTALL)
        if not match:
            raise ValueError(f"Brak bloku ```pseudocode w {algo_path}")
        
        return match.group(1)
    
    def run_test_case(self, algorithm_code: str, test_case: dict) -> bool:
        """
        Uruchom pojedynczy test
        Returns: True jeśli test przeszedł, False w przeciwnym razie
        """
        test_name = test_case.get('name', 'Unnamed test')
        input_values = test_case.get('input', [])
        expected_output = test_case.get('expected_output', [])
        expected_return = test_case.get('expected_return', None)
        
        try:
            # Uruchom interpreter
            interpreter = PseudocodeInterpreter(debug_mode=False)
            result = interpreter.run(algorithm_code, input_values=input_values)
            actual_output = interpreter.get_output()
            
            # Sprawdź output
            output_ok = actual_output == expected_output
            
            # Sprawdź return
            return_ok = True
            if expected_return is not None:
                return_ok = result == expected_return
            
            # Test przeszedł?
            passed = output_ok and return_ok
            
            if passed:
                print(f"  ✅ {test_name}")
                self.passed += 1
            else:
                print(f"  ❌ {test_name}")
                self.failed += 1
                
                if not output_ok:
                    print(f"     Oczekiwany output: {expected_output}")
                    print(f"     Otrzymany output:  {actual_output}")
                
                if not return_ok:
                    print(f"     Oczekiwany return: {expected_return}")
                    print(f"     Otrzymany return:  {result}")
            
            if self.verbose and passed:
                print(f"     Input:  {input_values}")
                print(f"     Output: {actual_output}")
                if result is not None:
                    print(f"     Return: {result}")
            
            return passed
            
        except Exception as e:
            print(f"  ❌ {test_name}")
            print(f"     BŁĄD: {e}")
            self.failed += 1
            return False
    
    def run_tests(self, test_path: Path, algo_path: Path):
        """Uruchom wszystkie testy dla algorytmu"""
        print(f"\n{'='*60}")
        print(f"🧪 TESTOWANIE: {algo_path.name}")
        print(f"{'='*60}\n")
        
        # Wczytaj test i algorytm
        test_data = self.load_test_file(test_path)
        algorithm_code = self.load_algorithm(algo_path)
        
        algo_name = test_data.get('algorithm', 'Unknown')
        description = test_data.get('description', '')
        
        print(f"📋 Algorytm: {algo_name}")
        if description:
            print(f"📝 Opis: {description}")
        print()
        
        # Uruchom każdy test case
        test_cases = test_data.get('test_cases', [])
        for test_case in test_cases:
            self.run_test_case(algorithm_code, test_case)
        
        print()
    
    def print_summary(self):
        """Wyświetl podsumowanie"""
        total = self.passed + self.failed
        
        print(f"{'='*60}")
        print(f"📊 PODSUMOWANIE")
        print(f"{'='*60}")
        print(f"Testy wykonane: {total}")
        print(f"✅ Przeszły:    {self.passed}")
        print(f"❌ Nieprzeszły: {self.failed}")
        
        if self.failed == 0:
            print(f"\n🎉 Wszystkie testy przeszły pomyślnie!")
        else:
            print(f"\n⚠️  {self.failed} test(ów) nie przeszło")
        print()


def main():
    """Main"""
    if len(sys.argv) < 3:
        print("Użycie: python test_runner.py <test.json> <algorithm.md> [--verbose]")
        print("\nPrzykład:")
        print("  python test_runner.py tests/test_suma.json workspace/suma.md")
        print("  python test_runner.py tests/test_suma.json workspace/suma.md --verbose")
        return
    
    test_path = Path(sys.argv[1])
    algo_path = Path(sys.argv[2])
    verbose = '--verbose' in sys.argv or '-v' in sys.argv
    
    # Sprawdź czy pliki istnieją
    if not test_path.exists():
        print(f"❌ Plik testowy nie istnieje: {test_path}")
        return
    
    if not algo_path.exists():
        print(f"❌ Plik algorytmu nie istnieje: {algo_path}")
        return
    
    # Uruchom testy
    runner = TestRunner(verbose=verbose)
    
    try:
        runner.run_tests(test_path, algo_path)
        runner.print_summary()
        
        # Exit code
        sys.exit(0 if runner.failed == 0 else 1)
        
    except Exception as e:
        print(f"❌ KRYTYCZNY BŁĄD: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(2)


if __name__ == "__main__":
    main()
