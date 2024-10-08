import pytest 
from src.prueba1 import mayor

@pytest.mark.parametrize(
    "input_x, input_y, expected",
    [
        (0, 0, 0),
        (-1, 1, 1),
        (55, 5, 55),
        (0,2,2)
    ]
)
def test_prueba1_params(input_x, input_y, expected):
    assert mayor(input_x, input_y) == expected