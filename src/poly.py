import json
import pathlib

class Polynomial:
    """
    The initialization receives a dictionary where the keys are non-negative degrees and
    the values are the coefficients.
    """
    def __init__(self, coef_at_degree={}):
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
    The interval parameter is specified as a tuple or a list of two numbers (int or float).
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
    Save polynomial as a JSON file in the data folder.
    The filename parameter specifies the name of the file.
    """
    def save_as_json(self, filename):
        # Create the data folder if it doesn't already exist.
        pathlib.Path('/data').mkdir(parents=True, exist_ok=True)
        json.dump(self.coef_at_degree, open(f"/data/{filename}", "w"))
    
    """
    Read a JSON file and use its corresponding dictionary to create a Polynomial instance.
    The filename parameter specifies the name of the file in the data folder.
    """
    @classmethod
    def from_json(cls, filename):
        # json module converts the keys into str, so we convert them back to int.
        str_coef_at_degree = json.load(open(f"/data/{filename}", "r"))
        coef_at_degree = {}
        for str_degree in str_coef_at_degree:
            degree = int(str_degree)
            coef_at_degree[degree] = str_coef_at_degree[str_degree]
        return cls(coef_at_degree)
    
    """
    Uses the Newton method to find a root given an initial value.
    The value parameter specifies the initial value.
    The optional parameters max_iterations and epsilon are used to set a maximum of
    iterations and the tolerance of error for the root, respectively.
    Returns a root if it was found and None otherwise.
    Prints information if a stationary point was encountered or no root was found.
    """
    def newton_method(self, value, max_iterations=100, epsilon=1e-3):
        derivative_poly = self.symbolic_derivative()
        previous = value - 1
        current = value
        count = 0
        while count <= max_iterations and abs(previous - current) >= epsilon:
            if abs(self.eval(current)) < epsilon:
                return current
            deriv_at_current = derivative_poly.eval(current)
            if abs(deriv_at_current) < epsilon:
                print(f"Stationary point at {current}.")
                break
            previous, current = current, current - self.eval(current) / deriv_at_current
            count += 1
        if abs(self.eval(current)) < epsilon: # Check if the last computed number is a root.
            return current
        print(f"No root found. Initial value: {value}. Iterations: {count}. Tolerance: {epsilon}.")
    
    """
    Uses the bisection method to find a root given an interval [a, b] in which
    self.eval(a) and self.eval(b) have opposite signs.
    The parameter interval [a, b] is specified as a tuple or list of two numbers
    (int or float).
    The optional parameters iterations and epsilon are used to set the number of
    iterations and the tolerance of error for the root, respectively.
    Returns a root if it was found and None otherwise.
    Prints information if the interval is invalid or if no root was found.
    """
    def bisection_method(self, interval, iterations=100, epsilon=1e-3):
        a, b = interval
        if self.eval(a) * self.eval(b) > 0:
            print(f"Bisection method requires an interval in which the polynomial has opposite signs in its endpoints. Interval: [{a}, {b}].")
            return None
        else:
            count = 0
            while count <= iterations:
                mid = (a + b) / 2
                if abs(self.eval(mid)) < epsilon:
                    return mid
                elif self.eval(a) * self.eval(mid) < 0:
                    b = mid
                else:
                    a = mid
                count += 1
            print(f"No root found. Interval: [{a}, {b}]. Iterations: {iterations}. Tolerance: {epsilon}.")
