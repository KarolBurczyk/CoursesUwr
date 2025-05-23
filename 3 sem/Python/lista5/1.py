class DerivativeError(Exception):
    "Raised when there are too many variables in the expression"
    pass

class VariableNotFoundException(Exception):
    "Raised when variable is not found in the given dictionary"
    pass

class DivByZero(Exception):
    "Raised when trying to divide by 0"
    pass

class Exp:
    def __init__(self):
        pass
    def calc(self, vars):
        pass
    def __str__(self):
        pass
    def __add__(self, e1, e2):
        return Add(e1, e2)
    def __mul__(self, e1, e2):
        return Mult(e1, e2)
    def derivative(self):
        pass
    # method counting how many variables are in an Expression
    def var_count(self):
        pass

class Add(Exp):
    def __init__(self, e1, e2):
        self.exp1 = e1
        self.exp2 = e2
    def calc(self, vars):
        return self.exp1.calc(vars) + self.exp2.calc(vars)
    def __str__(self):
        return "Add(" + str(self.exp1.__str__()) + ", " + str(self.exp2.__str__()) + ")"
    def derivative(self):
        if len(set(self.exp1.var_count() + self.exp2.var_count())) <= 1:
            return Add(self.exp1.derivative(), self.exp2.derivative())
        else:
            raise DerivativeError("Too many variables in the expression")
    def var_count(self):
        return self.exp1.var_count() + self.exp2.var_count()

class Sub(Exp):
    def __init__(self, e1, e2):
        self.exp1 = e1
        self.exp2 = e2
    def calc(self, vars):
        return self.exp1.calc(vars) - self.exp2.calc(vars)
    def __str__(self):
        return "Sub(" + str(self.exp1.__str__()) + ", " + str(self.exp2.__str__()) + ")"
    def derivative(self):
        if len(set(self.exp1.var_count() + self.exp2.var_count())) <= 1:
            return Sub(self.exp1.derivative(), self.exp2.derivative())
        else:
            raise DerivativeError("Too many variables in the expression")
    def var_count(self):
        return self.exp1.var_count() + self.exp2.var_count()

class Mult(Exp):
    def __init__(self, e1, e2):
        self.exp1 = e1
        self.exp2 = e2
    def calc(self, vars):
        return self.exp1.calc(vars) * self.exp2.calc(vars)
    def __str__(self):
        return "Mult(" + str(self.exp1.__str__()) + ", " + str(self.exp2.__str__()) + ")"
    def derivative(self):
        if len(set(self.exp1.var_count() + self.exp2.var_count())) <= 1:
            return Mult(self.exp1.derivative(), self.exp2.derivative())
        else:
            raise DerivativeError("Too many variables in the expression")
    def var_count(self):
        return self.exp1.var_count() + self.exp2.var_count()

class Div(Exp):
    def __init__(self, e1, e2):
        self.exp1 = e1
        self.exp2 = e2
    def calc(self, vars):
        try: 
            self.exp1.calc(vars) / self.exp2.calc(vars)
        except DivByZero:
            print("You can't divide by zero")
    def __str__(self):
        return "Div(" + str(self.exp1.__str__()) + ", " + str(self.exp2.__str__()) + ")"
    def derivative(self):
        if len(set(self.exp1.var_count() + self.exp2.var_count())) <= 1:
            return Div(self.exp1.derivative(), self.exp2.derivative())
        else:
            raise DerivativeError("Too many variables in the expression")
    def var_count(self):
        return self.exp1.var_count() + self.exp2.var_count()

class Const(Exp):
    def __init__(self, c):
        try:
            self.value = float(c)
        except TypeError:
            print("Const has to be a number")
    def calc(self, vars):
        return self.value
    def __str__(self):
        return "Const(" + str(self.value) + ")"
    def derivative(self):
        return Const(0)
    def var_count(self):
        return []

class Var(Exp):
    def __init__(self, c):
        self.value = str(c)
    def calc(self, vars):
        try:
            return vars[self.value]
        except VariableNotFoundException:
            print("Unable to find the value of the variable in the dictionary")
        
    def __str__(self):
        return 'Var("' + self.value + '")'
    def derivative(self):
        return Const(1)
    def var_count(self):
        return [self.value]

dic = {
    "x" : 2,
    "y" : 1
}

exp1 = Mult(Add(Const(8), Var('y')), Div(Const(1), Const(1)))
print(exp1.derivative())
print(exp1.__str__())

exp2 = Exp().__add__(Const('1'), Var('x'))
print(exp2.__str__())
print(exp2.derivative())

# exp3 = Div(Const(1), Const(0))
# print(exp3.calc(dic))
# (8 + y)*(1 / 1)
# y
# (0 + 1)*(1 / 0)