def decimal_to_binary(number):
    arr = []
    while number >= 1:
        if number / 2 == 1:
            arr.insert(0, 0)
            arr.insert(0, 1)
            break

        if number / 2 == 0.5:
            arr.insert(0, 1)
            break

        bit = number % 2
        arr.insert(0, bit)
        number = number // 2

    result = "".join(map(str, arr))
    return result
