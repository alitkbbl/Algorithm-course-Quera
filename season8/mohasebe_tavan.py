def power(base, exp):
    if exp == 0:
        return 1.0

    half = power(base, exp // 2)

    if exp % 2 == 0:
        return half * half
    else:
        return half * half * base


base = float(input())
exp = int(input())

result = power(base, exp)

print(f"{result:.3f}")
