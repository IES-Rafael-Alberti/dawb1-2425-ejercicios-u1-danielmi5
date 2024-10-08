import pytest 
from src.ej02_def import importe_total

@pytest.mark.parametrize(
    "horas, coste, importe",
    [
        (2, 10, 20),
        (10, 30, 300),
        (5, 5, 25)
    ]
)
def test_importe_total_params(horas, coste, importe):
    assert importe_total(horas, coste) == importe
