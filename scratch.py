def add(a,b):                # Pratham Sharma's Contribution 
    return a+b
def div(a,b):                # Shasya Bhatnagar's Contribution
    return a/b
def subtract(a, b):          # Additya Akash Mishra's Contribution
    return a - b 
def mul(a, b):               # Siddharth Saxena's Contribution
    return a*b 

def calculator(a,b,op):
    ans=0
    if op==1:
        ans=add(a,b)
    elif op==2:
        ans=subtract(a,b)
    elif op==3:
        ans=mul(a,b)
    elif op==4:
        ans=div(a,b)
    else:
        print("Incorrect input")

    print("Output for the given operation is: ",ans)

a=int(input("Enter first value: "))
b=int(input("Enter the second value: "))
print()
print("1:add, 2:subtract, 3:multiplication, 4: division")
op=int(input("Enter your choice for operation: "))
calculator(a,b,op)


