import pytest
from src.str_converter import StringConverter


class TestStrConverter(object):
    def test_str_input_to_int(self):
        with pytest.raises(ValueError):
            strc = StringConverter('a')
            strc.to_int()

    def test_int_input_to_int(self):
        strc = StringConverter(1)
        actual = strc.to_int()
        expected = 1
        assert actual == expected, f'Actual: {actual}, Expected: {expected}'

    # since to_str() is not there in StringConverter, we specify that this test may fail so ignore
    @pytest.mark.xfail(reason="StringConverter.to_str() method is not yet written")
    def test_str_input_to_str(self):
        strc = StringConverter(1)
        actual = strc.to_str()  # we haven't written to_str() in StringConverter yet.
        expected = "1"
        assert actual == expected, f'Actual: {actual}, Expected: {expected}'


