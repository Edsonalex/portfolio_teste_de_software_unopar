"""
logica_de_teste.py
Define as funções de teste que serão executadas
"""

import unittest
import io
from unittest.mock import patch
from maximo import maximo
from casos_de_teste_maximo import CASOS_TESTE_BASICOS, CASOS_TESTE_VALIDACAO, TODOS_OS_CASOS

class TestMaximoBasicos(unittest.TestCase):
    """Testes dos casos básicos (lógica com print)"""
    
    def test_casos_basicos(self):
        """Executa todos os casos de teste básicos"""
        for caso in CASOS_TESTE_BASICOS:
            with self.subTest(caso=caso["id"], nome=caso["nome"]):
                with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                    maximo(caso["a"], caso["b"])
                    resultado = mock_stdout.getvalue().strip()
                    self.assertEqual(resultado, caso["esperado"])


class TestMaximoValidacao(unittest.TestCase):
    """Testes de validação TDD (rejeição de tipos inválidos)"""
    
    def test_casos_validacao(self):
        """Executa todos os casos de validação TDD"""
        for caso in CASOS_TESTE_VALIDACAO:
            with self.subTest(caso=caso["id"], nome=caso["nome"]):
                with self.assertRaises(caso["deve_lancar"]) as context:
                    maximo(caso["a"], caso["b"])
                
                mensagem_erro = str(context.exception)
                for texto_esperado in caso["msg_contem"]:
                    self.assertIn(texto_esperado, mensagem_erro)
