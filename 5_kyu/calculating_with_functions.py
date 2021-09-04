def zero(a = False): return count(0,a[1],a[0]) if not isinstance(a,int) else 0
def one(a = False): return count(1,a[1],a[0]) if not isinstance(a,int) else 1
def two(a = False): return count(2,a[1],a[0]) if not isinstance(a,int) else 2
def three(a = False): return count(3,a[1],a[0]) if not isinstance(a,int) else 3
def four(a = False): return count(4,a[1],a[0]) if not isinstance(a,int) else 4
def five(a = False): return count(5,a[1],a[0]) if not isinstance(a,int) else 5
def six(a = False): return count(6,a[1],a[0]) if not isinstance(a,int) else 6
def seven(a = False): return count(7,a[1],a[0]) if not isinstance(a,int) else 7
def eight(a = False): return count(8,a[1],a[0]) if not isinstance(a,int) else 8
def nine(a = False): return count(9,a[1],a[0]) if not isinstance(a,int) else 9

def plus(num): return [num,"+"]
def minus(num): return [num,"-"]
def times(num): return [num,"*"]
def divided_by(num): return [num,"/"]


def count(n1,op,n2):
    if op == '+':
        return n1 + n2
    if op == '-':
        return n1 - n2
    if op == '/':
        return int(n1 / n2)

    return n1 * n2

print(seven(times(five())), 35)
print(four(plus(nine())), 13)
print(eight(minus(three())), 5)
print(six(divided_by(two())), 3)


# Best Solution
# def zero(f = None): return 0 if not f else f(0)
# def one(f = None): return 1 if not f else f(1)
# def two(f = None): return 2 if not f else f(2)
# def three(f = None): return 3 if not f else f(3)
# def four(f = None): return 4 if not f else f(4)
# def five(f = None): return 5 if not f else f(5)
# def six(f = None): return 6 if not f else f(6)
# def seven(f = None): return 7 if not f else f(7)
# def eight(f = None): return 8 if not f else f(8)
# def nine(f = None): return 9 if not f else f(9)

# def plus(y): return lambda x: x+y
# def minus(y): return lambda x: x-y
# def times(y): return lambda  x: x*y
# def divided_by(y): return lambda  x: x/y