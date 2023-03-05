class Solver():
    def __init__(self, var1, var2, var3):
        pass
    def add(a,b):                # Pratham Sharma's Contribution
        return a+b
    def div(a,b):                # Shasya Bhatnagar's Contribution
        return a/b
    def subtract(a, b):          # Additya Akash Mishra's Contribution
        return a - b
    def mul(a, b):               # Siddharth Saxena's Contribution
        return a*b

    def calculator(a, op, b):
        a = int(a)
        b = int(b)
        def add(a,b):                # Pratham Sharma's Contribution
            return a+b
        def div(a,b):                # Shasya Bhatnagar's Contribution
            return a/b
        def subtract(a, b):          # Additya Akash Mishra's Contribution
            return a - b
        def mul(a, b):               # Siddharth Saxena's Contribution
            return a*b

        ans=0
        if op=='+':
            ans=add(a,b)
        elif op=='-':
            ans=subtract(a,b)
        elif op=='*':
            ans=mul(a,b)
        elif op=='/':
            ans=div(a,b)
        else:
            return "Incorrect Operator"

        return ans
