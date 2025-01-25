class PolynomialA2:
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
        factorial_number = self.factorial(r_value)
        for i in range(2, self.n + 1):
            if factorial_number % (self.p ** i) != 0:
                return i - 1
        return self.n

    def s_p(self, m: int) -> int:
        if m == 1:
            return 1
        for i in range(m * self.p + 1):
            if self.find_mod(i) >= m:
                return i - 1
            
    def evaluate_internal_sum(self, t: int, i: int, t_n: int, a: int) -> int:
        res = 0
        for j in range(t+1, t_n):
            res += a[j] * (t - i)**j
        return res

    def evaluate_sum(self, t: int, t_n: int, a: list) -> int:
        result = 0
        for i in range(t+1):
            result += (-1)**i * (self.factorial(t) // 
            (self.factorial(i) * self.factorial(t - i))) * (self.function[t-i] -
            self.evaluate_internal_sum(t, i, t_n, a))
        return result % (self.p ** self.n)

    def find_solution(self, d: int, t: int):
        for i in range(self.p ** self.n):
            if (self.factorial(t) * i) % (self.p ** self.n) == d:
                return i
        return -1

    def check_sum(self, s_p: int, a: int, b: int) -> int:
        res = 0
        for s in range(1, s_p + 1):
            res += a[s] * b**s
        return res 

    def check_polynomial(self) -> bool:
        if self.n == 1:
            return True
        s_p = self.s_p(self.n)
        t_list = [i for i in range(s_p, 0, -1)]
        d_list = [0] * (len(t_list) + 1)
        a_list = [0] * (len(t_list) + 1)
        t_n = t_list[0] + 1
        for t in t_list:
            d_list[t] = self.evaluate_sum(t, t_n, a_list)        
            a_list[t] = self.find_solution(d_list[t], t)
            if a_list[t] == -1:
                return False
        for b in range(self.p ** self.n):
            if ((self.function[b] - 
                self.check_sum(t_list[0], a_list, b)) % 
                (self.p ** self.n)) != self.function[0]:
                return False
        a_list[0] = self.function[0]
        return (True, a_list)
polynomial = PolynomialA2(2, 2, [0, 2, 2, 2])
print(polynomial.check_polynomial())
