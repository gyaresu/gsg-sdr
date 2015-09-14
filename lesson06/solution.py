from cmath import pi, e, log
tau = 2 * pi
def average(readings):
    base = e ** (1j * tau / 360)
    total = 0
    for r in readings:
        total += r[1] * base ** r[0]
    result = total / len(readings)
    return (log(result, base).real, abs(result))

print average(((12,1), (15,1), (13, 1), (9, 1), (16, 1)))