# python3

"""
Solve the k-Universal Circular String Problem.
     Input: An integer k.
     Output: A k-universal circular string.
Sample Input:
4
Sample Output:
0000110010111101
"""


def de_bruijn(k, n):
    alphabet = list(map(str, range(k)))
    a = [0] * k * n
    sequence = []

    def db(t, p):
        if t > n:
            if n % p == 0:
                sequence.extend(a[1:p + 1])
        else:
            a[t] = a[t - p]
            db(t + 1, p)
            for j in range(a[t - p] + 1, k):
                a[t] = j
                db(t + 1, t)

    db(1, 1)
    return "".join(alphabet[i] for i in sequence)


if __name__ == "__main__":
    print(de_bruijn(2, int(input())))
