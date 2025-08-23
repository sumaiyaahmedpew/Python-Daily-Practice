# problem_27 Polynomial Calculator
import numpy as np

def pretty_print(poly):
    terms = []
    degree = len(poly) - 1
    for i, coeff in enumerate(poly):
        power = degree - i
        if coeff == 0:
            continue
        if power == 0:
            terms.append(str(coeff))
        elif power == 1:
            terms.append(f"{coeff}x")
        else:
            terms.append(f"{coeff}x^{power}")
    return " + ".join(terms)

def poly_add(p1, p2):
    return np.polyadd(p1, p2)

def poly_sub(p1, p2):
    return np.polysub(p1, p2)

def poly_mul(p1, p2):
    return np.polymul(p1, p2)

p1 = np.array([3, 2, 1])  
p2 = np.array([1, 4])  

print("P1 =", pretty_print(p1))
print("P2 =", pretty_print(p2))

print("\nP1 + P2 =", pretty_print(poly_add(p1, p2)))
print("P1 - P2 =", pretty_print(poly_sub(p1, p2)))
print("P1 * P2 =", pretty_print(poly_mul(p1, p2)))
