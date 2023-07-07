from poly import Polynomial

# Create Polynomial instances to test the methods of the Polynomial class.

poly1 = Polynomial({
    0: 1,
    1: -1,
    2: 3.0}
    )

poly2 = Polynomial({
    0: -3,
    1: 5,
    3: -9,
    5: 1}
    )

# Results for polynomial roots were checked using WolframAlpha.

# Save the dictionaries corresponding to the polynomials as JSON files.

poly1.save_as_json("poly1.json")

poly2.save_as_json("poly2.json")

# Evaluate the polynomials at specific values.

print(poly1.eval(0), poly1.eval(1), poly1.eval(-1), poly1.eval(1.5))

print(poly2.eval(0), poly2.eval(1), poly2.eval(-3), poly2.eval(0.25))

# Compute the symbolic integral of the polynomials and the definite integral over an interval.

print(poly1.symbolic_integrate().coef_at_degree, poly1.symbolic_integrate(2.0).coef_at_degree)

print(poly2.symbolic_integrate().coef_at_degree, poly2.symbolic_integrate(-1).coef_at_degree)

print(poly1.interval_integrate([1,3]), poly1.interval_integrate((-1.0, 0)), poly1.interval_integrate((0, -1.0)))

print(poly2.interval_integrate([1,5]), poly2.interval_integrate((-1.0, 0)), poly2.interval_integrate((0, -1.0)))

# Compute the symbolic derivative of the polynomials.

print(poly1.symbolic_derivative().coef_at_degree)

print(poly2.symbolic_derivative().coef_at_degree)

# Compute the roots of the polynomials using Newton's method and the bisection method.
# Remember that Newton's method doesn't work if it reaches a stationary point that is not a root of the original polynomial.
# poly1 has no real roots.
# (poly1)' has one real root 1/6.
# poly2 has three real roots: -1, approximately -2.8756 and approximately 2.9214.
# (poly2)' has four real roots: approximately +-0.4382 and approximately +-2.2821.

print(poly1.newton_method(1/6), poly1.newton_method(3.5, max_iterations=1e5), poly1.newton_method(-90, max_iterations=1e5, epsilon=0.1))

print(poly1.bisection_method((-100, 100)), poly1.bisection_method([-20,10], iterations=1e3, epsilon=0.1))

print(poly2.newton_method(-2), poly2.newton_method(-2.5), poly2.newton_method(3), poly2.newton_method(0), poly2.newton_method(0.4382))

print(poly2.bisection_method([-2,-3]), poly2.bisection_method([2.8,3]), poly2.bisection_method([-1.1,-0.9], iterations=1e6, epsilon=1e-6), poly2.bisection_method([3,4]))

# Test if the save_as_json and from_json methods work correctly.

print((Polynomial.from_json("poly1.json")).coef_at_degree, (Polynomial.from_json("poly2.json")).coef_at_degree)
