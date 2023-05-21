def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(c):
    return c(lambda a, b : a)

def cdr(c):
    return c(lambda a, b : b)

c = cons(2, 5)
print(car(c))
print(cdr(c))
