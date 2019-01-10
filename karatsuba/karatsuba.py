from math import floor


def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    num_digits = len(str(x))

    x_H = x / 10**(num_digits/2)
    x_L = x % (10 ** (num_digits / 2))

    y_H = y / 10**(num_digits/2)
    y_L = y % (10 ** (num_digits / 2))

    a = karatsuba(x_H, y_H)
    d = karatsuba(x_L, y_L)
    e = karatsuba((x_H + x_L), (y_H + y_L)) - a - d

    return a * 10**num_digits + e * 10**(num_digits/2) + d


if __name__ == '__main__':
    print(karatsuba(3141592653589793238462643383279502884197169399375105820974944592,
                    2718281828459045235360287471352662497757247093699959574966967627))
