import pytest 
from src.ej01_def import saludo

@pytest.mark.parametrize(
    "nombre",
    [
        ("Alejandro"),
        ("Daniel"),
        ("San")
    ]
)
def test_ej01_params(nombre):
    assert nombre == str(nombre)