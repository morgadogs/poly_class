import json

class Polynomial:
    """
    The initialization receives a dict where the keys are non negative degrees and the values are the coefficients.
    """
    def __init__ (self, coef_at_degree):
        self.coef_at_degree = coef_at_degree

    """
    Evaluates the value of the polynomial at a given x.
    """
    def eval (self, x):
        value_at_x = 0
        for degree in self.coef_at_degree:
            value_at_x += self.coef_at_degree[degree] * x ** degree
        return value_at_x
    
    """
    Returns the polynomial corresponding to the symbolic integral of self.
    The parameter constant can be used to set the coefficient at degree zero.
    """
    def symbolic_integrate (self, constant = 0):
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
    def symbolic_derivative (self):
        deriv_coef_at_degree = {}
        for degree in self.coef_at_degree:
            if degree > 0:
                deriv_coef_at_degree[degree - 1] = degree * self.coef_at_degree[degree]
        return Polynomial(deriv_coef_at_degree)
    
    """
    Save polynomial as json file.
    """
    def save_as_json (self, filename):
        json.dump(self.coef_at_degree, open(f"data/{filename}", "w"))