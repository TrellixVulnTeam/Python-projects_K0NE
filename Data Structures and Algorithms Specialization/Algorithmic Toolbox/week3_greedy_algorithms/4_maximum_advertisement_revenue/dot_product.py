# Uses python3

import sys


def max_dot_product(a, b):
    res = 0
    a.sort(reverse=True)
    b.sort(reverse=True)
    for i in range(len(a)):
        res += a[i] * b[i]
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
