"""
logica_teste_mutacao.py
Lógica dos testes de mutação
"""

from casos_de_teste_maximo import CASOS_TESTE_BASICOS


def executar_teste_contra_funcao(funcao, casos_teste):
    """
    Executa casos de teste contra uma função.
    Retorna lista de casos que falharam.
    """
    casos_falharam = []
    
    for caso in casos_teste:
        try:
            resultado = funcao(caso["a"], caso["b"])
            esperado_valor = int(caso["esperado"].split()[2])  # Extrai número
            
            if resultado != esperado_valor:
                casos_falharam.append(caso["id"])
        except Exception as e:
            casos_falharam.append(caso["id"])
    
    return casos_falharam


def testar_mutante(mutante, casos_teste):
    """
    Testa um mutante contra casos de teste.
    Retorna True se mutante foi morto, False se sobreviveu.
    """
    casos_falharam = executar_teste_contra_funcao(mutante["funcao"], casos_teste)
    return len(casos_falharam) > 0


def calcular_mutation_score(total_mutantes, mutantes_mortos):
    """Calcula o mutation score"""
    if total_mutantes == 0:
        return 0.0
    return (mutantes_mortos / total_mutantes) * 100
