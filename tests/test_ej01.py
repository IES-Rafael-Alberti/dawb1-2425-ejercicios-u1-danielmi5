import pytest 
from src.ej01_def import saludo

@pytest.mark.parametrize(
    "nombre",
    [
        (1),
        ("Daniel"),
        ("San")
    ]
)
def test_ej01_params(nombre):
    assert nombre == str(nombre)