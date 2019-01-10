def multiply(x, y):
    num_digits = len(str(x))

    if num_digits == 1:
        return x * y

    a = x / (10 ** (num_digits / 2))
    b = x % (10 ** (num_digits / 2))

    c = y / (10 ** (num_digits / 2))
    d = y % (10 ** (num_digits / 2))

    ac = multiply(a, c)
    ad = multiply(a, d)
    bc = multiply(b, c)
    bd = multiply(b, d)

    product = ac * 10 ** num_digits + (ad + bc) * 10 ** (num_digits / 2) + bd
    return product


if __name__ == '__main__':
    print(multiply(20, 19))
