# Hk
def hk(k, xs):
    return xs[k] - xs[k - 1]

# Lambda
def lf(k, xs):
    if k == 0:
        return 0
    return hk(k, xs) / (hk(k, xs) + hk(k + 1, xs))

# Iloraz roznicowy
def f(xs, ys):
    if len(xs) == 1:
        return ys[0]
    return (f(xs[1:], ys[1:]) - f(xs[:-1], ys[:-1])) / (xs[-1] - xs[0])

# Dk
def df(k, xs, ys):
    if k == 0:
        return 0
    return 6 * f(xs[(k - 1):(k + 2)], ys[(k - 1):(k + 2)])

# Moment
def m(xs, ys):
    n = len(xs) - 1

    q = [0 for _ in range(n)]                          
    u = [0 for _ in range(n)]
    l = [lf(k, xs) for k in range(n)]
    d = [df(k, xs, ys) for k in range(n)]

    for i in range(1, n):
        p = l[i] * q[i - 1] + 2
        q[i] = (l[i] - 1) / p
        u[i] = (d[i] - l[i] * u[i - 1]) / p

    m = [0 for _ in range(n + 1)]
    m[n - 1] = u[n - 1]

    for i in range(n - 2, 0, -1):
        m[i] = u[i] + q[i] * m[i + 1]

    return m

# Funkcja Sm
def sk(xs, ys, ms, k):
    return lambda x: \
        ((ms[k - 1] * (xs[k] - x) ** 3) / 6 + (ms[k] * (x - xs[k - 1]) ** 3) / 6 + \
        (ys[k - 1] - (ms[k - 1] * hk(k, xs) ** 2) / 6) * (xs[k] - x) + \
        (ys[k] - (ms[k] * hk(k, xs) ** 2) / 6) * (x - xs[k - 1])) / hk(k, xs)

# Zbior funkcji S
def get_s(xs, ys):
    ms = m(xs, ys)
    def res(x):
        for i in range(1, len(xs)):
            if xs[i - 1] <= x < xs[i]:
                return sk(xs, ys, ms, i)(x)

    return res 