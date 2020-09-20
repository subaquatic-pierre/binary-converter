from decimal_to_binary import decimal_to_binary
from binary_to_decimal import binary_to_decimal


def test_decimal_to_binary_1():
    result = decimal_to_binary(40)
    assert result == "101000"


def test_decimal_to_binary_2():
    result = decimal_to_binary(4003)
    assert result == "111110100011"


def test_decimal_to_binary_3():
    result = decimal_to_binary(6358)
    assert result == "1100011010110"


def test_binary_to_decimal_1():
    result = binary_to_decimal("101000")
    assert result == 40


def test_binary_to_decimal_2():
    result = binary_to_decimal("111110100011")
    assert result == 4003


def test_binary_to_decimal_3():
    result = binary_to_decimal("1100011010110")
    assert result == 6358


if __name__ == "__main__":
    test_decimal_to_binary_1()
    test_decimal_to_binary_2()
