def binary_to_decimal(binary: str) -> int:
    bits = list(binary)
    bits.reverse()
    results = []
    for i in range(len(bits)):
        if int(bits[i]) == 1:
            results.append(1 * (2 ** i))

    result = sum(results)
    return result
