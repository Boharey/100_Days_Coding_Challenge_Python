#creating a program that takes input of how man

print("***************Welcome to avg height calculator******************")
height_of_students_list =[]
no_of_students = int(input("no of students : "))

#taking height of students in a list
for i in range(no_of_students):
  height = int(input("Height : "))
  height_of_students_list.append(height)

sum = 0
#calculating average
for height in height_of_students_list:
  sum += height

print(f"hence the final avg height is : {sum/no_of_students}")
  
