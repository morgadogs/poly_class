import json

class Polynomial:
    """
    The initialization receives a dict where the keys are non-negative degrees and the
    values are the coefficients.
    """
    def __init__(self, coef_at_degree):
        self.coef_at_degree = coef_at_degree

    """
    Evaluates the value of the polynomial at a given x.
    """
    def eval(self, x):
        value_at_x = 0
        for degree in self.coef_at_degree:
            value_at_x += self.coef_at_degree[degree] * x ** degree
        return value_at_x
    
    """
    Returns the polynomial corresponding to the symbolic integral of self.
    The parameter constant can be used to set the coefficient at degree zero.
    """
    def symbolic_integrate(self, constant=0):
        int_coef_at_degree = {0: constant}
        for degree in self.coef_at_degree:
            int_coef_at_degree[degree + 1] = self.coef_at_degree[degree] / (degree + 1)
        return Polynomial(int_coef_at_degree)
    
    """
    Returns the value corresponding to the definite integral in an interval.
    Receives an interval as a tuple or a list of 2 numbers (int or float).
    """
    def interval_integrate(self, interval):
        integral = self.symbolic_integrate()
        a, b = interval
        return integral.eval(b) - integral.eval(a)

    """
    Returns the polynomial corresponding to the symbolic derivative of self.
    """
    def symbolic_derivative(self):
        deriv_coef_at_degree = {}
        for degree in self.coef_at_degree:
            if degree > 0:
                deriv_coef_at_degree[degree - 1] = degree * self.coef_at_degree[degree]
        return Polynomial(deriv_coef_at_degree)
    
    """
    Save polynomial as a JSON file.
    """
    def save_as_json(self, filename):
        json.dump(self.coef_at_degree, open(f"poly_class/data/{filename}", "w"))
    
    """
    Read a JSON file and receive its dictionary to create a Polynomial instance.
    """
    @classmethod
    def from_json(cls, filename):
    	coef_at_degree = json.load(open(f"poly_class/data/{filename}", "r"))
    	return cls(coef_at_degree)
    
    """
    Uses the Newton method to find a root given an initial value.
    Receives an initial value and optional parameters to set a maximum of
    iterations and the tolerance of error for the root.
    Default number of maximum iterations is 100, and error is 1e-6.
    Returns the root if it was found and None otherwise, printing "No root found".
    If there was a stationary point, prints in which value it occurred.
    """
    def newton_method(self, value, max_iterations=100, epsilon=1e-6):
        derivative_poly = self.symbolic_derivative()
        current = value
        next = current + 1
        count = 0
        while count < max_iterations and abs(current - next) >= epsilon:
            deriv_at_current = derivative_poly.eval(current)
            if abs(deriv_at_current) < epsilon:
                print(f"Stationary point at {current}.")
                break
            current, next = next, current - self.eval(current) / deriv_at_current
            if abs(self.eval(next)) < epsilon:
                return next
            count += 1
        print("No root found.")
    
    """
    Uses the bisection method to find a root given an interval.
    Receives an interval [a, b] as a tuple or list of two numbers (int or float) and
    optional parameters to set a maximum number of iterations and the tolerance of error for
    the root. Default max_iterations and epsilon are set as 1e4 and 1e-3, respectively.
    Checks if self.eval(a) and self.eval(b) have opposite signs.
    """
    def bisection_method(self, interval, max_iterations=1e4, epsilon=1e-3):
        a, b = interval
        if self.eval(a) * self.eval(b) > 0:
            print(f"Bisection method requires an interval in which the polynomial has opposite signs in its endpoints.")
            return None
        else:
            count = 0
            while count < max_iterations:
                mid = (a + b) / 2
                if abs(self.eval(mid)) < epsilon:
                    return mid
                elif self.eval(a) * self.eval(mid) < 0:
                    b = mid
                else:
                    a = mid
                count += 1
            print(f"No root found for the maximum number of iterations {max_iterations} and tolerance {epsilon}.")
