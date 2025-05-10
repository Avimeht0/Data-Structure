def average(a,b,c):
    avg=(a+b+c)/3
    return avg

def average2(a,b,c):
    avg=(a+b+c)/3
    print(f"The given numbers are{a},{b} and {c} and their average is {avg}")

print("The average is:",average(10,20,30))
average2(10,20,30)


def sum_of_natural_numbers(n):
   if n==1:
       return 1
   return n+sum_of_natural_numbers(n-1)
n=int(input("Enter the number: "))
print("The sum of first",n,"natural numbers is:",sum_of_natural_numbers(n))

def multiplication_table(n):
    if n==0:
        return
    multiplication_table(n-1)
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")