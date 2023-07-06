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
    5: 1})

poly3 = Polynomial({
    0: 4,
    1: 4,
    3: -8,
    5: -2,
    6: 2})

poly4 = Polynomial()

# Results for polynomial roots were checked using WolframAlpha.

# Test for the Polynomial poly1.

poly1.save_as_json("poly1.json")

print(poly1.eval(0), poly1.eval(1), poly1.eval(-1), poly1.eval(1.5))

print(poly1.symbolic_integrate().coef_at_degree, poly1.symbolic_integrate(2.0).coef_at_degree)

print(poly1.interval_integrate([1,3]), poly1.interval_integrate((-1.0, 0)), poly1.interval_integrate((0, -1.0)))

print(poly1.symbolic_derivative().coef_at_degree)

# poly1 has no real roots and (poly1)' has only the root 1/6.

print(poly1.newton_method(1/6), poly1.newton_method(3.5, max_iterations=1e5), poly1.newton_method(-90, max_iterations=1e5, epsilon=0.1))

print(poly1.bisection_method((-100, 100)), poly1.bisection_method([-20,10], max_iterations=1e3, epsilon=0.1))

# Test for the Polynomial poly2.

poly2.save_as_json("poly2.json")

print(poly2.eval(0), poly2.eval(1), poly2.eval(-3), poly2.eval(0.25))

print(poly2.symbolic_integrate().coef_at_degree, poly2.symbolic_integrate(-1).coef_at_degree)

print(poly2.interval_integrate([1,5]), poly2.interval_integrate((-1.0, 0)), poly2.interval_integrate((0, -1.0)))

print(poly2.symbolic_derivative().coef_at_degree)

# poly2 has three real roots: -1, approximately -2.8756 and approximately 2.9214. The complex roots are approximately 0.47712 +- 0.35982i.
# (poly2)' has four real roots: approximately +-0.43819 and approximately +-2.2821.