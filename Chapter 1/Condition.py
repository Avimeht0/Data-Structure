sub1=int(input("Enter first subject marks:"))
sub2=int(input("Enter second subject marks:"))
sub3=int(input("Enter thrid subject marks:"))
avg=sum([sub1,sub2,sub3])/3
print("The average is:",avg)
if(avg>=40 and sub1>=33 and sub2>= 33 and sub3>=33):
    print("You are pass")
else:
    print("You are fail")

"""A spam comment as defined as a text containing the following words:
    'make money', 'buy now', 'click this', 'subscribe this', 'buy now', 'click this', 'subscribe this'
    """

spam = input("Enter the comment: ")

if "make money" in spam:
    print("This is a spam comment")
elif "buy now" in spam:
    print("This is a spam comment")
elif "click this" in spam:                                                      
    print("This is a spam comment")
elif "subscribe this" in spam:
    print("This is a spam comment")
elif "buy now" in spam:
    print("This is a spam comment")
elif "click this" in spam:
    print("This is a spam comment")
elif "subscribe this" in spam:
    print("This is a spam comment")
else:
    print("This is not a spam comment")


""" Write a program to culculate the  grade of a student based on the marks 
following scheme:
    90-100 = A+
    80-89 = A
    70-79 = B
    60-69 = C
    50-59 = D
    40-49 = E
    <40 = F
"""
marks=int(input("Enter the marks: "))
