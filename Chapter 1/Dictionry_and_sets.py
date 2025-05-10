Student_marks={"Ravi":45,"Ashwin":87,"Rinku":89,"Ashish":90}
print(Student_marks["Ravi"])
marks=Student_marks.items()
print(marks)
print(Student_marks.keys())
print(Student_marks.values())
print(Student_marks.update({"Ravi":100}))
print(Student_marks)
print(Student_marks.pop("Ravi"))
print(Student_marks)
print(Student_marks.popitem())

#Set 
s=set() #empty set
s={1,} # set with one element
s={} # empty dictionary not set 