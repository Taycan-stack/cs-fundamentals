import pytest
from calculator import square

def test_str():
    with pytest.raises(TypeError):
        square("cat")