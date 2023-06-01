from poly import Polynomial

p = Polynomial({
    0: 1,
    1:-1,
    2:3}
    )

print(p.eval(0))

p.save_as_json()