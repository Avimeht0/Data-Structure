import string


name = "Arvind Mehta"
name = name[:4] + 'j' + name[5:]
print(name)

name = list(name)
name[4] = 'n'
name = "".join(name)
print(name)
# Skip value concept 

a="0123456789"
print(a[::3])

letter=""" Dear <|name|> 
You are selected for the <|job|>
Date: <|date|>"""

letter = letter.replace("<|name|>", "Arvind")
letter = letter.replace("<|job|>", "SDE")
letter = letter.replace("<|date|>", "1st Jan 2023")
print(letter)

#find double space 
string1 = "This is  a  string with  double spaces"
def double_space(string):
    count = 0
    for i in range(len(string)-1):
        if string[i] == " " and string[i+1] == " ":
            count += 1
    return count
print(double_space(string1))
print(string1.find("  "))
#remove double space make only one space
string1 = string1.replace("  ", " ")
print(string1)