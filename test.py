import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return -2*x**6 - 1.5*x**4 - 10*x + 2

def df(x):
    return -12*x**5 - 6*x**3 - 10

def plot_function():
    x = np.linspace(-3, 3, 400)
    y = f(x)
    plt.plot(x, y, label='f(x)')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid()
    plt.title("Graphical Method for Root Finding")
    plt.legend()
    plt.show()

def error_approx(new, old):
    return abs((new - old) / new) * 100 if new != 0 else 0

def bisection_method(a, b, tol=1e-6):
    print("\nBisection Method:")
    iter_count = 0
    old_c = a
    while abs(b - a) > tol:
        c = (a + b) / 2
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
    return (a + b) / 2

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

def newton_raphson_method(x0, tol=1e-6):
    print("\nNewton-Raphson Method:")
    iter_count = 0
    old_x = x0
    while abs(f(x0)) > tol:
        x_new = x0 - f(x0) / df(x0)
        err = error_approx(x_new, old_x)
        print(f"Iteration {iter_count}: x = {x0:.4f}, f(x) = {f(x0):.4f}, df(x) = {df(x0):.4f}, x_new = {x_new:.4f}, Error = {err:.4f}%")
        if err < 5:
            return x_new
        old_x = x0
        x0 = x_new
        iter_count += 1
    return x0

def secant_method(x0, x1, tol=1e-6):
    print("\nSecant Method:")
    iter_count = 0
    while abs(f(x1)) > tol:
        x_new = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        err = error_approx(x_new, x1)
        print(f"Iteration {iter_count}: x0 = {x0:.4f}, x1 = {x1:.4f}, x_new = {x_new:.4f}, f(x_new) = {f(x_new):.4f}, Error = {err:.4f}%")
        if err < 5:
            return x_new
        x0, x1 = x1, x_new
        iter_count += 1
    return x1

# Example usage
if __name__ == "__main__":
    plot_function()

    root_bisection = bisection_method(0, 1)
    root_regula_falsi = regula_falsi_method(0, 1)
    root_newton = newton_raphson_method(1)
    root_secant = secant_method(0, 1)

    print(f"\nBisection Method Root: {root_bisection:.4f}")
    print(f"Regula Falsi Root: {root_regula_falsi:.4f}")
    print(f"Newton-Raphson Method Root: {root_newton:.4f}")
    print(f"Secant Method Root: {root_secant:.4f}")
