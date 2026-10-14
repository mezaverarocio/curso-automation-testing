import pytest

from calculadora import sumar, restar, multiplicar, dividir

@pytest.fixture
def numeros_decimales():
    return 0.1, 0.2

@pytest.fixture
def numeros_enteros():
    return 20, 5

@pytest.mark.smoke   
def test_sumar_positivos():
    assert sumar(2, 3) == 5
@pytest.mark.smoke
def test_sumar_error():
    with pytest.raises(TypeError):
        sumar(2, "3")
@pytest.mark.smoke
def test_sumar_enteros(numeros_enteros):
    a, b = numeros_enteros
    assert sumar(a, b) == 25 
@pytest.mark.smoke
def test_sumar_decimales(numeros_decimales):
    a, b = numeros_decimales
    assert sumar(a, b) == pytest.approx(0.3)

def test_restar_positivos():
    assert restar(5, 3) == 2
def test_restar_error():
    with pytest.raises(TypeError):
        restar(5, "3")

def test_multiplicar_positivos():
    assert multiplicar(4, 3) == 12
def test_multiplicar_error():
    with pytest.raises(TypeError):
        multiplicar(4, "3")

def test_dividir_positivos():
    assert dividir(10, 2) == 5
@pytest.mark.exception
def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)
@pytest.mark.exception
def test_dividir_error():
    with pytest.raises(TypeError):
        dividir(10, "2")
def test_dividir_enteros(numeros_enteros):
    a, b = numeros_enteros
    assert dividir(a, b) == 4

@pytest.mark.smoke
@pytest.mark.parametrize("a, b, resultado",
                            [(1, 2, 3), 
                            (5, 5, 10), 
                            (10, 15, 25)
                            ]
                        )
def test_sumar_parametrizado(a, b, resultado):
    assert sumar(a, b) == resultado

@pytest.mark.parametrize("a, b, resultado",
                            [(10, 5, 5),
                            (20, 10, 10),
                            (15, 5, 10)
                            ]
                        )
def test_restar_parametrizado(a, b, resultado):
    assert restar(a, b) == resultado