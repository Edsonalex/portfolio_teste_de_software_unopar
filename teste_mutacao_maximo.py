"""
teste_mutacao_maximo.py
Executor do teste de mutação com relatório detalhado
"""

from datetime import datetime
from mutantes_maximo import MUTANTES, maximo_original
from casos_de_teste_maximo import CASOS_TESTE_BASICOS
from logica_teste_mutacao import testar_mutante, calcular_mutation_score, executar_teste_contra_funcao


def executar_teste_mutacao():
    """Executa teste de mutação e gera relatório detalhado"""
    
    print("="*70)
    print("TESTE DE MUTAÇÃO - FUNÇÃO MAXIMO()")
    print("="*70)
    print(f"Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print()
    
    print("📊 INFORMAÇÕES:")
    print("-"*70)
    print(f"Total de mutantes: {len(MUTANTES)}")
    print(f"Casos de teste (básicos): {len(CASOS_TESTE_BASICOS)}")
    print()
    
    # Testar função original
    print("="*70)
    print("1. TESTANDO FUNÇÃO ORIGINAL:")
    print("="*70)
    casos_falharam = executar_teste_contra_funcao(maximo_original, CASOS_TESTE_BASICOS)
    
    if len(casos_falharam) == 0:
        print("✅ Função original passou em todos os testes")
    else:
        print(f"❌ Função original falhou em {len(casos_falharam)} casos")
    print()
    
    # Testar mutantes
    print("="*70)
    print("2. TESTANDO MUTANTES:")
    print("="*70)
    print()
    
    mutantes_mortos = []
    mutantes_vivos = []
    
    for mutante in MUTANTES:
        print(f"Testando Mutante #{mutante['id']}: {mutante['nome']}")
        
        morto = testar_mutante(mutante, CASOS_TESTE_BASICOS)
        
        if morto:
            print(f"  ✅ MORTO - Detectado pelos testes")
            mutantes_mortos.append(mutante)
        else:
            print(f"  ❌ VIVO - NÃO detectado pelos testes")
            mutantes_vivos.append(mutante)
        print()
    
    # Relatório final
    print("="*70)
    print("RELATÓRIO FINAL:")
    print("="*70)
    print()
    
    total = len(MUTANTES)
    mortos = len(mutantes_mortos)
    vivos = len(mutantes_vivos)
    
    print(f"Total de mutantes: {total}")
    print(f"  ✅ Mutantes mortos: {mortos}")
    print(f"  ❌ Mutantes vivos: {vivos}")
    print()
    
    mutation_score = calcular_mutation_score(total, mortos)
    print(f"📊 MUTATION SCORE: {mutation_score:.1f}%")
    print()
    
    # Detalhamento por tipo
    tipos_count = {}
    for mutante in mutantes_mortos:
        tipo = mutante["tipo"]
        tipos_count[tipo] = tipos_count.get(tipo, 0) + 1
    
    if tipos_count:
        print("Mutantes mortos por tipo:")
        for tipo, count in sorted(tipos_count.items()):
            print(f"  • {tipo}: {count}")
        print()
    
    # Mutantes vivos (problemas)
    if mutantes_vivos:
        print("⚠️  ATENÇÃO - Mutantes que sobreviveram:")
        for mutante in mutantes_vivos:
            print(f"  • Mutante #{mutante['id']}: {mutante['nome']}")
        print()
    
    print("="*70)
    if mutation_score >= 70:
        print(f"✅ QUALIDADE BOA - Mutation Score: {mutation_score:.1f}%")
    else:
        print(f"⚠️  QUALIDADE BAIXA - Mutation Score: {mutation_score:.1f}%")
    print("="*70)


if __name__ == '__main__':
    executar_teste_mutacao()
