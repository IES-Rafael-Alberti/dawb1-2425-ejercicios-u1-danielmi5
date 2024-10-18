import pytest 
from src.ej05_def import calcula_IVA
# Diferencia con la imagen de docs: Código modificado para que funcione con el codigo original (ej05_def.py)

@pytest.mark.parametrize(
    "precio_sin_IVA, tipo_IVA, precio_con_IVA",
    [
        (5, 21, 5*1.21 ),
        (50, 77, 50*1.77), 
        (234, 50, 234*1.5)
    ]
)
def test_calcula_IVA_params(precio_sin_IVA, tipo_IVA, precio_con_IVA):
    assert calcula_IVA(precio_sin_IVA, tipo_IVA) == precio_con_IVA
