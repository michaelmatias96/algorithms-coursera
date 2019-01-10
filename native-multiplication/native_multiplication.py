def multiply(x, y):
    num_digits = len(str(x))

    x_H = x / 10 ** (num_digits / 2)
    x_L = x % 10 ** (num_digits / 2)

    y_H = y / 10 ** (num_digits / 2)
    y_L = y % 10 ** (num_digits / 2)

    product = (x_H * y_H * 10 ** num_digits) + (x_H * y_L + x_L * y_H) * 10 ** (num_digits / 2) + x_L * y_L
    return product


if __name__ == '__main__':
    print(multiply(3141592653589793238462643383279502884197169399375105820974944592,
                   2718281828459045235360287471352662497757247093699959574966967627))
