CASOS_TESTE_BASICOS = [
    {"id": "CT-01", "nome": "a_maior_que_b", "a": 20, "b": 10, "esperado": "O numero 20 é o maior"},
    {"id": "CT-02", "nome": "a_menor_que_b", "a": 10, "b": 20, "esperado": "O numero 20 é o maior"},
    {"id": "CT-03", "nome": "valores_iguais", "a": 15, "b": 15, "esperado": "Os numeros são iguais e o valor é 15"},
    {"id": "CT-04", "nome": "a_maior_negativos", "a": -5, "b": -10, "esperado": "O numero -5 é o maior"},
    {"id": "CT-05", "nome": "a_menor_negativos", "a": -20, "b": -8, "esperado": "O numero -8 é o maior"},
    {"id": "CT-06", "nome": "positivo_vs_negativo", "a": 10, "b": -5, "esperado": "O numero 10 é o maior"},
    {"id": "CT-07", "nome": "negativo_vs_positivo", "a": -3, "b": 7, "esperado": "O numero 7 é o maior"},
    {"id": "CT-08", "nome": "zero_vs_negativo", "a": 0, "b": -5, "esperado": "O numero 0 é o maior"},
]

CASOS_TESTE_VALIDACAO = [
    {"id": "CT-09", "nome": "rejeita_string_a", "a": "dez", "b": 20, "deve_lancar": TypeError, "msg_contem": ["deve ser número inteiro", "str"]},
    {"id": "CT-10", "nome": "rejeita_string_b", "a": 20, "b": "dez", "deve_lancar": TypeError, "msg_contem": ["deve ser número inteiro", "str"]},
    {"id": "CT-11", "nome": "rejeita_strings_ambos", "a": "quinze", "b": "quinze", "deve_lancar": TypeError, "msg_contem": ["deve ser número inteiro"]},
    {"id": "CT-12", "nome": "rejeita_float_a", "a": 5.5, "b": 15, "deve_lancar": TypeError, "msg_contem": ["deve ser número inteiro", "float"]},
    {"id": "CT-13", "nome": "rejeita_float_b", "a": -20, "b": -8.3, "deve_lancar": TypeError, "msg_contem": ["deve ser número inteiro", "float"]},
    {"id": "CT-14", "nome": "rejeita_float_ambos", "a": 10.4, "b": -5.9, "deve_lancar": TypeError, "msg_contem": ["deve ser número inteiro"]},
    {"id": "CT-15", "nome": "rejeita_boolean_a", "a": True, "b": 10, "deve_lancar": TypeError, "msg_contem": ["deve ser número inteiro", "bool"]},
    {"id": "CT-16", "nome": "rejeita_boolean_b", "a": 10, "b": False, "deve_lancar": TypeError, "msg_contem": ["deve ser número inteiro", "bool"]},
    {"id": "CT-17", "nome": "rejeita_none_a", "a": None, "b": 10, "deve_lancar": TypeError, "msg_contem": ["deve ser número inteiro", "NoneType"]},
    {"id": "CT-18", "nome": "rejeita_none_b", "a": 10, "b": None, "deve_lancar": TypeError, "msg_contem": ["deve ser número inteiro", "NoneType"]},
    {"id": "CT-19", "nome": "rejeita_lista_a", "a": [10], "b": 20, "deve_lancar": TypeError, "msg_contem": ["deve ser número inteiro", "list"]},
    {"id": "CT-20", "nome": "rejeita_lista_b", "a": 10, "b": [20], "deve_lancar": TypeError, "msg_contem": ["deve ser número inteiro", "list"]},
    {"id": "CT-21", "nome": "rejeita_dict_a", "a": {"num": 10}, "b": 20, "deve_lancar": TypeError, "msg_contem": ["deve ser número inteiro", "dict"]},
    {"id": "CT-22", "nome": "rejeita_dict_b", "a": 10, "b": {"num": 20}, "deve_lancar": TypeError, "msg_contem": ["deve ser número inteiro", "dict"]},
]

TODOS_OS_CASOS = CASOS_TESTE_BASICOS + CASOS_TESTE_VALIDACAO
