# #write a program give multiplication table of given number .
# num=int(input("Enter the number: "))
# for i in range(1,11):
#     print(num,"*",i,"=",num*i)

# l=["harry","Sohan","Sachin","Ankit"]

# for name in l:
#     if name.startswith("S"):
#         print(f"Hello {name}")

        

# Pattern printing

# n = int(input("Enter the number of rows: "))

# for i in range(1, n + 1):
#     # Print leading spaces
#     print(" " * (n - i), end="")
    
#     # Print asterisks
#     print("*" * (2 * i - 1))

n = int(input("Enter the number of rows: "))
row = n
col = (n * 2) - 1 if n % 2 != 0 else n * 2

for i in range(1, row + 1):
    for j in range(1, col + 1):
        
        
        if (j >= (n - i + 1)) and (j <= (n + i - 1)):
            print("*", end="")
        else:
            print(" ", end="")
    print()
    