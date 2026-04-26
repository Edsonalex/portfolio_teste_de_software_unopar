import unittest
import io
from unittest.mock import patch
from app import maximo


class TesteFuncaoMaximo(unittest.TestCase):

    def testa_a_maior_que_b(self):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            maximo(20, 10)
            self.assertEqual(mock_stdout.getvalue().strip(), "O numero 20 é o maior")

    def testa_a_menor_que_b(self):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            maximo(10, 20)
            self.assertEqual(mock_stdout.getvalue().strip(), "O numero 20 é o maior")

    def testa_a_igual_a_b(self):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            maximo(15, 15)
            self.assertEqual(mock_stdout.getvalue().strip(), "O numero b é o maior")


if __name__ == '__main__':
    unittest.main()
