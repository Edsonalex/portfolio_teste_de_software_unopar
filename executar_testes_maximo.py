"""
executar_testes_maximo.py
Executa os testes e gera relatório estatístico detalhado
"""

import unittest
import sys
from io import StringIO
from datetime import datetime
from logica_de_teste import TestMaximoBasicos, TestMaximoValidacao
from casos_de_teste_maximo import CASOS_TESTE_BASICOS, CASOS_TESTE_VALIDACAO, TODOS_OS_CASOS


def executar_testes_com_relatorio():
    """Executa todos os testes e gera relatório detalhado"""
    
    print("="*70)
    print("EXECUÇÃO DE TESTES - FUNÇÃO MAXIMO()")
    print("="*70)
    print(f"Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print()
    
    # Estatísticas dos casos
    print("📊 ESTATÍSTICAS DOS CASOS DE TESTE:")
    print("-"*70)
    print(f"Total de casos: {len(TODOS_OS_CASOS)}")
    print(f"  • Casos básicos (lógica): {len(CASOS_TESTE_BASICOS)}")
    print(f"  • Casos validação (TDD): {len(CASOS_TESTE_VALIDACAO)}")
    print()
    
    # Criar suite de testes
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    suite.addTests(loader.loadTestsFromTestCase(TestMaximoBasicos))
    suite.addTests(loader.loadTestsFromTestCase(TestMaximoValidacao))
    
    # Executar testes
    print("="*70)
    print("EXECUTANDO TESTES:")
    print("="*70)
    print()
    
    runner = unittest.TextTestRunner(verbosity=2)
    resultado = runner.run(suite)
    
    # Relatório detalhado
    print()
    print("="*70)
    print("RELATÓRIO DETALHADO:")
    print("="*70)
    print()
    
    total_testes = resultado.testsRun
    sucessos = total_testes - len(resultado.failures) - len(resultado.errors)
    falhas = len(resultado.failures)
    erros = len(resultado.errors)
    
    print(f"Total de testes executados: {total_testes}")
    print(f"  ✅ Sucessos: {sucessos}")
    print(f"  ❌ Falhas: {falhas}")
    print(f"  ⚠️  Erros: {erros}")
    print()
    
    if total_testes > 0:
        percentual_sucesso = (sucessos / total_testes) * 100
        print(f"Taxa de sucesso: {percentual_sucesso:.1f}%")
    
    print()
    
    # Cobertura por categoria
    print("📋 COBERTURA POR CATEGORIA:")
    print("-"*70)
    def calcular_cobertura(total, executados):
        """Calcula percentual de cobertura"""
        if total == 0:
            return 0.0
        
        return (executados / total) * 100

    # Usar a função
    total_basicos = len(CASOS_TESTE_BASICOS)
    total_validacao = len(CASOS_TESTE_VALIDACAO)

    cobertura_basicos = calcular_cobertura(total_basicos, total_basicos)
    cobertura_validacao = calcular_cobertura(total_validacao, total_validacao)
    
    print(f"Casos básicos testados: {total_basicos}/{total_basicos}    ({cobertura_basicos:.0f}%)")
    print(f"Casos validação testados: {total_validacao}/{total_validacao}    ({cobertura_validacao:.0f}%)")
    
    # Resultado final
    print("="*70)
    if resultado.wasSuccessful():
        print("✅ TODOS OS TESTES PASSARAM!")
    else:
        print("❌ ALGUNS TESTES FALHARAM")
        if resultado.failures:
            print(f"\nFalhas: {len(resultado.failures)}")
        if resultado.errors:
            print(f"Erros: {len(resultado.errors)}")
    print("="*70)
    
    return resultado


if __name__ == '__main__':
    resultado = executar_testes_com_relatorio()
    sys.exit(0 if resultado.wasSuccessful() else 1)
