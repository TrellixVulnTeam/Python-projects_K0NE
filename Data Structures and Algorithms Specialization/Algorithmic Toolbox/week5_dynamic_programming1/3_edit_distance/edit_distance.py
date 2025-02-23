# Uses python3
def edit_distance(s, t):
    n, m = len(s), len(t)

    d = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        d[i][0] = i
    for i in range(m + 1):
        d[0][i] = i

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            insertion = d[i][j - 1] + 1
            deletion = d[i - 1][j] + 1
            match = d[i - 1][j - 1]
            mismatch = d[i - 1][j - 1] + 1
            if s[i - 1] == t[j - 1]:
                d[i][j] = min([insertion, deletion, match])
            else:
                d[i][j] = min([insertion, deletion, mismatch])

    return d[n][m]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
