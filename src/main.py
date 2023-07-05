from poly import Polynomial

p = Polynomial({
    0: 1,
    1:-1,
    2:3}
    )

print(p.eval(0))

p.save_as_json("poly.json")

q = Polynomial({
    0: 3,
    1: 5,
    3: -9,
    5: -1})

print(q.bisection_method([-300,1000], 50))

