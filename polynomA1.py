class PolynomialA1:

    def __init__(self, prime_number: int, power: int, function: list[int])->None:
        self.p = prime_number
        self.n = power
        self.function = function

    def factorial(self, number: int) -> int:
        if number == 0 or number == 1:
            return 1
        else:
            return number * self.factorial(number - 1)

    def find_mod(self, r_value: int) -> int:
        if r_value < self.p:
            return 0
        factorial_number = self.factorial(r_value)
        for i in range(2, self.n + 1):
            if factorial_number % (self.p ** i) != 0:
                return i - 1
        return self.n

    def evaluate_sum(self, r_value: int) -> bool:
        sum_result = 0
        for s in range(0, r_value + 1):
            sum_result += (((-1)**(r_value - s))*(self.factorial(r_value) //
            (self.factorial(s)*self.factorial(r_value - s)))*self.function[s])
        return sum_result  

    def check_polynomial(self) -> bool:
        if self.n == 1:
            return True
        coefficients = []
        polynom = [0 for _ in range(self.p**self.n)]
        for r in range(self.p ** self.n):
            mod = self.find_mod(r)
            coefficients.append(self.evaluate_sum(r))
            if coefficients[r] % (self.p**mod) != 0:
                return False
            if (exp:=self.divide_by_mod(coefficients[r],(self.factorial(r)))):
                coefficients_polynom = self.calculate_coefficients(r-1)
                for i in range(self.p**self.n - 1, -1, -1):
                    polynom[i] += exp*coefficients_polynom[i]
        polynom = [elem % (self.p**self.n) for elem in polynom]
        polynom.reverse()
        return True, polynom
    
    def calculate_coefficients(self, n: int) -> list[int]:
        if n >= 0:
            coefficients = [1]
            for i in range(1, n + 1):
                coefficients.append(0)
                for j in range(i, 0, -1):
                    coefficients[j] = coefficients[j] - i * coefficients[j-1]
            coefficients.append(0)           
            return [0] * (self.p**self.n - len(coefficients)) + coefficients
        return [0] * (self.p**self.n - 1) + [1]

    def modular_division(self, a: int, b: int, m: int) -> int:
        if b == 0:
            raise ValueError("Divide by zero")
        inverse_b = pow(b, -1, m)
        if inverse_b is None:
            raise ValueError("Do not exist")
        result = (a * inverse_b) % m

        return result

    def divide_by_mod(self, delta: int, fact_j: int) -> int:
        while fact_j % self.p == 0:
            fact_j //= self.p
            delta //= self.p
        fact_j %= self.p**self.n
        delta %= self.p**self.n
       
        return self.modular_division(delta, fact_j, self.p ** self.n)

polynomial = PolynomialA1(2, 2, [3, 1, 3, 1])
print(polynomial.check_polynomial())
