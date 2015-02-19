def cube(n):
    return n**3

def by_three(n):
    if n % 3 == 0:
        return cube(n)
        print "n is divisible by 3"
    else:
        return False
        print "n is not"
