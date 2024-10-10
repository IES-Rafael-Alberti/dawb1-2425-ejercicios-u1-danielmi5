import pytest 
from src.ej11_def import calcula
# Código modificado (He quitado la conversión a str)

@pytest.mark.parametrize(
    "n, suma",
    [
        (5,((5*(5+1))/2)),
        (12,((12*(12+1))/2)), 
        (23, ((23*(23+1))/2))
    ]
)
def test_calcula_params(n, suma):
    assert calcula(n) == suma
