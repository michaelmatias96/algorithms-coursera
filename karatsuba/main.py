def run_karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    size_numbers = max(len(str(x)), len(str(y)))
    half_size_numbers = size_numbers / 2

    a = x / 10 ** half_size_numbers
    b = x % 10 ** half_size_numbers
    c = y / 10 ** half_size_numbers
    d = y % 10 ** half_size_numbers

    ac = run_karatsuba(a, c)
    bd = run_karatsuba(b, d)

    ad_plus_bc = run_karatsuba(a + b, c + d) - ac - bd

    product = ac * 10 ** (2 * half_size_numbers) + (ad_plus_bc * 10 ** half_size_numbers) + bd

    return product


if __name__ == '__main__':
    product = run_karatsuba(3141592653589793238462643383279502884197169399375105820974944592,
                            2718281828459045235360287471352662497757247093699959574966967627)
    print(product)
