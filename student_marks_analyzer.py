marks = [78,85,90,65,88,78,92,77,61]
print("Student  marks ",marks)

num_students = len(marks)
print("No.of students ",num_students)

print("Mark of the first student ",marks[0])
print("Mark of the last student ",marks[-1])

print (f"Marks of first 3 students : {marks[0:3]}")
print (f"Marksfrom index to end : {marks[4:]}")

#iterate through marks using loop 
#using enumerate here that includes index and the value so that we do not create seperate variables

for index,mark in enumerate(marks):
    print(f"Student {index+1} : {mark}")
    
total_marks = sum(marks)
avg_marks = total_marks/num_students
smallest_mark = min(marks)
largest_mark= max(marks)

print("Total sum ",total_marks)
print(f"Average {avg_marks:.2f}")
print(f"smallest_mark {smallest_mark}")
print(f"largest_mark {largest_mark}")