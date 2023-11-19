class Polynomial:
    def __init__(self, expression):
        self.expression = expression

    def differentiate(self):
        terms = self.expression.split("+")

        derivative_terms = []
        for term in terms:
            if "x" not in term:
                derivative_terms.append("0")
            elif "*" in term: # Handle cases like '2 * x'
                coefficient, variable = term.split("*")
                derivative_terms.append(str(int(coefficient) * int(variable.split("^")[1])))
            else:
                power = term.split("^")[1]
                coefficient = power.split("x")[0]
                new_power = str(int(power) - 1)
                derivative_terms.append(coefficient + "x^" + new_power)

            derivative = "+".join(derivative_terms)
            return derivative

expression = input("Enter a polynomial in standard algebraic notation:")

polynomial = Polynomial(expression)

derivative = polynomial.differentiate()

print(derivative)