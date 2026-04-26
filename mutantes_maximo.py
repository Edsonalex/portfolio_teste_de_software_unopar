"""
mutantes_maximo.py
Lista dos mutantes para análise (apenas casos básicos)
"""

def maximo_original(a, b):
    """Função original (sem validação para testes básicos)"""
    if a > b:
        return a
    else:
        return b

def mutante_01_operador_maior_igual(a, b):
    """ROR: > para >="""
    if a >= b:  # MUTAÇÃO
        return a
    else:
        return b

def mutante_02_operador_menor(a, b):
    """ROR: > para <"""
    if a < b:  # MUTAÇÃO
        return a
    else:
        return b

def mutante_03_operador_igual(a, b):
    """ROR: > para =="""
    if a == b:  # MUTAÇÃO
        return a
    else:
        return b

def mutante_04_retorna_b_no_if(a, b):
    """VDL: Retorna b em vez de a no if"""
    if a > b:
        return b  # MUTAÇÃO
    else:
        return b

def mutante_05_retorna_a_no_else(a, b):
    """VDL: Retorna a em vez de b no else"""
    if a > b:
        return a
    else:
        return a  # MUTAÇÃO

def mutante_06_remove_else(a, b):
    """SDL: Remove bloco else"""
    if a > b:
        return a
    # MUTAÇÃO: else removido

def mutante_07_inverte_retornos(a, b):
    """VDL: Inverte retornos"""
    if a > b:
        return b  # MUTAÇÃO
    else:
        return a  # MUTAÇÃO

MUTANTES = [
    {"id": 1, "nome": "ROR: > → >=", "funcao": mutante_01_operador_maior_igual, "tipo": "ROR"},
    {"id": 2, "nome": "ROR: > → <", "funcao": mutante_02_operador_menor, "tipo": "ROR"},
    {"id": 3, "nome": "ROR: > → ==", "funcao": mutante_03_operador_igual, "tipo": "ROR"},
    {"id": 4, "nome": "VDL: retorna b no if", "funcao": mutante_04_retorna_b_no_if, "tipo": "VDL"},
    {"id": 5, "nome": "VDL: retorna a no else", "funcao": mutante_05_retorna_a_no_else, "tipo": "VDL"},
    {"id": 6, "nome": "SDL: remove else", "funcao": mutante_06_remove_else, "tipo": "SDL"},
    {"id": 7, "nome": "VDL: inverte retornos", "funcao": mutante_07_inverte_retornos, "tipo": "VDL"},
]
