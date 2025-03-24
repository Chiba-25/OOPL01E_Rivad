import numpy as np

def f(x):
    return -2*x**6 - 1.5*x**4 - 10*x + 2

def error_approx(new, old):
    return abs((new - old) / new) * 100 if new != 0 else 0

def regula_falsi_method(a, b, tol=1e-6):
    print("\nRegula Falsi Method:")
    iter_count = 0
    old_c = a

    while abs(f(a) - f(b)) > tol:
        c = b - (f(b) * (b - a)) / (f(b) - f(a))
        err = error_approx(c, old_c)

        print(f"Iteration {iter_count}: x_l = {a:.4f}, x_u = {b:.4f}, x_r = {c:.4f}, f(x_r) = {f(c):.4f}, Error = {err:.4f}%")

        if err < 5:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

        old_c = c
        iter_count += 1

    return c

# Example usage
if __name__ == "__main__":
    root_regula_falsi = regula_falsi_method(0, 1)
    print(f"\nRegula Falsi Root: {root_regula_falsi:.4f}")
