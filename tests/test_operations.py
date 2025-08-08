import pytest
from calculator import operations
from config import settings

@pytest.mark.skipif(settings.ENVIRONMENT != "test", reason="Sadece test ortamında çalışır.")
class TestCalculator:

    def test_add_success(self):
        assert operations.add(2, 3) == 5

    def test_add_fail(self):
        assert operations.add(2, 3) == 6  # fail test

    def test_subtract_success(self):
        assert operations.subtract(5, 3) == 2

    def test_subtract_fail(self):
        assert operations.subtract(5, 3) == 1

    def test_multiply_success(self):
        assert operations.multiply(4, 2) == 8

    def test_multiply_fail(self):
        assert operations.multiply(4, 2) == 10

    def test_divide_success(self):
        assert operations.divide(10, 2) == 5

    def test_divide_fail(self):
        assert operations.divide(10, 2) == 6

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Sıfıra bölme yapılamaz"):
            operations.divide(5, 0)

