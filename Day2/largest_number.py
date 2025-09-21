n=int(input("Enter n value:"))
r=int(input("Enter r value:"))
a=int(input("Enter a value:"))
if n>r>a:
    print("n is largest with value:",n)
elif r>n>a:
    print("r is largest with value:",r)
else:
    print("a is largest with value:",a)