def decimal_to_binary(number):
    arr = []
    while number > 1:
        bit = number % 2
        arr.insert(0, bit)
        if number / 2 == 0.5:
            arr.insert(0, 1)
            break
        elif number / 2 == 1:
            arr.insert(0, 0)
            arr.insert(0, 1)
            break
        else:
            number = number // 2

    result = "".join(map(str, arr))
    return result


def test_decimal_to_binary():
    result = decimal_to_binary(40)
    assert result == "101000"


if __name__ == "__main__":
    test_decimal_to_binary()
