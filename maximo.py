"""
maximo.py
Função a ser testada
"""

def maximo(a, b):
  
    # Validação de tipo para 'a'
    if not isinstance(a, int) or isinstance(a, bool):
        raise TypeError(
            f"O parâmetro 'a' deve ser número inteiro, "
            f"não {type(a).__name__}"
        )
    
    # Validação de tipo para 'b'
    if not isinstance(b, int) or isinstance(b, bool):
        raise TypeError(
            f"O parâmetro 'b' deve ser número inteiro, "
            f"não {type(b).__name__}"
        )
    
    # Lógica principal
    if a > b:
        return print(f"O numero {a} é o maior")
    elif a == b:
        return print(f"Os numeros são iguais e o valor é {a}")
    else:
        return print(f"O numero {b} é o maior")
