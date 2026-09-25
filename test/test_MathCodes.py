import numpy as np

# ============= Teste Adição e Subtração =============
from MathCodes import Soma, Subtracao


def test_adicao_de_vetores():
    operacao = Soma(2, -3, 1, -1)

    x, y = operacao.VetoresNumpy()
    resultado = operacao.Calcular_VetoresNumpy(x, y)

    esperado = np.array([3, -4])

    np.testing.assert_array_equal(resultado, esperado)


def test_subtracao_de_vetores():
    operacao = Subtracao(2, -3, 1, -1)

    x, y = operacao.VetoresNumpy()
    resultado = operacao.Calcular_VetoresNumpy(x, y)

    esperado = np.array([1, -2])

    np.testing.assert_array_equal(resultado, esperado)
