import pytest 
from src.ej04_def import convertir_temp
### Código modificado para que pueda funcionar el test recibiendo datos (sin input) --> Si en el código original se elimina el input, funcina el test.

@pytest.mark.parametrize(
    "farenheit, celsius",
    [
        (5, (5-32)/1.8),
        (50, (50-32)/1.8), 
        (234, (234-32)/1.8)
    ]
)
def test_convertir_params(farenheit, celsius):
    assert convertir_temp(farenheit) == ("{:.2f}".format(celsius) + " °C" + " (""{:.2f}".format(farenheit)+ " °F)")
